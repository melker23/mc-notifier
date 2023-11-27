# Minecraft Version Checker

This Python script checks for the latest Minecraft version and sends updates to a Discord webhook.

## Prerequisites

- Python 3.x installed on your system
- Install the required Python packages using the following command:

```bash
pip install -r requirements.txt
```
# Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/melker23/mc-notifier.git
   cd mc-notifier
   ```

# Setting Up Discord Webhook and Running the Script

To receive notifications about the latest Minecraft version updates, you need to set up a Discord webhook and run the script. Follow the steps below:

## Set Up a Discord Webhook

1. Open your Discord server.
2. Navigate to the channel where you want to receive updates.
3. Click on the gear icon next to the channel name and select "Integrations."
4. Click on "Create Webhook."
5. Customize the webhook name, avatar, and select the channel.
6. Copy the webhook URL provided.

## Configuring Discord Webhook in the Script

Create a `.env` file in the project root and add the following line:

```env
DISCORD_WEBHOOK_URL=your_webhook_url_here
```
Replace your_webhook_url_here with the copied webhook URL from the previous step. This environment variable is crucial for the script to send updates to the designated Discord channel.



