from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union

# This exercise requires the use of classes with inheritance, super(),
# try/except blocks, list comprehensions for data processing, and ABC
# with @abstractmethod. Type hints from the typing module must be
# used. The isinstance() function is needed for type checking.

# This exercise demonstrates subtype polymorphism in action. Your
# StreamProcessor should be able to handle any DataStream subtype
# without knowing the specific implementation details. This is the
# power of polymorphic design!
# 13


class DataStream(ABC):
    stream_id: str
    number_of_records: int

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.number_of_records = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return [item for item in data_batch if isinstance(item, dict)]

        return [
            item
            for item in data_batch
            if isinstance(item, dict) and criteria in item
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "data_count": self.number_of_records,
        }


class SensorStream(DataStream):
    average_temp: float

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.average_temp = 0.0

    def process_batch(self, data_batch: List[Dict[str, float]]) -> str:
        if not data_batch:
            return "No data to process."

        self.number_of_records = len(data_batch)
        temp_records = self.filter_data(data_batch, "temp")
        if not temp_records:
            return "No temperature data to process."

        self.average_temp = sum(
            item.get("temp", 0.0) for item in temp_records
        ) / len(temp_records)
        return f"Processed {self.number_of_records} sensor records."

    def filter_data(
        self,
        data_batch: List[Dict[str, float]],
        criteria: Optional[str] = None,
    ) -> List[Dict[str, float]]:
        default_keys = ["temp", "humidity", "pressure"]
        include_critical = criteria == "critical"

        filtered_data: List[Dict[str, float]] = []
        for item in data_batch:
            if not isinstance(item, dict):
                continue
            if not any(key in item for key in default_keys):
                continue

            is_critical = ("temp" in item and item.get("temp", 0.0) > 75) or (
                "humidity" in item and item.get("humidity", 0.0) > 80
            )
            if include_critical and not is_critical:
                continue

            filtered_data.append(item)

        return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        print(
            f"Sensor analytics: {self.number_of_records} readings processed,",
            f"avg temp: {self.average_temp:.1f}C",
        )
        return {
            "stream_id": self.stream_id,
            "data_count": self.number_of_records,
            "average_temp": self.average_temp,
        }


class TransactionStream(DataStream):
    net_units: float

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.net_units = 0

    def process_batch(self, data_batch: List[Dict[str, float]]) -> str:
        if not data_batch:
            return "No data to process."

        if not self.filter_data(data_batch):
            return "Data does not meet filter criteria."

        self.number_of_records = len(data_batch)
        total_buy = sum(item.get("buy", 0.0) for item in data_batch)
        total_sell = sum(item.get("sell", 0.0) for item in data_batch)
        self.net_units = total_buy - total_sell
        return f"Processed {self.number_of_records} transaction records."

    def filter_data(
        self,
        data_batch: List[Dict[str, float]],
        criteria: Optional[str] = None,
    ) -> List[Dict[str, float]]:
        default_keys = ["buy", "sell"]
        include_critical = criteria == "critical"

        filtered_data: List[Dict[str, float]] = []
        for item in data_batch:
            if not isinstance(item, dict):
                continue
            if not any(key in item for key in default_keys):
                continue

            is_critical = ("buy" in item and item.get("buy", 0.0) > 1000) or (
                "sell" in item and item.get("sell", 0.0) > 1000
            )
            if include_critical and not is_critical:
                continue

            filtered_data.append(item)

        return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        symbol = "+" if self.net_units > 0 else ""
        print(
            f"Transaction analytics: {self.number_of_records} operations,",
            f"net flow: {symbol}{self.net_units:.2f} units",
        )
        return {
            "stream_id": self.stream_id,
            "data_count": self.number_of_records,
            "net_units": self.net_units,
        }


