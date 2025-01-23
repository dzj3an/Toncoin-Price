from pyromod import Client
import asyncio
from logging import basicConfig, INFO
basicConfig(format="*%(levelname)s %(message)s", level=INFO, force=True)

from configs import BOT_TOKEN, API_HASH, API_ID, OWNERS_ID

plugins = dict(root="plugins")
app = Client('ton_price',api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=plugins)

async def main():
    await app.start()
    for owner in OWNERS_ID:
        await app.send_message(owner, '**[LOGS]:** Bot | ONLINE ✅.')

loop: asyncio.AbstractEventLoop = asyncio.get_event_loop_policy().get_event_loop()
loop.create_task(main())
loop.run_forever()