import argparse
import time
from datetime import datetime

import pytz
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

from config.config_local import Config


def valid_tz(s):
    try:
        return pytz.timezone(s)
    except:
        msg = "Not a valid tz: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)


def convert_time_to_string(dt):
    return f"{dt.hour}:{dt.minute:02}"


parser = argparse.ArgumentParser()
parser.add_argument("--api_id", required=False, help="user api ID", type=str, default=Config.API_ID)
parser.add_argument("--api_hash", required=False, help="user api Hash", type=str, default=Config.API_HASH)
parser.add_argument("--tz", required=False, help="user api Hash", type=valid_tz, default=valid_tz('Asia/Tashkent'))

args = parser.parse_args()

client = TelegramClient("carpediem", args.api_id, args.api_hash)


async def setBio():
    while True:
        bts = convert_time_to_string(datetime.now(args.tz).replace(tzinfo=None))
        await client(UpdateProfileRequest(about='This is a test from Telethon :' + bts))
        time.sleep(30)


if __name__ == '__main__':
    client.start()
    import asyncio

    asyncio.get_event_loop().run_until_complete(setBio())
