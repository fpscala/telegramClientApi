import os
import time

from telethon import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest

from config.config_local import Config
from utils.util import getStringFromArray, array

# Remember to use your own values from my.telegram.org!
client = TelegramClient(Config.SESSION_NAME, Config.API_ID, Config.API_HASH)


async def main():
    index = 0
    while True:
        getPhotoList()
        print(array)
        size = len(array)
        if index == size:
            index = 0
        filePath = 'avatars/' + str(getStringFromArray(index))
        index += 1
        photos = await client.get_profile_photos('me')
        await client(DeletePhotosRequest(photos))
        await client(UploadProfilePhotoRequest(
            await client.upload_file(filePath)
        ))
        time.sleep(180)


def getPhotoList():
    array.clear()
    for file in os.listdir('avatars/'):
        if file.endswith('.jpg') or file.endswith('.png'):
            array.append(file)


if __name__ == '__main__':
    import asyncio

    client.start()
    asyncio.get_event_loop().run_until_complete(main())
