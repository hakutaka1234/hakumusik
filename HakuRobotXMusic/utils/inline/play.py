from pyrogram.types import InlineKeyboardButton
import config


## After Edits with Timer Bar

def time_to_sec(time: str):
    x = time.split(":")

    if len(x) == 2:
        min = int(x[0])
        sec = int(x[1])

        total_sec = (min*60) + sec
    elif len(x) == 3:
        hour = int(x[0])
        min = int(x[1])
        sec = int(x[2])

        total_sec = (hour*60*60) + (min*60) + sec

    return total_sec

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_sec(played)
    total_sec = time_to_sec(dur)

    x, y = str(round(played_sec/total_sec,1)).split(".")
    pos = int(y)

    line = "—"
    circle = "◉"

    bar = line*(pos-1)
    bar += circle
    bar += line*(10-len(bar))

    buttons = [
        [
            InlineKeyboardButton(
                callback_data="close",
            )
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_sec(played)
    total_sec = time_to_sec(dur)

    x, y = str(round(played_sec/total_sec,1)).split(".")
    pos = int(y)

    line = "—"
    circle = "◉"

    bar = line*(pos-1)
    bar += circle
    bar += line*(10-len(bar))
    
    buttons = [
            [
            InlineKeyboardButton(
                callback_data="close",
            )
        ],
    ]
    return buttons


## Inline without Timer Bar


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                callback_data="close",
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                callback_data="close",
            )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                callback_data="close",
            )
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
                [
            InlineKeyboardButton(
                callback_data="close",
            )
        ],
    ]
    return buttons


## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                callback_data="close",
            )
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                callback_data="close",
            )
        ],
    ]
    return buttons


## Cpanel Markup


def panel_markup_1(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                callback_data="close",
            )
        ],
    ]
    return buttons
