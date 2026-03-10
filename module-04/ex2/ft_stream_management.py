
import sys

def ft_stream_management() -> None:
	print("=== CYBER ARCHIVES - COMMUNICATION ===\n")
	try:
		archivist_id = accept_input("Enter archivist ID: ")
		status_report = accept_input("Enter status report: ")
		print("\n")

		write_stdout(f"Archive status from {archivist_id}: {status_report}")
		write_stderr("System diagnostic: Communication channels verified")
		write_stdout("Data transmission complete")
		print("\n")

		print("Three-channel communication test successful.")
	except IOError as e:
		print(f"Error: {e}")
		return


def accept_input(msg: str) -> str:
	if sys.stdin.readable():
		print("Input Stream active.", end=" ")
	else:
		raise IOError("Input Stream is not readable.")
	print(msg, end="")
	return input()

def write_stdout(msg: str) -> None:
	if sys.stdout.writable():
		sys.stdout.write("[STANDARD] " + msg + "\n")
	else:
		raise IOError("Output Stream is not writable.")

def write_stderr(msg: str) -> None:
	if sys.stderr.writable():
		sys.stderr.write("[ALERT] " + msg + "\n")
	else:
		raise IOError("Error Stream is not writable.")

if __name__ == "__main__":
	ft_stream_management()
