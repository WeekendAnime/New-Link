from ast import pattern
import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7520539725:AAFyWVPB5H0VbVggbvAjjn2NgCl_eJ68RQc")
BOT_USERNAME = 'LinkkShare_bot'
APP_ID = int(os.environ.get("APP_ID", "28744454"))
API_HASH = os.environ.get("API_HASH", "debd37cef0ad1a1ce45d0be8e8c3c5e7")
OWNER_ID = int(os.environ.get("OWNER_ID", "6266529037"))
PORT = os.environ.get("PORT", "8080")
DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))
STICKER_ID = os.environ.get("STICKER_ID", "CAACAgUAAxkBAAEPQLRorzC7PcWDMNuR6UkaxaKLxtsY-gACERUAApg9qVU2Cwv5mdxKhDYE")  # Replace with your sticker ID
COMMAND_PHOTO = os.environ.get("COMMAND_PHOTO", "https://ibb.co/mVkSySr7")  # Replace with your photo URL
START_PIC = os.environ.get("START_PIC", "https://ibb.co/mVkSySr7")
START_MSG = os.environ.get("START_MESSAGE", "Hᴇʟʟᴏ {mention} ~\n\n <i><b><blockquote>Iᴀᴍ ᴀ ᴀᴅᴠᴀɴᴄᴇ ʟɪɴᴋ sʜᴀʀᴇ ʙᴏᴛ ᴛʜʀᴏᴜɢʜ ᴡʜɪᴄʜ ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ ᴛʜᴇ ʟɪɴᴋs ᴏғ sᴘᴇᴄɪғɪᴄ ᴄʜᴀɴɴᴇʟs ᴡʜɪᴄʜ sᴀᴠᴇ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟs ғʀᴏᴍ ᴄᴏᴘʏʀɪɡʜᴛ.</blockquote></b></i>")
ABOUT_TXT = os.environ.get("HELP_MESSAGE", "<i><b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/RexBots_Official>RexBots</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/RexBots_Official>RexBOTS</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href='https://t.me/about_zani/117'>ZANI</a>\n◈ ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>ᴍᴏɴɢᴏ ᴅʙ</a>\n» ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href='https://t.me/about_zani/117'>ZANI</a></blockquote></b></i>")
HELP_TXT =  os.environ.get("HELP_MESSAGE", "⁉️ Hᴇʟʟᴏ {mention} ~\n\n <b><blockquote expandable>➪ I ᴀᴍ ᴀ ᴘʀɪᴠᴀᴛᴇ ʟɪɴᴋ sʜᴀʀɪɴɢ ʙᴏᴛ, ᴍᴇᴀɴᴛ ᴛᴏ ᴘʀᴏᴠɪᴅᴇ ʟɪɴᴋ ғᴏʀ sᴘᴇᴄɪғɪᴄ ᴄʜᴀɴɴᴇʟs.\n\n ➪ Iɴ ᴏʀᴅᴇʀ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʟɪɴᴋs ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ ᴀʟʟ ᴍᴇɴᴛɪᴏɴᴇᴅ ᴄʜᴀɴɴᴇʟ ᴛʜᴀᴛ ɪ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴛᴏ ᴊᴏɪɴ. Yᴏᴜ ᴄᴀɴ ɴᴏᴛ ᴀᴄᴄᴇss ᴏʀ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇs ᴜɴʟᴇss ʏᴏᴜ ᴊᴏɪɴᴇᴅ ᴀʟʟ ᴄʜᴀɴɴᴇʟs.\n\n ‣ /help - Oᴘᴇɴ ᴛʜɪs ʜᴇʟᴘ ᴍᴇssᴀɢᴇ !</blockquote></b>")
BOT_STATS_TEXT = "<i><b><blockquote>ʙᴏᴛ ᴜᴘᴛɪᴍᴇ\n{uptime}</blockquote></b></i>"
USER_REPLY_TEXT = "<i><b><blockquote>⚠️ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ.</blockquote></b></i>"
LOG_FILE_NAME = "links-sharingbot.txt"
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1002257657458"))

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
