import asyncio
from telethon import TelegramClient, events

api_id = 35209658
api_hash = 'c795e2be9ef3057488fc6f21105a5f29'

client = TelegramClient('telegram_session', api_id, api_hash)

@client.on(events.NewMessage(chats='ffddnju'))
async def handler(event):
    try:
        text = event.message.text or ""
        text = text.replace("@ffddnju", "@abrehamazbitew")
        
        if event.message.media:
            await client.send_file('abrehamazbitew', event.message.media, caption=text)
        elif text:
            await client.send_message('abrehamazbitew', text)
    except Exception as e:
        print(f"Error forwarding message: {e}")

async def main():
    print("Bot is running on Render 24/7...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())

import asyncio
from telethon import TelegramClient

api_id = 35209658
api_hash = 'c795e2be9ef3057488fc6f21105a5f29'

client = TelegramClient('telegram_session', api_id, api_hash)

async def main():
    await client.start()
    print("Session created successfully!")

with client:
    client.loop.run_until_complete(main())

nano forwarder.py
import asyncio
from telethon import TelegramClient, events

api_id = 35209658
api_hash = 'c795e2be9ef3057488fc6f21105a5f29'

client = TelegramClient('telegram_session', api_id, api_hash)

@client.on(events.NewMessage(chats='ffddnju'))
async def handler(event):
    try:
        text = event.message.text or ""
        text = text.replace("@ffddnju", "@abrehamazbitew")
        
        if event.message.media:
            await client.send_file('abrehamazbitew', event.message.media, caption=text)
        elif text:
            await client.send_message('abrehamazbitew', text)
    except Exception as e:
        print(f"Error forwarding message: {e}")

async def main():
    print("Bot is running on Render 24/7...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())

