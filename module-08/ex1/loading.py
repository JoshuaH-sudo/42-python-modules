def loading():
    print("LOADING STATUS: loading programs... *\n")
    print("Checking dependencies:")
    all_imported = False
    try:
        import pandas as pd

        print(f"[OK] {pd} ({pd.__version__} - Data manipulation ready )")
        import numpy as np

        print(f"[OK] {np} ({np.__version__} - Numerical computing ready )")
        import matplotlib as mpl

        print(f"[OK] {mpl} ({mpl.__version__} - Visualization ready )")
        all_imported = True
    except ImportError as e:
        print(
            f"[ERROR] Missing dependencies '{e.name}'!",
        )
    if not all_imported:
        print(
            "\nPlease install the missing dependencies with pip or poetry:",
        )
        print("\nThen run this program again.")
        exit(1)
    print("\nAll dependencies checked. Ready to enter the construct!")


if __name__ == "__main__":
    loading()
