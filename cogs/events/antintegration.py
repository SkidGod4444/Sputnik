import os
import discord
from discord.ext import commands
import requests
import sys
import setuptools
from itertools import cycle
import threading
import datetime
import logging
from core import Sputnik, Cog
import time
import asyncio
import aiohttp
import tasksio
from discord.ext import tasks
import random
from utils.Tools import *

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

class antintegration(Cog):
    def __init__(self, client: Sputnik):
        self.client = client      
        self.headers = {"Authorization": f"Bot MTAzNDQ1MzkzOTkzMzkzNzczNA.GASulU.95KgzwiRyc2_uKXGdbNSpiMwqq2B7wZjx8CvX0"}
       # print("Cog Loaded: Antintegration")
    @commands.Cog.listener()
    async def on_guild_integrations_update(self, guild):
        try:
          data = getConfig(guild.id)
          anti = getantiintig(guild.id)
          punish = data["aintigpunish"]
          wl = data["integrationwl"]
          wled = data["whitelisted"]
          reason = "Creating Integration | Not Whitelisted"
          async for entry in guild.audit_logs(
                limit=1,
                after=datetime.datetime.utcnow() - datetime.timedelta(seconds=30)):
            user = entry.user.id
            api = random.randint(8,9)
            if entry.user.id == 967791712942583818:
              return
            elif entry.user == guild.owner:
              pass
            elif str(entry.user.id) in wled or wl or anti == "off":
              pass
            else:
              if entry.action == discord.AuditLogAction.integration_create:
               async with aiohttp.ClientSession(headers=self.headers) as session:
                if punish == "ban":
                    async with session.put(f"https://discord.com/api/v{api}/guilds/%s/bans/%s" % (guild.id, user), json={"reason": reason}) as r:
                      if r.status in (200, 201, 204):
                        logging.info("Successfully banned %s" % (user))
                elif punish == "kick":
                         async with session.delete(f"https://discord.com/api/v{api}/guilds/%s/members/%s" % (guild.id, user), json={"reason": reason}) as r2:
                             if r2.status in (200, 201, 204):
                               logging.info("Successfully kicked %s" % (user))
                elif punish == "none":
                    mem = guild.get_member(entry.user.id)
                    await mem.edit(roles=[role for role in mem.roles if not role.permissions.administrator], reason=reason)
                else:
                       return
        except Exception as error:
            if isinstance(error, discord.Forbidden):
              return