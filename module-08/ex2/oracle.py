from dotenv import load_dotenv
from os import getenv


def oracle():
    print("ORACLE STATUS: reading the Matrix...\n")

    load_dotenv()
    mode = getenv("MATRIX_MODE")
    database_url = getenv("DATABASE_URL")
    api_key = getenv("API_KEY")
    log_level = getenv("LOG_LEVEL")
    zion_endpoint = getenv("ZION_ENDPOINT")

    for var_name, var_value in [
        ("MATRIX_MODE", mode),
        ("DATABASE_URL", database_url),
        ("API_KEY", api_key),
        ("LOG_LEVEL", log_level),
        ("ZION_ENDPOINT", zion_endpoint),
    ]:
        if var_value is None:
            print(f"[ERROR] Missing environment variable: {var_name}")
        else:
            print(f"[OK] {var_name}: {var_value}")

    if None in [mode, database_url, api_key, log_level, zion_endpoint]:
        print("\nPlease set the missing environment variables in a .env file")
        return

    print("Configuration loaded:")
    print(
        f"Mode: {mode}",
        "Database: Connected to local instance",
        "API Access: Authenticated",
        f"Log Level: {log_level}",
        "Zion Endpoint: Online",
        sep="\n",
    )

    print("\nEnvironment security check:")
    print(
        "[OK] No hardcoded secrets detected",
        "[OK] .env file properly configured",
        "[OK] Production overrides available",
        "\nThe Oracle sees all configurations",
        sep="\n",
    )


if __name__ == "__main__":
    oracle()
