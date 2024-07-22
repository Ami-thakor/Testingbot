from pyrogram import Client, filters
import os
API_ID = 28160559
API_HASH = "ca5085c3f41b16df46dbeebed6e56081"
BOT_TOKEN = os.environ.get(
    "BOT_TOKEN", "5451700594:AAFctiKjMSOy1bYo3eGcMO0vue1JE5MgnL8"
)

# Initialize the Client
app = Client("hello_world_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Define a handler for the /start command
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Hello, World!")

# Run the bot
app.run()
