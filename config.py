import re
import os
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 21374618
API_HASH = "e3c08a17fd1a974590cca32d38c03aab"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7188036509:AAHn9MIo6fkIHfqx1swhS6-BfSQmJRPdMEQ"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://Bhumi:Bhumi99@cluster0.ue8p4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MUSIC_BOT_NAME = "˹ʙʜᴜᴍι ᴍᴜsιƈ˼"
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 90))

# Chat id of a group for logging bot's activities
LOGGER_ID = -1002244957657
LOG_GROUP_ID = "-1002244957657"

# Get this value from @BRANDRD_ROBOT on Telegram by /id
OWNER_ID = 1321591503

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/WCGKING/BrandrdXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TIGERBHUMISINGH")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+DzLMBmzrr0g5M2Vl")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = "BQFGJpoAGBEiJMRFoQl2Hgp_Ix9N2KiGfAqchPKItuKzaleOeD9KqmKG64L9lOuUNZhCsZso2XHFv1P6fCWSSO4m8rPZa_vp0xUmKPqHGW88JP4N6hRcNXZLOld8bXDvP_VuL0PElqcPV2fWeily1OusNdC6Wj2_xsnRdu7YMXcCQurG32ypQ36LtcqbJvoG0lTmK0DHu94EF3qxNUZRINR423yH0a4T_SPXyxNO77rCNsRA2u2uPP8Z7bkoUY5tLDfPOErhFMqfjNlniTiausaw6bfIMREu4MWLPbMtyb7OGKMhJE1d-cf4dwXEvapBtb1fCVMN7PpzXkrxsRiOX7OH2RUXMAAAAAGxBRIMAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/f2a2bfb6c39b29a8e4ecc.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/f2a2bfb6c39b29a8e4ecc.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/f2a2bfb6c39b29a8e4ecc.jpg"
STATS_IMG_URL = "https://graph.org/file/f2a2bfb6c39b29a8e4ecc.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/f2a2bfb6c39b29a8e4ecc.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/f2a2bfb6c39b29a8e4ecc.jpg"
STREAM_IMG_URL = "https://graph.org/file/f2a2bfb6c39b29a8e4ecc.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/f2a2bfb6c39b29a8e4ecc.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/f2a2bfb6c39b29a8e4ecc.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/f2a2bfb6c39b29a8e4ecc.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/f2a2bfb6c39b29a8e4ecc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/f2a2bfb6c39b29a8e4ecc.jpg"
