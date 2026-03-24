import importlib


def loading():
    print("LOADING STATUS: loading programs...\n")
    print("Checking dependencies:")
    dependencies = [
        ("pandas", "Data manipulation ready"),
        ("numpy", "Numerical computing ready"),
        ("matplotlib", "Visualization ready"),
        ("matplotlib.pyplot", "Plotting backend ready"),
    ]
    imported_modules = {}
    missing_dependencies = []

    for module_name, status_message in dependencies:
        try:
            imported_module = importlib.import_module(module_name)
            imported_modules[module_name] = imported_module
            display_name = module_name
            try:
                display_version = imported_module.__version__
            except AttributeError:
                display_version = "n/a"
            print(
                f"[OK] {display_name} ({display_version})",
                f"- {status_message}",
            )
        except ImportError:
            missing_dependencies.append(module_name)

    if missing_dependencies:
        print("\n[ERROR] Missing dependencies detected:")
        for module_name in missing_dependencies:
            print(f"- {module_name}")
        print(
            "\nPlease install the missing dependencies with pip or poetry:",
        )
        print("\nThen run this program again.")
        exit(1)
    else:
        print("")

    pd = imported_modules["pandas"]
    np = imported_modules["numpy"]
    plt = imported_modules["matplotlib.pyplot"]

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
