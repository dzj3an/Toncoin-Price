from pyromod import Client 
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup, CallbackQuery

from configs import OWNERS_ID
from utils import search_process

@Client.on_callback_query(filters.regex("admin_menu"))
async def menu_callback(app: Client, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    message_id = callback_query.message.id
    chat_id = callback_query.message.chat.id

    if user_id not in OWNERS_ID:return

    tonprice = await search_process("ton_price")
    if tonprice is True:
        ton = "Ton Price ✅"
    else:
        ton = "Ton Price ❌"

    keyboard = [
        [InlineKeyboardButton(f"{ton}", callback_data=f"price_ton_on_off"),
        InlineKeyboardButton(f"Turn off Bot", callback_data=f"turn_off_bot")],
    ]
    buttons = InlineKeyboardMarkup(keyboard)
    await app.edit_message_text(chat_id,message_id,"Menu:",reply_markup=buttons)