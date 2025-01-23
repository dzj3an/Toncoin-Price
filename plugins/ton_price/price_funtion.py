from pyromod import Client 
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup, CallbackQuery
import asyncio

from utils import search_process, process
from configs import CHANNEL_TON, TON_TOKEN
from pytonapi import AsyncTonapi

@Client.on_callback_query(filters.regex("price_ton_on_off"))
async def price_ton_on_off(app: Client, callback_query: CallbackQuery):

    message_id = callback_query.message.id
    chat_id = callback_query.message.chat.id

    ton = await search_process("ton_price")
    if ton is True:
        process_id_to_delete = "ton_price"
        if process_id_to_delete in process:
            process[process_id_to_delete].cancel()
            del process[process_id_to_delete]
            text = "Ton Price = Off ❌"

        else:
            print("The process was not found.")
    else:
        process_id = "ton_price"
        process[process_id] = asyncio.create_task(ton_price(app))
        text = "Ton Price = On ✅"
        
    keyboard = [
        [InlineKeyboardButton("Menu", callback_data=f"admin_menu")],
    ]
    buttons = InlineKeyboardMarkup(keyboard)
    await app.edit_message_text(chat_id,message_id,f"{text}",reply_markup=buttons)


async def ton_price(app: Client):
    while True:
        try:
            tonapi = AsyncTonapi(api_key=TON_TOKEN)
            price = await tonapi.rates.get_prices(tokens=["TON"], currencies=["USD"])
            price = price.rates

            # Current price
            current_price = price['TON']['prices']['USD']  
            # 24 hour difference
            price_ton_24 = price['TON']['diff_24h']['USD']  
            
            text = f"""
**Toncoin | ${current_price:.4f} USD**
<blockquote>{price_ton_24} | 24 hours</blockquote>
"""
            await app.send_message(chat_id=CHANNEL_TON, text=text)
        except Exception as e:
            print(f"Error al obtener o procesar los datos: {e}")
        
        # Wait 1 minute for the next interaction
        await asyncio.sleep(60)