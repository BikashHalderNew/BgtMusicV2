

from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from BgtxD.config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from BgtxD.power import get_command
from BgtxD import app
from BgtxD.centre.call import BIKASH
from BgtxD.utility import bot_sys_stats
from BgtxD.utility.decorators.language import language

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(
    filters.command(PING_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"],
    )
    start = datetime.now()
    pytgping = await BIKASH.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            MUSIC_BOT_NAME, resp, UP, DISK, CPU, RAM, pytgping
        )
    )
