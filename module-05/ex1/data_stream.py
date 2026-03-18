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

    def __init__(self, stream_id: str):
        self.stream_id = stream_id
        self.number_of_records = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        return [
            item
            for item in data_batch
            if isinstance(item, dict) and criteria in item.keys()
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "data_count": self.number_of_records,
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Dict[str, float]]) -> str:
        if not data_batch:
            return "No data to process."

        self.number_of_records = len(data_batch)
        temp_records = self.filter_data(data_batch, "temp")
        self.average_temp = sum(
            [item.get("temp", 0) for item in temp_records]
        ) / len(temp_records)
        return self.get_stats()

    def filter_data(
        self,
        data_batch: List[Dict[str, float]],
        criteria: List[str] = ["temp", "humidity", "pressure"],
    ) -> List[Dict[str, float]]:
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        print(
            f"Sensor analytics: {self.number_of_records} readings processed,",
            f"avg temp: {self.average_temp:.1f}°C",
        )


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.net_units = 0

    def process_batch(self, data_batch: List[Dict[str, float]]) -> str:
        if not data_batch:
            return "No data to process."
        if not self.filter_data(data_batch):
            return "Data does not meet filter criteria."

        self.number_of_records = len(data_batch)
        total_buy = sum(item.get("buy", 0) for item in data_batch)
        total_sell = sum(item.get("sell", 0) for item in data_batch)
        self.net_units = total_sell - total_buy
        return self.get_stats()

    def filter_data(
        self,
        data_batch: List[Dict[str, float]],
        criteria: List[str] = ["buy", "sell"],
    ) -> List[Dict[str, float]]:
        return [
            item
            for item in data_batch
            if isinstance(item, dict) and any(key in item for key in criteria)
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        symbol = (
            "+" if self.net_units > 0 else "-" if self.net_units < 0 else "0"
        )
        print(
            f"Transaction analytics: {self.number_of_records} operations,",
            f"net flow: {symbol}{self.net_units:.2f} units",
        )


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)

    def filter_data(
        self,
        data_batch: List[str],
        criteria: List[str] = ["login", "error", "logout"],
    ) -> List[str]:
        return super().filter_data(data_batch, criteria)

    def process_batch(self, data_batch: List[str]) -> str:
        if not data_batch:
            return "No data to process."

        self.number_of_records = len(data_batch)
        self.error_count = sum(1 for item in data_batch if "error" in item)
        return self.get_stats()

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        print(
            f"Event analytics: {self.number_of_records} events,",
            f"{self.error_count} errors detected",
        )


class StreamProcessor:
    streams: List[DataStream]

    def __init__(self):
        self.streams = []

    def add_stream(self, stream: DataStream, data_type: str):
        print(f"Stream ID: {stream.stream_id} type: {data_type}")
        self.streams.append({"stream": stream, "type": data_type})

    def process_stream(self, data: List[Any]) -> str:
        for stream_dict in self.streams:
            stream = stream_dict["stream"]
            try:
                results = stream.filter_data(data)
                stream.process_batch(results)
            except Exception as e:
                print(f"Error processing stream {stream.stream_id}: {e}")
                continue


def demo():
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
    print()

    print("Initializing Transaction Stream...")
    transaction_stream = TransactionStream("TRANSACTION_001")
    stream_processor.add_stream(transaction_stream, "Financial Data")
    transaction_data = [
        {"buy": 100.0},
        {"sell": 150.0},
        {"buy": 50.0},
    ]
    print(f"Processing transaction batch: {transaction_data}")
    transaction_stream.process_batch(transaction_data)
    print()

    print("Initializing Event Stream...")
    event_stream = EventStream("EVENT_001")
    stream_processor.add_stream(event_stream, "System Events")
    event_data = ["login", "error", "logout"]
    print(f"Processing event batch: {event_data}")
    event_stream.process_batch(event_data)
    print()

    print("=== Polymorphic Stream Processing ===\n")
    print("Processing mixed stream types through unified interface...")

    mixed_data = [
        {"temp": 25.0},
        {"buy": 200.0},
        {"humidity": 70},
        {"sell": 250.0},
        {"pressure": 1010},
        "login",
        "error: disk full",
        {"temp": 20.0},
    ]

    stream_processor.process_stream(mixed_data)


if __name__ == "__main__":
    demo()
