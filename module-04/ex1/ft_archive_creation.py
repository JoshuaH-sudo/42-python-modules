def ft_archive_creation() -> None:
	print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
	archive_name = "new_discovery.txt"

	data_to_store = [
		"New quantum algorithm discovered",
		"Efficiency increased by 347%",
		"Archived by Data Archivist trainee"
	]

	print(f"Initializing new storage unit: {archive_name}")

	try:
		file = open(archive_name, "w")
		print("Storage unit ready for data input...\n")

		i = 1
		for line in data_to_store:
			entry = f"[ENTRY {i:03d}] {line}\n"
			print(entry, end="")
			file.write(entry)
			i += 1
		
		print("\nData inscription complete. Storage unit sealed.")
		file.close()
	except IOError:
		print("Error writing to file.")

if __name__ == "__main__":
	ft_archive_creation()
