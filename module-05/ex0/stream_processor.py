from typing import Any, List
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        if type(data) is str:
            print(f'Processing data: "{data}"')
        else:
            print(f"Processing data: {data}")

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: List[int]) -> str:
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
            if type(item) is not int:
                print(f"Validation failed: {item} is not an integer.")
                return False
        print("Validation: Numeric data verified")

        return True


class TextProcessor(DataProcessor):
    def process(self, data: str) -> str:
        length = len(data)
        numOfWords = len(data.split())
        result = f"Processed text: {length} charcters, {numOfWords} words"

        return self.format_output(result)

    def validate(self, data: str) -> bool:
        if type(data) is not str:
            print(f"Validation failed: {data} is not a string.")
            return False
        print("Validation: Text data verified")

        return True


class LogProcessor(DataProcessor):
    logLevels = ["ERROR", "WARNING", "INFO"]

    def process(self, data: str) -> str:
        log_level = self.get_log_level(data)
        log_msg = data.split(": ", 1)[1]
        result = f"[ALERT] {log_level} level detected: {log_msg}"

        return self.format_output(result)

    def validate(self, data: str) -> bool:
        if type(data) is not str:
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


def stream_processor() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    numProcessor = NumericProcessor()
    testNumData = [1, 2, 3, 4, 5]
    print(f"Processing data: {testNumData}")
    if not numProcessor.validate(testNumData):
        print("Numeric data validation failed. Check input format.")
    else:
        print(numProcessor.process(testNumData), "\n")

    print("Initializing Text Processor...")
    textProcessor = TextProcessor()
    testTextData = "Hello Nexus World"
    print(f'Processing data: "{testTextData}"')
    if not textProcessor.validate(testTextData):
        print("Text data validation failed. Check input format.")
    else:
        print(textProcessor.process(testTextData), "\n")

    print("Initializing Log Processor...")
    logProcessor = LogProcessor()
    testLogData = "ERROR: Connection timeout"
    print(f'Processing data: "{testLogData}"')
    if not logProcessor.validate(testLogData):
        print("Log data validation failed. Check input format.")
    else:
        print(logProcessor.process(testLogData), "\n")

    print("=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data through same interface...")

    processors: List[DataProcessor] = [
        numProcessor,
        textProcessor,
        logProcessor,
    ]
    dataSamples = [
        [2, 2, 2],
        "hello world!",
        "INFO: System ready",
    ]
    for i in range(len(processors)):
        print(f"Result {i+1}: {processors[i].process(dataSamples[i])}")

    print("\nFoundation systems online. Nexus ready for advance streams.")


if __name__ == "__main__":
    stream_processor()
