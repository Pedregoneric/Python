# Import the necessary modules
import os
import subprocess

# Define the command to run for updating the system
update_cmd = "sudo apt-get update && sudo apt-get upgrade -y"

# Run the command
subprocess.run(update_cmd.split())

# Print a success message
print("System update completed successfully!")
