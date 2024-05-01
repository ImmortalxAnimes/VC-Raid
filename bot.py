import os
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

API_ID = os.environ.get("17271772")
API_HASH = os.environ.get("897542330c90728e4e7fef57f42f9c79")
BOT_TOKEN = os.environ.get("6931069312:AAER2u5Zw_KhM-ZxZPwBBJyWf146nzWGIZA")
ASSISTANT_ID = os.environ.get("BQEHi9wAvRq1uU1SK7y_E7mxlk5EeG1S31Y4Sm6X9mtqeD1levwVaOe3mTpilDv184g6EkjEWRd0cbPBS94sTj89hxPZawWWCRgit_BlrOeF-Xx6WdocQ2Ayok_yBZunQuk9cSD1TvTKGOR2Ov17sXihFUYFjBA3hJ9mpBov8fGyAWCgQiRS6OMafulbYIemXZUK1mPCQ69xygzavQ0gDZQtBFXFyOpIf7-8HN2pXNag5Wn4KEp-LTLfH95hFfWaT7WLA1dxOfAFYlzxUAJ-bUuUYYtkzPm3gEyvW4P56KI3Ls3ZqtAd2MpOYDCTAe7JsRGzZnJzlJnylAAIV7B_gwurHIXd6wAAAAB_Ez2fAA")

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
