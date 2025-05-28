import datetime
import sys

def main():
    print("Hello from GitHub Actions!")

if __name__ == "__main__":
    # Create a timestamped log file
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = f"logs_{timestamp}.txt"

    # Redirect stdout and stderr to the log file
    sys.stdout = open(log_file, "w")
    sys.stderr = sys.stdout

    main()
