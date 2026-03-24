def ft_crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    lost_file_name = "lost_archive.txt"
    forbidden_file_name = "classified_data.txt"
    standard_file_name = "standard_archive.txt"

    # Access file that does not exist
    print(f"CRISIS ALERT: Attemping access to '{lost_file_name}'...")
    try:
        with open(lost_file_name, "r") as file:
            print("Access granted to lost archive. Retrieving data...\n")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage martix")
    except IOError as error:
        print(f"RESPONSE: Unexpected error accessing lost archive - {error}")
    finally:
        print("STATUS: Crisis handled, system stable")

    # Access file without permissions
    print(f"\nCRISIS ALERT: Attempting access to '{forbidden_file_name}'...")
    try:
        with open(forbidden_file_name, "r") as file:
            print("Access granted to forbidden archive. Retrieving data...\n")
            for line in file:
                print(line.strip())
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except IOError as error:
        # Make sure file exists with read permissions removed to test.
        print(
            f"RESPONSE: Unexpected error accessing forbidden archive - {error}"
        )
    finally:
        print("STATUS: Crisis handled, system maintained")

    # Access file with permissions
    print(f"\nROUTINE ACCESS: Attempting access to '{standard_file_name}'...")
    try:
        with open(standard_file_name, "r") as file:
            print("Archived recovered - ", end="")
            for line in file:
                print(f"''{line.strip()}''")
    except IOError as error:
        print(
            f"RESPONSE: Unexpected error accessing standard archive - {error}"
        )
    finally:
        print("STATUS: Normal operations resumed")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
