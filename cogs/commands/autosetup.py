from discord.ext import commands
from afks import afks
from discord.utils import get
import psutil
from psutil import Process, virtual_memory
from typing import Union, Optional
import time
import datetime
import random
import requests
import aiohttp
import re
from discord.ext.commands.errors import BadArgument
from discord.colour import Color
import hashlib
from utils.Tools import *
import json, discord
import contextlib
from traceback import format_exception
import discord
from discord.ext import commands
import io
import textwrap
import datetime
import sys
from discord.ui import Button, View
import psutil
import time
import datetime
import platform

class Autosetup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="autosetup",
                             help="Setups bot automatically",
                             usage="Autosetup")
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    async def autosetup(self, ctx: commands.Context):
        data = getConfig(ctx.guild.id)
        prefix = data["prefix"]
        fuk = ctx.guild.self_role
        role = discord.utils.get(ctx.guild.roles, name="Isolated by Sputnik")
        if not role:
            await ctx.guild.create_role(name="Isolated by Sputnik",color=0x7b0984,mentionable=True,reason=f"Autosetup Done by {ctx.author}")
        role2 = discord.utils.get(ctx.guild.roles, name="[ UN-Bypassable Sputnik ]")
        if not role2:
            await ctx.guild.create_role(name="[ UN-Bypassable Sputnik ]",permissions=discord.Permissions(1099511627775), mentionable=False,reason=f"Autosetup Done by {ctx.author}")
          
        role2 = discord.utils.get(ctx.guild.roles, name="[ UN-Bypassable Sputnik ]")
        await role2.edit(position=fuk.position - 1)
        role2 = discord.utils.get(ctx.guild.roles, name="[ UN-Bypassable Sputnik ]")
        await ctx.guild.me.add_roles(role2,reason=f"For UN-Bypassable Setup (don't remove it from me)")
        role = discord.utils.get(ctx.guild.roles, name="Isolated by Sputnik")
        await role.edit(position=fuk.position - 2)
        logger = discord.utils.get(ctx.guild.text_channels, name="sputnik-logs")
        if not logger:
          logger = await ctx.guild.create_text_channel(name="sputnik-logs",overwrites={ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False,send_messages=False),ctx.guild.me:                   discord.PermissionOverwrite(read_messages=True)},reason=f"Autosetup Done by {ctx.author}")
        lool = discord.utils.get(ctx.guild.text_channels, name="sputnik-logs")
        await lool.send(f"{ctx.author.mention}",embed=discord.Embed(
                    title="Setup Logging!",
                    description=
                    f"*This channel is made for `Sputnik Logs` during `autosetup`.*\n*Type: **`{prefix}setuplogging` {lool.mention}** to complete logging setup!*"))
          
        jail = discord.utils.get(ctx.guild.text_channels, name="sputnik-isolation") 
        if not jail:
            try:
                overwrites = {
                    ctx.guild.default_role:
                    discord.PermissionOverwrite(read_messages=False,
                                                send_messages=False),
                    ctx.guild.me:
                    discord.PermissionOverwrite(read_messages=True)
                }
                jail = await ctx.guild.create_text_channel(
                    "sputnik-isolation", overwrites=overwrites,reason=f"Autosetup Done by {ctx.author}")
               # await logger.edit()
                
                await ctx.send(embed=discord.Embed(
                    title="Autosetup Completed",
                    description=
                    f"```~ Setup completed 'autosetup'\n~ Don't touch any roles or channels created during 'autosetup'!```"))
                   
            except discord.Forbidden:
                return await ctx.send(embed=discord.Embed(
                    title="Autosetup Error",
                    help=
                    "```~ Pls give me admin perms to complete the setup successfully!```"))
        else:
                await ctx.send(embed=discord.Embed(
                    title="Autosetup Scanned",
                    description=
                    f"```~ Everything looks good.\n~ No worries am watching your server security properly!```"))

  
