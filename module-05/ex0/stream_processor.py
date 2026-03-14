from typing import Any, List
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        if isinstance(data, str):
            print(f'Processing data: "{data}"')
        else:
            print(f"Processing data: {data}")

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self):
        print("Initializing Numeric Processor...")

    def process(self, data: List[int]) -> str:
        super().process(data)

        if not self.validate(data):
            return "Invalid data: All items must be integers."
        length = data.__len__()
        sumValues = sum(data)
        average = sumValues / length
        result = (
            f"Processed {length} numeric values, "
            f"sum={sumValues}, avg={average:.1f}"
        )

        return self.format_output(result)

    def validate(self, data: List[int]) -> bool:
        for item in data:
            if not isinstance(item, int):
                print(f"Validation failed: {item} is not an integer.")
                return False
        print("Validation: Numeric data verified")

        return True


class TextProcessor(DataProcessor):
    def __init__(self):
        print("Initializing Text Processor...")

    def process(self, data: str) -> str:
        super().process(data)

        if not self.validate(data):
            return "Invalid data: Input must be a string."
        length = len(data)
        numOfWords = len(data.split())
        result = f"Processed text: {length} charcters, {numOfWords} words"

        return self.format_output(result)

    def validate(self, data: str) -> bool:
        if not isinstance(data, str):
            print(f"Validation failed: {data} is not a string.")
            return False
        print("Validation: Text data verified")

        return True


class LogProcessor(DataProcessor):
    logLevels = ["ERROR", "WARNING", "INFO"]

    def __init__(self):
        print("Initializing Log Processor...")

    def process(self, data: str) -> str:
        super().process(data)

        if not self.validate(data):
            return "Invalid data: Input must be a string."
        log_level = self.get_log_level(data)
        log_msg = data.split(": ", 1)[1]
        result = f"[ALERT] {log_level} level detected: {log_msg}"

        return self.format_output(result)

    def validate(self, data: str) -> bool:
        if not isinstance(data, str):
            print(f"Validation failed: {data} is not a string.")
            return False
        if not any(level in data for level in self.logLevels):
            print(f"Validation failed: No valid log level found in {data}.")
            return False
        print("Validation: Log entry verified")

        return True

    def get_log_level(self, data: str) -> str:
        for level in self.logLevels:
            if level in data:
                return level

        return "UNKNOWN"


def stream_processor():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    numProcessor = NumericProcessor()
    testNumData = [1, 2, 3, 4, 5]
    print(numProcessor.process(testNumData), "\n")

    textProcessor = TextProcessor()
    testTextData = "Hello Nexus World"
    print(textProcessor.process(testTextData), "\n")

    logProcessor = LogProcessor()
    testLogData = "ERROR: Connection timeout"
    print(logProcessor.process(testLogData), "\n")

    print("=== Polymorphic Processing Demo ===")


if __name__ == "__main__":
    stream_processor()
