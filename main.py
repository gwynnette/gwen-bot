
import discord
import dotenv
import os
import sys; sys.dont_write_bytecode = True
from discord.ext import commands
from dotenv import load_dotenv

class RonhorBot:

    def bootup():

        bot_config = load_dotenv('config/preferences.env')
        bot_prefixes = os.getenv('bot_prefixes')
        RonhorBot = commands.Bot(command_prefix = bot_prefixes)

        cached_key = os.getenv('cached_key')
        active_key = os.getenv('active_key')

        if active_key != cached_key:
            print("Boot sequence failed. Error code: HARLEYLEO")
        else:
            RonhorBot.run(active_key)

    try:
        bootup()
        print("Boot sequence successful. Bot will be online in a few moments.")
    except Exception as error:
        print(error)