import asyncio
import importlib
from sys import argv
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from BrandrdXMusic import LOGGER, app, userbot
from BrandrdXMusic.core.call import Hotty
from BrandrdXMusic.misc import sudo
from BrandrdXMusic.plugins import ALL_MODULES
from BrandrdXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

from BrandrdXMusic.plugins.tools.clone import restart_bots

STRING1="BQEyh-EAgr-25XRaPfkGwX-ksMioRBgn8142hMC91MIevQouUEWOhGSQNrgHAw5U2CcnWeGduN6dSlKV9rGrlhdBSie7PPFhmD7XHEi4NpgujqBEQepfi5HRgthx1JDBglNrrvTKAuQg4YTGDOWksgsJA_CqRZgPl8kNmRkZwbZM8LljLZ0UlDjjcm9_6gKiaRd-z0mWyp6XSt_RVF_FV1n2Ya3MCxDjO2GbhZRhp8-a6wpUyp8flVedIiBKabWfrwriTaVAXW8Bg5RS1iPLzFxvkLpVC94uO8jbZh0mZffdtS5UZ6_HS6WRTRj-SNt7_L4jjGgGz7wTCOzpnuZEE39SvPNdRgAAAAHRFShNAA"


async def init():
    # if (
    #     not STRING1
    #     and not config.STRING2
    #     and not config.STRING3
    #     and not config.STRING4
    #     and not config.STRING5
    # ):
    #     LOGGER(__name__).error("Assistant client variables not defined, exiting...")
    #     exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("BrandrdXMusic.plugins" + all_module)
    LOGGER("BrandrdXMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Hotty.start()
    try:
        await Hotty.stream_call("https://graph.org/file/e999c40cb700e7c684b75.mp4")
    except NoActiveGroupCall:
        LOGGER("BrandrdXMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Hotty.decorators()
    LOGGER("BrandrdXMusic").info(
        "ᴅʀᴏᴘ ʏᴏᴜʀ ɢɪʀʟꜰʀɪᴇɴᴅ'ꜱ ɴᴜᴍʙᴇʀ ᴀᴛ @learningbots79 ᴊᴏɪɴ @LB_Music_Bot , @learning_bots ꜰᴏʀ ᴀɴʏ ɪꜱꜱᴜᴇꜱ"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("BrandrdXMusic").info("Stopping Brandrd Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
