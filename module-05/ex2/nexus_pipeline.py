# This exercise requires the use of classes with inheritance, super(),
# try/except blocks, list and dict comprehensions for data processing,
# ABC with @abstractmethod, and Protocol for duck typing. The
# collections module is authorized for advanced data structures.
# Type hints from typing module (including Protocol) must be used
# throughout

# ProcessingStage (Protocol): Interface for stages using duck typing. Any class
# with process() can act as a stage.
# •ProcessingPipeline (ABC): Abstract base managing stages. Contains a list of
# stages and orchestrates data ow.
# •Stage Classes: InputStage, TransformStage, OutputStage implement the Pro-
# tocol (duck typing, no inheritance). No constructor parameters.
# •Adapter Classes: JSONAdapter, CSVAdapter, StreamAdapter inherit from ProcessingPipeline
# and override process(). Each takes pipeline_id parameter.
# •NexusManager: Orchestrates multiple pipelines polymorphically.
# •Key Relationships: Composition (contains), Inheritance (inherits from), Imple-
# mentation (implements protocol).
# Required Implementation:
# •Create a exible ProcessingPipeline abstract base class with congurable pro-
# cessing stages
# •Use Protocol or duck typing for stage interfaces (stages must have a process()
# method)
# •Implement specialized pipeline stages (InputStage, TransformStage, OutputStage)
# with process() methods
# •Build data adapters (JSONAdapter, CSVAdapter, StreamAdapter) that inherit
# from ProcessingPipeline
# •Each adapter should override the process() method for format-specic handling
# •Create a NexusManager that orchestrates multiple pipelines polymorphically
# •Demonstrate pipeline chaining where output from one pipeline feeds into another
# •Include comprehensive error handling and recovery mechanisms
# •Add performance monitoring and pipeline statistics

# This is your masterpiece! Demonstrate how method overriding and
# subtype polymorphism enable building complex, maintainable systems.
# Your pipeline should handle any data type or processing requirement
# through polymorphic interfaces.
# 17


from abc import ABC, abstractmethod
from typing import Any, Protocol, Union


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class InputStage:
    def process(self, data) -> dict:
        print(f"Input: {data}")
        return data


class TransformStage:
    def process(self, data) -> dict:
        print("Transform: Enriched with metadata and validation")
        return data


class OutputStage:
    def process(self, data) -> dict:
        print(f"Output: {data}")
        return data


class ProcessingPipeline(ABC):
    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        print(f"Processing JSON data in pipeline {self.pipeline_id}")
        InputStage().process(data)
        TransformStage().process(data)
        OutputStage().process(data)


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Any:
        print(f"Processing CSV data in pipeline {self.pipeline_id}")
        return super().process(data)


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str):
        self.pipeline_id = pipeline_id
        print("Pipeline capacity: 1000 streams/second\n")

    def process(self, data: Any) -> Any:
        print(f"Processing Stream data in pipeline {self.pipeline_id}")
        return super().process(data)


class NexusManager:
    def __init__(self):
        self.pipelines = {}

    def add_pipeline(self, pipeline_id: str, pipeline: ProcessingPipeline):
        self.pipelines[pipeline_id] = pipeline

    def process_data(self, pipeline_id: str, data: Any) -> Any:
        if pipeline_id not in self.pipelines:
            raise ValueError(f"Pipeline {pipeline_id} not found.")
        return self.pipelines[pipeline_id].process(data)


def nexus_pipeline():
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
    json_data = {"name": "Nexus", "type": "Pipeline", "version": 1.0}
    manager.process_data("json", json_data)


if __name__ == "__main__":
    nexus_pipeline()
