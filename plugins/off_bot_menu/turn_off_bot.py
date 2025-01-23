from pyromod import Client 
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup, CallbackQuery

@Client.on_callback_query(filters.regex("turn_off_bot"))
async def turn_off_bot(app: Client, callback_query: CallbackQuery):

    message_id = callback_query.message.id
    chat_id = callback_query.message.chat.id

    keyboard = [
        [InlineKeyboardButton("OFF", callback_data=f"off-bot")],
        [InlineKeyboardButton("Menu", callback_data=f"admin_menu")],
    ]
    
    text = f"""    
Do you want to turn off the Bot?
"""
    buttons = InlineKeyboardMarkup(keyboard)
    await app.edit_message_text(chat_id,message_id,f"{text}",reply_markup=buttons)