from pyrogram import Client, filters
import os
import zipfile
import asyncio
from AotBeats import app


async def zip_file(file_path, zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.write(file_path, os.path.basename(file_path))


async def unzip_file(zip_file_path, output_folder):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        zip_file.extractall(output_folder)


@app.on_message(filters.command("zip"))
async def zip_command(client, message):
    if message.reply_to_message and message.reply_to_message.document:
        m = await message.reply_text("**ᴢɪᴘᴘɪɴɢ ғɪʟᴇ...**")

        # Download the document
        original_file = await client.download_media(message.reply_to_message)
        zip_file_path = f"{original_file}.zip"

        await asyncio.sleep(1)
        await m.edit("**ᴄᴏᴍᴘʀᴇssɪɴɢ ғɪʟᴇ...**")

        # Zip the file
        await zip_file(original_file, zip_file_path)

        await asyncio.sleep(1)
        await m.edit("**ᴜᴘʟᴏᴀᴅɪɴɢ ᴢɪᴘᴘᴇᴅ ғɪʟᴇ...**")

        # Send the zipped file
        await message.reply_document(zip_file_path)

        await m.edit("**✅ ᴢɪᴘᴘɪɴɢ ᴄᴏᴍᴘʟᴇᴛᴇ!**")

        # Cleanup
        os.remove(zip_file_path)
        os.remove(original_file)

    else:
        await message.reply_text("**ʀᴇᴘʟʏ ᴛᴏ ᴀ ғɪʟᴇ ᴡɪᴛʜ /ᴢɪᴘ ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ɪᴛ ᴛᴏ ᴀ ᴢɪᴘ ғɪʟᴇ.**")


@app.on_message(filters.command("unzip"))
async def unzip_command(client, message):
    if message.reply_to_message and message.reply_to_message.document and message.reply_to_message.document.file_name.endswith(".zip"):
        m = await message.reply_text("**ᴜɴᴢɪᴘᴘɪɴɢ ғɪʟᴇ...**")

        # Download the zip file
        zip_file_path = await client.download_media(message.reply_to_message)
        output_folder = zip_file_path.replace(".zip", "_unzipped")

        await asyncio.sleep(1)
        await m.edit("**ᴇxᴛʀᴀᴄᴛɪɴɢ ғɪʟᴇs...**")

        # Create output folder
        os.makedirs(output_folder, exist_ok=True)

        # Unzip the file
        await unzip_file(zip_file_path, output_folder)

        await asyncio.sleep(1)
        await m.edit("**ᴜᴘʟᴏᴀᴅɪɴɢ ᴇxᴛʀᴀᴄᴛᴇᴅ ғɪʟᴇs...**")

        # Send extracted files
        for root, dirs, files in os.walk(output_folder):
            for file in files:
                file_path = os.path.join(root, file)
                await message.reply_document(file_path)

        await m.edit("**✅ ᴜɴᴢɪᴘᴘɪɴɢ ᴄᴏᴍᴘʟᴇᴛᴇ!**")

        # Cleanup
        for root, dirs, files in os.walk(output_folder, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(output_folder)
        os.remove(zip_file_path)

    else:
        await message.reply_text("**ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴢɪᴘ ғɪʟᴇ ᴡɪᴛʜ /ᴜɴᴢɪᴘ ᴛᴏ ᴇxᴛʀᴀᴄᴛ ɪᴛs ᴄᴏɴᴛᴇɴᴛs.**")
