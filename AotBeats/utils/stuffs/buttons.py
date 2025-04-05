from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("◈ ɢʀᴏᴜᴘ ◈", callback_data="mplus HELP_Group"), 
    InlineKeyboardButton("◈ sᴛɪᴄᴋᴇʀs ◈", callback_data="mplus HELP_Sticker"),
    InlineKeyboardButton("◈ ᴀɪ-ʜᴇʟᴘ ◈", callback_data="mplus HELP_ChatGPT")],
    [InlineKeyboardButton("◈ ɪɴꜰᴏ ◈", callback_data="mplus HELP_Info"), 
    InlineKeyboardButton("◈ ᴛᴀɢ-ᴀʟʟ ◈", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("◈ ᴇxᴛʀᴀs ◈", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("◈ ʙᴀɴ-ᴜɴʙᴀɴ ◈", callback_data="mplus HELP_Action"),
    InlineKeyboardButton("◈ ɢᴏᴏɢʟᴇ ◈", callback_data="mplus HELP_Search"),
    InlineKeyboardButton("◈ ɪᴍᴀɢᴇ ◈", callback_data="mplus HELP_Image")],    
    [InlineKeyboardButton("◈ ᴛɢᴍ ◈", callback_data="mplus HELP_TG"),
    InlineKeyboardButton("◈ ɢᴀᴍᴇs ◈", callback_data="mplus HELP_Game"),
    InlineKeyboardButton("◈ ғᴏɴᴛ ◈", callback_data="mplus HELP_Font")],
    [InlineKeyboardButton("◈ ᴛʀᴜᴛʜ-ᴅᴀʀᴇ ◈", callback_data="mplus HELP_TD"),
    InlineKeyboardButton("◈ ʜᴀsᴛᴀɢ ◈", callback_data="mplus HELP_HT"),
    InlineKeyboardButton("◈ ɪᴍᴘᴏsᴛᴇʀ ◈", callback_data="mplus HELP_Imposter")], 
    [InlineKeyboardButton("◈ ǫᴜᴏᴛʟʏ ◈", callback_data="mplus HELP_Q"),
    InlineKeyboardButton("◈ ғᴜɴ ◈", callback_data="mplus HELP_Fun"),
    InlineKeyboardButton("◈ ᴛᴛs ◈", callback_data="mplus HELP_TTS")],          
    [InlineKeyboardButton("", callback_data=f"managebot123 settings_back_helper"), 
    InlineKeyboardButton("< ʀᴇᴛᴜʀɴ ", callback_data=f"settings_back_helper")]
]
