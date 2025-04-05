from pyrogram import Client, filters
from AotBeats import app  # Keep normal import, only text will be styled

@app.on_message(filters.command("weather"))
def weather(client, message):
    try:
        # Get the location from user message
        user_input = message.command[1]
        location = user_input.strip()
        weather_url = f"https://wttr.in/{location}.png"
        
        # Reply with the weather information as a photo
        message.reply_photo(photo=weather_url, caption="**ʜᴇʀᴇ'ꜱ ᴛʜᴇ ᴡᴇᴀᴛʜᴇʀ ꜰᴏʀ ʏᴏᴜʀ ʟᴏᴄᴀᴛɪᴏɴ — ᴀᴏᴛʙᴇᴀᴛs**")
    except IndexError:
        # User didn't provide a location
        message.reply_text("**ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ʟᴏᴄᴀᴛɪᴏɴ. ᴜꜱᴇ /ᴡᴇᴀᴛʜᴇʀ ɴᴇᴡ ʏᴏʀᴋ — ᴀᴏᴛʙᴇᴀᴛs**")
