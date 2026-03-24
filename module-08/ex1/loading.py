def loading():
    print("LOADING STATUS: loading programs...\n")
    print("Checking dependencies:")
    all_imported = False
    try:
        import pandas as pd

        print(
            f"[OK] {pd.__name__} ({pd.__version__})",
            "- Data manipulation ready",
        )
        import numpy as np

        print(
            f"[OK] {np.__name__} ({np.__version__})",
            "- Numerical computing ready",
        )
        import matplotlib as mlp
        from matplotlib import pyplot as plt

        print(
            f"[OK] {mlp.__name__} ({mlp.__version__})", "- Visualization ready"
        )
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
    else:
        print("")

    sample_matrix_data = np.random.rand(1000, 1000)
    print("Analysing Matrix data...")
    analysis_result = np.mean(sample_matrix_data, axis=0)
    print("Processing 1000 data points...")
    processed_data = pd.DataFrame(analysis_result, columns=["Mean Value"])
    print("Generating visualization...")
    plt.bar(processed_data.index, processed_data["Mean Value"])
    plt.savefig("matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    loading()
