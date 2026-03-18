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

    def __init__(self, stream_id: str, type: str):
        self.stream_id = stream_id
        print(f"Stream ID: {self.stream_id}, Type: {type}")

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
        super().__init__(stream_id, "Sensor")


class TransactionStream(DataStream):
    def __init__(
        self,
        stream_id: str,
    ):
        super().__init__(stream_id, "Transaction")


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "Event")


class StreamProcessor:
    def __init__(self, stream: DataStream):
        self.stream = stream

    def process_stream(self, data: List[Any]) -> str:
        try:
            if not self.stream.filter_data(data):
                raise ValueError("Data does not meet filter criteria.")
            return self.stream.process_batch(data)
        except Exception as e:
            return f"Error processing stream: {e}"


def main():
    sensor_stream = SensorStream("SENSOR_001")
    transaction_stream = TransactionStream("TRANS_001")
    event_stream = EventStream("EVENT_001")

    processor = StreamProcessor(sensor_stream)
    print(
        processor.process_stream(
            [{"temp": 22.0}, {"humidity": 65}, {"pressure": 1013}]
        )
    )

    processor.stream = transaction_stream
    print(
        processor.process_stream(
            [{"buy": 100.0}, {"sell": 150.0}, {"buy": 75.0}]
        )
    )

    processor.stream = event_stream
    print(processor.process_stream(["login", "logout", "error"]))
