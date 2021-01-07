from telethon import TelegramClient

from config.config_local import Config

# Remember to use your own values from my.telegram.org!
client = TelegramClient(Config.SESSION_NAME, Config.API_ID, Config.API_HASH)


async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    print(me.phone)
    # You can print all the dialogs/conversations that you are part of:
    async for dialog in client.iter_dialogs():
        print(dialog.name)
        file = open("dialogs/" + dialog.name + ".txt", "w")
        async for message in client.iter_messages(dialog.name, reverse=False):
            if message.sender_id == me.id:
                author = "me"
            else:
                author = dialog.name
            text = str(author) + ":\t" + message.text + "\n"
            file.write(text)
            if message.photo:
                path = await message.download_media("media")
                print('File saved to', path)
        file.close()


with client:
    client.loop.run_until_complete(main())
