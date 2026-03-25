def garden_operations() -> None:
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print()

    try:
        print("Testing ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print()

    try:
        print("Testing FileNotFoundError...")
        with open("missing.txt", "r") as file:
            file.read()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print()

    try:
        print("Testing KeyError...")
        missing = {"a": 1, "b": 2}
        print(missing["_plant"])
    except KeyError:
        print("Caught KeyError: 'missing_plant'")
    print()

    # Testing multiple exceptions in one block
    try:
        print("Testing multiple errors together...")
        lst = [1, 2, 3]
        print(lst[5])  # This will raise IndexError
        10 / 0  # This will raise ZeroDivisionError
    except (IndexError, ZeroDivisionError):
        print("Caught an error, but program continues!")
    print()


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
