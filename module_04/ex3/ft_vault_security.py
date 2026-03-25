def ft_vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    read_file_name = "classified_data.txt"
    write_file_name = "classified_data_new.txt"
    print("Initiating secure vault access...")
    try:
        with open(read_file_name, "r") as file:
            print("Vault connection established with failsafe protocols.\n")

            print("SECURE EXTRACTION:")
            for line in file:
                print(line.strip())
    except IOError:
        print(
            f"Error: Unable to access {read_file_name}.",
            "Vault integrity compromised.",
        )
    print()

    try:
        with open(write_file_name, "w") as file:
            print("SECURE PRESERVATION:")
            new_line = "[CLASSIFIED] New security protocols archived\n"
            print(new_line)
            file.write(new_line)
            print("Vault automatically sealed upon completion")
    except IOError:
        print(
            f"Error: Unable to write to {write_file_name}.",
            "Vault integrity compromised.",
        )
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security()
