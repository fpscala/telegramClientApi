import argparse
import time
from datetime import datetime

import pytz
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

from config.config_local import Config
from utils.util import getStringFromArray, array, countdown, convert_time_to_string


def valid_tz(s):
    try:
        return pytz.timezone(s)
    except:
        msg = "Not a valid tz: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


parser = argparse.ArgumentParser()
parser.add_argument("--api_id", required=False, help="user api ID", type=str, default=Config.API_ID)
parser.add_argument("--api_hash", required=False, help="user api Hash", type=str, default=Config.API_HASH)
parser.add_argument("--tz", required=False, help="user api Hash", type=valid_tz, default=valid_tz('Asia/Tashkent'))

args = parser.parse_args()

client = TelegramClient("carpediem", args.api_id, args.api_hash)
client.flood_sleep_threshold = 0  # Don't auto-sleep

async def setBio():
    index = 0
    while True:
        size = len(array)
        print(index)
        bts = str(countdown(datetime.now(args.tz).replace(microsecond=0, tzinfo=None)))
        if index == size:
            bio = 'Yangi yil ' + bts + ' dan keyin kirib keladi!'
            index = 0
        else:
            bio = str(getStringFromArray(index))
        print(bio)
        index += 1
        await client(UpdateProfileRequest(about='Yangi yil ' + bts + ' dan keyin kirib keladi!'))
        time.sleep(1)


if __name__ == '__main__':
    client.start()
    import asyncio

    asyncio.get_event_loop().run_until_complete(setBio())
