
# dependencies
import discord
import dotenv
import os
import sys; sys.dont_write_bytecode = True
import traceback
from discord.ext import commands
from dotenv import load_dotenv

# global variables
bot_secrets = load_dotenv('./config/secrets.env')
bot_prefixes = ['.r ', '!r ']
RonhorBot = commands.Bot(command_prefix = bot_prefixes)

# terminal notifications
@RonhorBot.event
async def on_ready():
    print("Bot is now online.")

class __init__:
    
    # verify bot's secrets
    def verification():

        print("Verifiying bot credentials. This will only take a moment.")
        cached_key = os.getenv('cached_key')
        active_key = os.getenv('active_key')
        
        if active_key == cached_key:
            print("Credentials verified. Bot will be online shortly.") # if results are true: bot will log in to discord
            RonhorBot.run(active_key)
            
        elif active_key != cached_key:
            print("Credentials not verified. Error code: HARLEYLEO") # if results are false: terminal throws exception

    try:
        verification()

    except Exception as error:
        traceback.print_exc()
        
