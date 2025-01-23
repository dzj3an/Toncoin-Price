from pyromod import Client, Message 
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup

from configs import OWNERS_ID
from utils import search_process

@Client.on_message(filters.command("menu"))
async def menu_command(app: Client, msg: Message):
    user_id = msg.from_user.id

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
    await msg.reply_text("Menu:", reply_markup=buttons)