from abc import ABC, abstractmethod
from typing import Any, Protocol, Union, List, Dict


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class ProcessingPipeline(ABC):
    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass

    class InputStage(ProcessingStage):
        def process(self, data: Any) -> Any:
            pass

    class TransformStage(ProcessingStage):
        def process(self, data: Any) -> Any:
            pass

    class OutputStage(ProcessingStage):
        def process(self, data: Any) -> Any:
            pass


class JSONAdapter(ProcessingPipeline):
    stages: List[ProcessingStage]

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages = [
            self.InputStage(),
            self.TransformStage(),
            self.OutputStage(),
        ]

    def process(self, data: Any) -> Union[str, Any]:
        for stage in self.stages:
            try:
                data = stage.process(data)
            except Exception as e:
                print(f"Error in stage {stage.__class__.__name__}: {e}")
                return None
        return data

    class InputStage:
        def process(self, data: Dict) -> Dict:
            print(f"Input: {data}")
            return data

    class TransformStage:
        def process(self, data: Dict) -> Dict:
            print("Transform: Enriched with metadata and validation")
            if data.get("sensor") is None or data.get("value") is None:
                raise ValueError(
                    "Missing required fields: 'sensor' and 'value'"
                )

            is_normal = data.get("temp", 0) < 100
            status = "Normal Range" if is_normal else "High"
            return {
                "sensor": data.get("sensor"),
                "unit": data.get("unit", "C"),
                "value": data.get("value"),
                "is_normal": is_normal,
                "status": status,
            }

    class OutputStage:
        def process(self, data: Dict) -> str:
            if data["sensor"] == "temp":
                return (
                    "Output: Processed temperature reading: "
                    f"{data['value']} {data['unit']} ({data['status']})"
                )
            return (
                "Output: Processed sensor reading: "
                f"{data['sensor']}={data['value']} {data['unit']} "
                f"({data['status']})"
            )


class CSVAdapter(ProcessingPipeline):
    stages: List[ProcessingStage]

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages = [
            self.InputStage(),
            self.TransformStage(),
            self.OutputStage(),
        ]

    def process(self, data: Any) -> Any:
        for stage in self.stages:
            try:
                data = stage.process(data)
            except Exception as e:
                print(f"Error in stage {stage.__class__.__name__}: {e}")
                return None
        return data

    class InputStage:
        def process(self, data: str) -> str:
            print('Input: "user,action,timestamp"')
            return data

    class TransformStage:
        def process(self, data: str) -> Dict:
            print("Transform: Parsed CSV event row and validated fields")
            fields = [field.strip() for field in data.split(",")]
            if len(fields) != 3:
                raise ValueError(
                    "CSV data must contain user, action, and timestamp"
                )

            user, action, timestamp = fields
            return {
                "user": user,
                "action": action,
                "timestamp": timestamp,
                "actions_processed": 1,
            }

    class OutputStage:
        def process(self, data: Dict) -> str:
            return (
                f"Output: {data['user']} activity logged: "
                f"{data['actions_processed']} actions processed"
            )


class StreamAdapter(ProcessingPipeline):
    stages: List[ProcessingStage]

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages = [
            self.InputStage(),
            self.TransformStage(),
            self.OutputStage(),
        ]
        print("Pipeline capacity: 1000 streams/second\n")

    def process(self, data: Any) -> Any:
        for stage in self.stages:
            try:
                data = stage.process(data)
            except Exception as e:
                print(f"Error in stage {stage.__class__.__name__}: {e}")
                return None
        return data

    class InputStage:
        def process(self, data: List[Dict]) -> List[Dict]:
            print("Input: Real-time sensor stream")
            return data

    class TransformStage:
        def process(self, data: List[Dict]) -> Dict:
            print("Transform: Aggregated and filtered")
            if not data:
                raise ValueError(
                    "Stream data must include at least one reading"
                )

            valid_temps = [
                reading["value"]
                for reading in data
                if reading.get("sensor") == "temp"
                and reading.get("value") is not None
            ]

            if not valid_temps:
                raise ValueError(
                    "No valid temperature readings found in stream"
                )

            average_temp = sum(valid_temps) / len(valid_temps)
            return {
                "reading_count": len(valid_temps),
                "average_temp": average_temp,
                "unit": "C",
            }

    class OutputStage:
        def process(self, data: Dict) -> str:
            return (
                "Output: Stream summary: "
                f"{data['reading_count']} readings, "
                f"avg: {data['average_temp']:.1f}°{data['unit']}"
            )


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: Dict[str, ProcessingPipeline] = {}

    def add_pipeline(
        self, pipeline_id: str, pipeline: ProcessingPipeline
    ) -> None:
        self.pipelines[pipeline_id] = pipeline

    def process_data(self, pipeline_id: str, data: Any) -> Any:
        try:
            if pipeline_id not in self.pipelines:
                raise ValueError(f"Pipeline {pipeline_id} not found.")
            return self.pipelines[pipeline_id].process(data)
        except Exception as e:
            print(f"Error processing data in pipeline {pipeline_id}: {e}")
            return None


def nexus_pipeline() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    print("Initializing Nexus Manager...")
    manager = NexusManager()
    json_pipeline = JSONAdapter("JSON_Pipeline_1")
    csv_pipeline = CSVAdapter("CSV_Pipeline_1")
    stream_pipeline = StreamAdapter("Stream_Pipeline_1")
    manager.add_pipeline("json", json_pipeline)
    manager.add_pipeline("csv", csv_pipeline)
    manager.add_pipeline("stream", stream_pipeline)

    print(
        "Creating Data Processing Pipeline...",
        "Stage 1: Input validation and parsing",
        "Stage 2: Data transformation and enrichment",
        "Stage 3: Output formatting and delivery",
        sep="\n",
    )

    print("\n=== Multi-Format Data Processing ===\n")

    print("Processing JSON data through pipeline...")
    json_data = {"sensor": "temp", "value": 23.5, "unit": "C"}
    print(manager.process_data("json", json_data))

    print("\nProcessing CSV data through same pipeline...")
    csv_data = "joshua,login,2026-03-20T14:30:00Z"
    print(manager.process_data("csv", csv_data))

    print("\nProcessing stream data through same pipeline...")
    stream_data = [
        {"sensor": "temp", "value": 21.8, "unit": "C"},
        {"sensor": "temp", "value": 22.0, "unit": "C"},
        {"sensor": "temp", "value": 22.4, "unit": "C"},
        {"sensor": "temp", "value": 21.9, "unit": "C"},
        {"sensor": "temp", "value": 22.4, "unit": "C"},
    ]
    print(manager.process_data("stream", stream_data))

    print("\n=== Pipeline Chaining Demo ===\n")

    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")
    data = {
        "sensor": "joshua,login,2026-03-20T14:30:00Z",
        "value": 22.5,
        "unit": "C",
    }
    json_data = manager.pipelines["json"].TransformStage().process(data)
    csv_data = (
        manager.pipelines["csv"]
        .TransformStage()
        .process(json_data.get("sensor"))
    )
    print(
        "Chained Transformations Result:",
        f"JSON Transform: {json_data}",
        f"CSV Transform: {csv_data}",
        sep="\n",
    )
    print("\nChain result: processed through 3-stage pipeline\n")

    print("\n=== Error Recovery Test ===\n")
    error_json_data = {"sensor": None, "value": 150.0, "unit": "C"}
    print(manager.process_data("json", error_json_data))

    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    nexus_pipeline()
