import asyncio
from telethon import TelegramClient, events

api_id = 35209658
api_hash = 'c795e2be9ef3057488fc6f21105a5f29'

client = TelegramClient('telegram_session', api_id, api_hash)

@client.on(events.NewMessage(chats='ffddnju'))
async def handler(event):
    text = event.raw_text or ''
    # ጽሑፍ እና ሊንኮች መቀየሪያ
    text = text.replace('@ffddnju', '@abrehamazbitew')
    text = text.replace('https://t.me/ffddnju', 'https://t.me/abrehamazbitew')
    
    try:
        if event.media:
            await client.send_file('abrehamazbitew', event.media, caption=text)
        elif text:
            await client.send_message('abrehamazbitew', text)
    except Exception as e:
        print(f"Error: {e}")

async def main():
    await client.start()
    print("Forwarder Started Successfully!")
    await client.run_until_disconnected()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

