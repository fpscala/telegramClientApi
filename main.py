import time
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.handlers import MessageHandler
from config_local import Config

app = Client(Config.SESSION_NAME, api_id=Config.API_ID, api_hash=Config.API_HASH)
client = "PrinceMRD"

try:

    async def forward_msg(_, message):
        await message.forward("me")


    @app.on_message(filters.text & filters.private)
    def echo(_, message):
        message.reply_text(message.text)


    async def getChatHistory(account):
        with app:
            for message in app.iter_history(account, reverse=True):
                print(message.text)


    my_handler = MessageHandler(echo)
    app.add_handler(my_handler)
    app.run()
except FloodWait as e:
    time.sleep(e.x)  # Wait "x" seconds before continuing
