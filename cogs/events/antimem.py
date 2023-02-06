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
import time
import asyncio
import aiohttp
from core import Sputnik, Cog
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

class antimem(Cog):
    def __init__(self, client: Sputnik):
        self.client = client      
        self.headers = {"Authorization": f"Bot MTA0OTMxNjQ1NzU4NDAwNTE4NQ.GNY2Hi.Ual3L0hdB-1Vg_OsSLBOiya2zru_6ObVpnqlas"}

    @commands.Cog.listener()
    async def on_member_update(self, before, after) -> None:
      guild = before.guild
      role1 = discord.utils.get(before.guild.roles, name="Isolated by Sputnik")
      role2 = discord.utils.get(before.guild.roles, name="[ UN-Bypassable Sputnik ]")
      async for entry in guild.audit_logs(limit=1):
        user = entry.user.id
        if user == 1049316457584005185:
          pass
        else:
          if before.roles != after.roles:
            if role1 in before.roles:
              if role2 not in before.roles:
                if role1 not in after.roles:
                    await before.add_roles(role1,reason="You can't remove this role manually, try doing 'unisolate' that member!")
                else:
                  if role2 in after.roles:
                    await before.remove_roles(role2,reason="Assigning it to others may leads to be dangerous")
                #heksjs