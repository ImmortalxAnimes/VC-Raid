import os
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

API_ID = os.environ.get("17271772")
API_HASH = os.environ.get("897542330c90728e4e7fef57f42f9c79")
BOT_TOKEN = os.environ.get("AAER2u5xZPwBBJyWf146nzWGIZA")
ASSISTANT_ID = ()

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
