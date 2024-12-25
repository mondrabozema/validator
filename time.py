import time
from datetime import datetime

# Specify the file where the date will be saved
file_name = "current_date.txt"

try:
    print(f"Saving the current date and time to {file_name} every 5 seconds. Press Ctrl+C to stop.")
    while True:
        # Get the current date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Write the current time to the file
        with open(file_name, "a") as file:
            file.write(current_time + "\n")

        # Wait for 5 seconds
        time.sleep(5)
except KeyboardInterrupt:
    print("\nScript stopped by user.")
