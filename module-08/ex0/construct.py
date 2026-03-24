import os
from site import getusersitepackages
import sys


def construct():
    print("\nMATRIX STATUS: ", end="")
    is_virtual_env = (
        "VIRTUAL_ENV" in os.environ or sys.prefix != sys.base_prefix
    )
    if is_virtual_env:
        print("Welcome to the construct")
    else:
        print("You're still plugged in")
    print("")

    print(f"Current Python: {sys.executable}")
    print(
        "Virtual Environment:",
        f"{sys.prefix if is_virtual_env else 'None detected'}",
    )
    if is_virtual_env:
        print(
            "Environment path:", f"{os.environ.get('VIRTUAL_ENV', sys.prefix)}"
        )
    print("")

    if is_virtual_env:
        print(
            "SUCCESS: You're in an isolated environment!",
            "Safe to install packages without affecting the global system\n",
        )
        print("Package installation path:", getusersitepackages())
    else:
        print(
            "WARNING: You're in the global environment!",
            "The machines can see everything you install\n",
        )
        print(
            "To enter the construct, run:",
            "python -m venv matrix_env",
            "source matrix_env/bin/activate # On Unix",
            "matrix_env\\Scripts\\activate # On Windows",
            sep="\n",
        )
        print(
            "\nThen run this program again.",
        )


if __name__ == "__main__":
    construct()
