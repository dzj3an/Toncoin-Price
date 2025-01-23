from pyromod import Client 
from pyrogram import filters
from pyrogram.types import  CallbackQuery
import asyncio, os

@Client.on_callback_query(filters.regex("off-bot"))
async def off_bot(app: Client, callback_query: CallbackQuery):

    message_id = callback_query.message.id
    chat_id = callback_query.message.chat.id

    await app.delete_messages(chat_id, message_ids=message_id)
    msg = await app.send_message(chat_id,f"Turning off in... 5...")
    await asyncio.sleep(1)
    await app.edit_message_text(chat_id,msg.id,f"Turning off in... 4...")
    await asyncio.sleep(1)
    await app.edit_message_text(chat_id,msg.id,f"Turning off in... 3...")
    await asyncio.sleep(1)
    await app.edit_message_text(chat_id,msg.id,f"Turning off in... 2...")
    await asyncio.sleep(1)
    await app.edit_message_text(chat_id,msg.id,f"Turning off in... 1..")
    await asyncio.sleep(1)
    await app.edit_message_text(chat_id,msg.id,f"OFF")
    
    try:
        os._exit(0)
    except:
        await app.edit_message_text(chat_id,msg.id,f"ERROR: {str(Exception)}")