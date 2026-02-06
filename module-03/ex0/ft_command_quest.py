import sys


def ft_command_quest() -> None:
    print("=== Command Quest ===")
    program_name = sys.argv[0]
    total_arguments = len(sys.argv)
    if len(sys.argv) < 2:
        print("No arguments provided!")
    print(f"Program name: {program_name}")
    i = 1
    if total_arguments > 1:
        print(f"Arguments received: {total_arguments - 1}")
    while i < total_arguments:
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1
    print(f"Total arguments: {total_arguments}")


if __name__ == "__main__":
    ft_command_quest()
