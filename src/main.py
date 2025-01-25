from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the date and time as 'YYYY-MM-DD HH:MM:SS'
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")

# Write the formatted date and time to a file
with open("version.md", "w") as file:
    file.write(formatted_now + "\n")


