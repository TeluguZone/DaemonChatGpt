from pyrogram import Client, filters
from config import LOG_CHANNEL
from plugins.database import db
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)


LOG_TEXT = """<b>#NewUser
    
ID - <code>{}</code>

Nᴀᴍᴇ - {}</b>
"""

@Client.on_message(filters.command('start'))
async def start_message(c,m):
    await db.is_user_exist(m.from_user.id)
    await db.add_user(m.from_user.id, m.from_user.first_name)
    await c.send_message(LOG_CHANNEL, LOG_TEXT.format(m.from_user.id, m.from_user.mention))
    await m.reply_photo("https://graph.org/file/36d04bdf89222362a779e.jpg",
        caption="**ʜɪ** 👋\n\n**ɪ ᴀᴍ ᴀ ᴄʜᴀᴛɢᴘᴛ ʙᴏᴛ**\n\n⭕ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ :-** **[TeluguZone™](https://t.me/Teluguzone0)**",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('⚡,BACKUP CHANNEL', url='https://t.me/TeluguZoneofc')
                    ],  
                    [
                        InlineKeyboardButton("MY Father 🧎‍♂️", url='https://t.me/daemon990'),
                        InlineKeyboardButton("🤖 ᴜᴘᴅᴀᴛᴇ", url='https://t.me/teluguzone0')
                    ]
                ]
            )
        )
  
