from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from HakuRobotXMusic import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="",
                
            )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="",

           )
        ],
     ]
    return buttons
