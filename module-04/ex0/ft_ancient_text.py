def ft_ancient_text() -> None:
	print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

	file_name = "ancient_fragment.txt"

	print(f"Accessing Storage Vault: {file_name}")
	try:
		file = open(file_name, "r")
		print("Connection established...\n")
		print("RECOVERED DATA:")

		for line in file:
			print(line, end="")
		
		print("\n\nData recovery complete. Storage unit disconnected.")
		file.close()
	except FileNotFoundError:
		print("File not found.")

if __name__ == "__main__":
	ft_ancient_text()
