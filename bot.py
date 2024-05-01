import os
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ASSISTANT_ID = os.environ.get("ASSISTANT_ID")

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
pytgcalls = PyTgCalls(app)


@app.on_message(filters.command("play", prefixes="/") & filters.private)
async def play_music(client, message):
    chat_id = message.chat.id
    # Check if the user is the assistant
    if chat_id == ASSISTANT_ID:
        # Join the voice chat
        await pytgcalls.join_group_call(chat_id)
        # Play the music file (replace with your actual file)
        await pytgcalls.start_audio(message.chat.id, "path_to_music_file.mp3")


app.run()
