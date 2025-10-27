from bot import Bot
from pyrogram.types import Message, InputMediaPhoto, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import filters
from config import BOT_STATS_TEXT, USER_REPLY_TEXT, STICKER_ID, COMMAND_PHOTO
from datetime import datetime
from helper_func import *
import asyncio

async def check_admin(_, client, message: Message):
    if not message.from_user:
        return False
    user_id = message.from_user.id
    chat_id = message.chat.id
    chat_member = await client.get_chat_member(chat_id, user_id)
    return chat_member.status in ["administrator", "OWNER"]

admin = filters.create(check_admin)

is_owner_or_admin = admin

@Bot.on_message(filters.command('stats') & admin)
async def stats(bot: Bot, message: Message):
    await bot.send_sticker(message.chat.id, STICKER_ID)
    await asyncio.sleep(0.5)
    
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    caption = f"<i><b><blockquote expandable>{BOT_STATS_TEXT.format(uptime=time)}\n\n📜 <b>ʜᴏᴡ ɪᴛ ᴡᴏʀᴋs</b>: ᴅɪsᴘʟᴀʏs ᴛʜᴇ ʙᴏᴛ’s ᴜᴘᴛɪᴍᴇ. ᴏɴʟʏ ᴛʜᴇ ᴏᴡɴᴇʀ ᴄᴀɴ ᴜsᴇ ᴛʜɪs.</blockquote></b></i>"
    buttons = [
        [InlineKeyboardButton("• ʀᴇғʀᴇsʜ •", callback_data="refresh_stats")]
    ]
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=COMMAND_PHOTO,
        caption=caption,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Bot.on_callback_query(filters.regex(r"refresh_stats"))
async def refresh_stats_callback(client, callback_query):
    now = datetime.now()
    delta = now - client.uptime
    time = get_readable_time(delta.seconds)
    caption = f"<i><b><blockquote expandable>{BOT_STATS_TEXT.format(uptime=time)}\n\n📜 <b>ʜᴏᴡ ɪᴛ ᴡᴏʀᴋs</b>: ᴅɪsᴘʟᴀʏs ᴛʜᴇ ʙᴏᴛ’s ᴜᴘᴛɪᴍᴇ. ᴏɴʟʏ ᴛʜᴇ ᴏᴡɴᴇʀ ᴄᴀɴ ᴜsᴇ ᴛʜɪs.</blockquote></b></i>"
    await client.send_sticker(callback_query.message.chat.id, STICKER_ID)
    await asyncio.sleep(0.5)
    await callback_query.message.edit_media(
        media=InputMediaPhoto(
            media=COMMAND_PHOTO,
            caption=caption
        ),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("• ʀᴇғʀᴇsʜ •", callback_data="refresh_stats")]])
    )
