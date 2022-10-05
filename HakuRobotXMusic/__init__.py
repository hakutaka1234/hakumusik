from HakuRobotXMusic.core.bot import HakuRobotXMusicBot
from HakuRobotXMusic.core.dir import dirr
from HakuRobotXMusic.core.git import git
from HakuRobotXMusic.core.userbot import Userbot
from HakuRobotXMusic.misc import dbb, heroku, sudo
from aiohttp import ClientSession

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = HakuRobotXMusicBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
