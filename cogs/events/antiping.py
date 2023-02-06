import os
import discord
from discord.ext import commands
import requests
import sys
from utils.Tools import getConfig, add_user_to_blacklist, getanti
import setuptools
from itertools import cycle
from collections import Counter
import threading
import datetime
import logging
from core import Sputnik, Cog
import time
import asyncio
import aiohttp
import tasksio
from discord.ui import View, Button
import json
from discord.ext import tasks
import random

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

class antipinginv(Cog):
    def __init__(self, client: Sputnik):
        self.client = client
        self.spam_control = commands.CooldownMapping.from_cooldown(10, 12.0, commands.BucketType.user)
       # print("Cog Loaded: Antipinginv")

    @commands.Cog.listener()
    async def on_message(self, message):
      button = Button(label="Invite", url =  "https://discord.gg/3YmDAzbuRR")
      button1 = Button(label="Support", url = "https://discord.gg/3YmDAzbuRR")
      try:
       
        with open("blacklist.json", "r") as f:
          data2 = json.load(f)
          Sputnik = '<@1034453939933937734>'
          try:
            data = getConfig(message.guild.id)
            anti = getantiping(message.guild.id)
            prefix = data["prefix"]
            wled = data["whitelisted"]
            wl = data["pingswl"]
            punish = data["apingpunish"]
          except Exception:
            pass
          guild = message.guild
          if message.mention_everyone:
            if str(message.author.id) in wled or wl or anti == "off":
              pass
            else:
              if punish == "ban":
                await message.guild.ban(message.author, reason="Mentioning Everyone | Not Whitelisted")
              elif punish == "kick":
                await message.guild.kick(message.author, reason="Mentioning Everyone | Not Whitelisted")
              elif punish == "none":
                return


          elif message.content == Sputnik or message.content == "<@!1034453939933937734>":
            if str(message.author.id) in data2["ids"]:
              embed = discord.Embed(title="<:error_ok:1002376341959757884> Blacklisted", description="You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/jkop)")
              await message.reply(embed=embed, mention_author=False)
            else:

              embed = discord.Embed(description=f"""
Hey, I'm ***Sputnik!***\n\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> Please use the following command instead: `s!help` or `s!commands`\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> If you continue to have problems, consider asking for help [discord.gg/Sputnikbot](https://discord.gg/ZrcXSdnM46)
""",color=0xdbdbdb) 
              view = View()
              view.add_item(button)
              view.add_item(button1)
              #view.add_item(button2)
              await message.reply(embed=embed, mention_author=True, view=view)
          else:
            return
      except Exception as error:
        if isinstance(error, discord.Forbidden):
              return





