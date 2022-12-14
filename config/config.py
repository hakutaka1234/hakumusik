import re

import sys

from os import getenv

from dotenv import load_dotenv

from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "17278438"))

API_HASH = getenv("API_HASH", "7886b64c08117902bf1aaff07280b512")

BOT_TOKEN = getenv("BOT_TOKEN", "5622516770:AAFZ3jZV0WU1fFY5GpNF1ba2GPg_4VTpDN8")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://diaapitubot:eNeRA310798@rachmadalfio.qwqyflg.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT_MIN = int(

    getenv("DURATION_LIMIT", "300")

)

SONG_DOWNLOAD_DURATION = int(

    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180")

)

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001686544997"))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "RoychoManageBot")

OWNER_ID = list(

    map(int, getenv("OWNER_ID", "1954780613").split())

)

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(

    "UPSTREAM_REPO",

    "https://github.com/hakutaka1234/hakumusik",

)

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", "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")

SUPPORT_CHANNEL = getenv(

    "SUPPORT_CHANNEL", "https://t.me/hakucmd_userbot")

SUPPORT_GROUP = getenv(

    "SUPPORT_GROUP", "https://t.me/evzesda")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")

AUTO_LEAVE_ASSISTANT_TIME = int(

    getenv("ASSISTANT_LEAVE_TIME", "5400")

)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", "True")

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "6"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://telegra.ph/file/f84d28d91512a445ecce1.mp4")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "a9aa01845c0c4418b65f58e17a495b5c")

SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "da894e2055e14ee0b6743c044d0655cb")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(

    getenv("CLEANMODE_MINS", "7")

)

TG_AUDIO_FILESIZE_LIMIT = int(

    getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600")

)

TG_VIDEO_FILESIZE_LIMIT = int(

    getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824")

)

# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION1", "QA1wLJ1V6kPGxsaCoptdIeLUvCbQQUWb2PiLe7yi_cLN8hCJWMgqBSp1H4CJvvME70z7kgEQ-YUuKHiUVKef_BgMGhqEtfAee4I6oo4zYeW6KwlLPcixBbQie39Vn4B7_Zb331hyzx8rFQ3cUHPAXiikkazLpg9a5uKsP5Azrl9EBskIdLfgC8a4L21PrsZaGRhD8tpY5cIAIqkaDS_hYT1y_zIxc8KuxotgCmw7Y9mf8_IgQpTYDZMjK4KfoPLu3jlRxhRu_58r2wYzNEj_1thFc4MuoZn74w4XjQoJFnWaOu0SmD0L-naQ8psf1lD0EsS9wh1-nxMeJWRJogkrEu6AAAAAF-6qA4A")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()

YTDOWNLOADER = 1

LOG = 2

LOG_FILE_NAME = "anonxlogs.txt"

adminlist = {}

lyrical = {}

chatstats = {}

userstats = {}

clean = {}

autoclean = []

START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/96b621f97915c335d53b3.jpg")

PLAYLIST_IMG_URL = getenv(

    "PLAYLIST_IMG_URL",

    "assets/Playlist.jpeg",

)

GLOBAL_IMG_URL = getenv(

    "GLOBAL_IMG_URL",

    "assets/Global.jpeg",

)

STATS_IMG_URL = getenv(

    "STATS_IMG_URL",

    "assets/Stats.jpeg",

)

TELEGRAM_AUDIO_URL = getenv(

    "TELEGRAM_AUDIO_URL",

    "assets/Audio.jpeg",

)

TELEGRAM_VIDEO_URL = getenv(

    "TELEGRAM_VIDEO_URL",

    "assets/Video.jpeg",

)

STREAM_IMG_URL = getenv(

    "STREAM_IMG_URL",

    "assets/Stream.jpeg",

)

SOUNCLOUD_IMG_URL = getenv(

    "SOUNCLOUD_IMG_URL",

    "assets/Soundcloud.jpeg",

)

YOUTUBE_IMG_URL = getenv(

    "YOUTUBE_IMG_URL",

    "assets/Youtube.jpeg",

)

SPOTIFY_ARTIST_IMG_URL = getenv(

    "SPOTIFY_ARTIST_IMG_URL",

    "assets/SpotifyArtist.jpeg",

)

SPOTIFY_ALBUM_IMG_URL = getenv(

    "SPOTIFY_ALBUM_IMG_URL",

    "assets/SpotifyAlbum.jpeg",

)

SPOTIFY_PLAYLIST_IMG_URL = getenv(

    "SPOTIFY_PLAYLIST_IMG_URL",

    "assets/SpotifyPlaylist.jpeg",

)

def time_to_seconds(time):

    stringt = str(time)

    return sum(

        int(x) * 60**i

        for i, x in enumerate(reversed(stringt.split(":")))

    )

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

SONG_DOWNLOAD_DURATION_LIMIT = int(

    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")

)

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

if UPSTREAM_REPO:

    if not re.match("(?:http|https)://", UPSTREAM_REPO):

        print(

            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"

        )

        sys.exit()

if PLAYLIST_IMG_URL:

    if PLAYLIST_IMG_URL != "assets/Playlist.jpeg":

        if not re.match("(?:http|https)://", PLAYLIST_IMG_URL):

            print(

                "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"

            )

            sys.exit()

if GLOBAL_IMG_URL:

    if GLOBAL_IMG_URL != "assets/Global.jpeg":

        if not re.match("(?:http|https)://", GLOBAL_IMG_URL):

            print(

                "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"

            )

            sys.exit()

if STATS_IMG_URL:

    if STATS_IMG_URL != "assets/Stats.jpeg":

        if not re.match("(?:http|https)://", STATS_IMG_URL):

            print(

                "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"

            )

            sys.exit()

if TELEGRAM_AUDIO_URL:

    if TELEGRAM_AUDIO_URL != "assets/Audio.jpeg":

        if not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL):

            print(

                "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"

            )

            sys.exit()

if STREAM_IMG_URL:

    if STREAM_IMG_URL != "assets/Stream.jpeg":

        if not re.match("(?:http|https)://", STREAM_IMG_URL):

            print(

                "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"

            )

            sys.exit()

if SOUNCLOUD_IMG_URL:

    if SOUNCLOUD_IMG_URL != "assets/Soundcloud.jpeg":

        if not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL):

            print(

                "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"

            )

            sys.exit()

if YOUTUBE_IMG_URL:

    if YOUTUBE_IMG_URL != "assets/Youtube.jpeg":

        if not re.match("(?:http|https)://", YOUTUBE_IMG_URL):

            print(

                "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"

            )

            sys.exit()

if TELEGRAM_VIDEO_URL:

    if TELEGRAM_VIDEO_URL != "assets/Video.jpeg":

        if not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL):

            print(

                "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"

            )

            sys.exit()