class EventStream(DataStream):
    error_count: int

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.error_count = 0

    def filter_data(
        self,
        data_batch: List[str],
        criteria: Optional[str] = None,
    ) -> List[str]:
        default_keywords = ["login", "error", "logout"]
        keywords = [criteria] if criteria is not None else default_keywords
        return [
            item
            for item in data_batch
            if isinstance(item, str)
            and any(keyword in item for keyword in keywords)
        ]

    def process_batch(self, data_batch: List[str]) -> str:
        if not data_batch:
            return "No data to process."

        self.number_of_records = len(data_batch)
        self.error_count = sum(1 for item in data_batch if "error" in item)
        return f"Processed {self.number_of_records} event records."

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        print(
            f"Event analytics: {self.number_of_records} events,",
            f"{self.error_count} errors detected",
        )
        return {
            "stream_id": self.stream_id,
            "data_count": self.number_of_records,
            "error_count": self.error_count,
        }


class StreamProcessor:
    batch_count: int
    total_sensor: int
    total_trans: int
    total_event: int
    streams: List[Dict[str, Any]]

    def __init__(self) -> None:
        self.streams = []
        self.batch_count = 0
        self.total_sensor = 0
        self.total_trans = 0
        self.total_event = 0

    def add_stream(self, stream: DataStream, data_type: str) -> None:
        print(f"Stream ID: {stream.stream_id} type: {data_type}")
        self.streams.append({"stream": stream, "type": data_type})

    def process_stream(self, data: List[Any]) -> None:
        self.batch_count += 1
        for stream_dict in self.streams:
            stream = stream_dict["stream"]
            try:
                results = stream.filter_data(data)
                if results:
                    stream.process_batch(results)
                    match stream:
                        case SensorStream():
                            self.total_sensor += stream.number_of_records
                        case TransactionStream():
                            self.total_trans += stream.number_of_records
                        case EventStream():
                            self.total_event += stream.number_of_records
            except Exception:
                continue

        print(
            f"Batch {self.batch_count} Results:",
            f"- Sensor data: {self.total_sensor} readings processed,",
            f"- Transaction data: {self.total_trans} operations processed,",
            f"- Event data: {self.total_event} events processed",
            "\n",
            sep="\n",
        )

        print("Stream filtering active: High-priority data only")
        critical_sensor_data = 0
        critical_trans_data = 0
        for stream_dict in self.streams:
            stream = stream_dict["stream"]
            try:
                stream_critical_data = stream.filter_data(
                    data, criteria="critical"
                )
                match stream:
                    case SensorStream():
                        critical_sensor_data += len(stream_critical_data)
                    case TransactionStream():
                        critical_trans_data += len(stream_critical_data)
            except Exception:
                continue
        print(
            "Filtered results:",
            f"{critical_sensor_data} critical sensor alerts,",
            f"{critical_trans_data} large transactions\n",
        )


def demo() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    stream_processor = StreamProcessor()
    print("Initializing Sensor Stream...")
    sensor_stream = SensorStream("SENSOR_001")
    stream_processor.add_stream(sensor_stream, "Environmental Data")
    sensor_data = [
        {"temp": 22.5},
        {"humidity": 65},
        {"pressure": 1013},
    ]
    print(f"Processing sensor batch: {sensor_data}")
    sensor_stream.process_batch(sensor_data)
    sensor_stream.get_stats()
    print()

    print("Initializing Transaction Stream...")
    transaction_stream = TransactionStream("TRANSACTION_001")
    stream_processor.add_stream(transaction_stream, "Financial Data")
    transaction_data = [
        {"buy": 100.0},
        {"sell": 150.0},
        {"buy": 75.0},
    ]
    print(f"Processing transaction batch: {transaction_data}")
    transaction_stream.process_batch(transaction_data)
    transaction_stream.get_stats()
    print()

    print("Initializing Event Stream...")
    event_stream = EventStream("EVENT_001")
    stream_processor.add_stream(event_stream, "System Events")
    event_data = ["login", "error", "logout"]
    print(f"Processing event batch: {event_data}")
    event_stream.process_batch(event_data)
    event_stream.get_stats()
    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    mixed_data = [
        {"temp": 80.0},
        {"buy": 200.0},
        {"humidity": 90},
        {"sell": 250.0},
        {"buy": 200.0},
        "login",
        "error: disk full",
        "logout",
        {"buy": 20000.0},
    ]
    stream_processor.process_stream(mixed_data)

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    demo()
