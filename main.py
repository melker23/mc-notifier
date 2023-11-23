import os
import requests
import json

webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
# Read Discord Webhook URL from file
webhook_url_file = "discord_webhook_url.txt"

# Minecraft API URL
minecraft_api = "https://launchermeta.mojang.com/mc/game/version_manifest.json"

# Read stored version from a file
stored_version_file = "stored_version.txt"

# Check if the file exists
if os.path.exists(stored_version_file):
    with open(stored_version_file, "r") as file:
        stored_version = file.read().strip()
else:
    # If the file does not exist, create it with an empty string
    stored_version = ""

# Get the latest Minecraft version
response = requests.get(minecraft_api)
data = response.json()
latest_version = data['latest']['release']

# Check if the latest version has changed
if latest_version != stored_version:
    # Update the stored version
    stored_version = latest_version

    # Send message to Discord webhook
    message = f"Latest Minecraft version updated to {latest_version}."
    requests.post(webhook_url, headers={"Content-Type": "application/json"}, json={"content": message})

    # Update the stored version in the file
    with open(stored_version_file, "w") as file:
        file.write(stored_version)
else:
    # Versions are the same, print the message
    message = f"No change in the latest Minecraft version. Current version: {latest_version}."
    print(message)

# Additional messages for no updates
if not latest_version:
    # Minecraft version not available, print the message
    message = "Unable to retrieve the latest Minecraft version. Please check the API or try again later."
    print(message)
