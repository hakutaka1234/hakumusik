from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, MUSIC_BOT_NAME
from strings import get_command
from HakuRobotXMusic import app
from HakuRobotXMusic.core.call import Haku
from HakuRobotXMusic.utils import bot_sys_stats
from HakuRobotXMusic.utils.decorators.language import language

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(
    filters.command(PING_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    pytgping = await Haku.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        )
    )
