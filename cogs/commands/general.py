import discord
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


password = ['1838812`', '382131847', '231838924', '218318371', '3145413', '43791', '471747183813474', '123747019', '312312318']
def remove(afk):
    if "[AFK]" in afk.split():
        return " ".join(afk.split()[1:])
    else:
        return afk

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.aiohttp = aiohttp.ClientSession()
        self._URL_REGEX = r'(?P<url><[^: >]+:\/[^ >]+>|(?:https?|steam):\/\/[^\s<]+[^<.,:;\"\'\]\s])'
        self.tasks = []
        self.dump_tasks = []
        self.sniped = {}
        self.afk = {}
        
        

          

 
######################


    @commands.hybrid_command(usage="Avatar [member]",
        name='avatar',
        aliases=['av', 'pfp'],
        help="""Wanna steal someone's avatar here you go
Aliases"""
    )
    @blacklist_check()
    async def avatar(self, ctx, user: discord.Member = None):
        button2 = discord.ui.Button(label='Avatar', style=discord.ButtonStyle.grey)
        button = discord.ui.Button(label='Banner', style=discord.ButtonStyle.grey)
        button3 = discord.ui.Button(label='Server Avatar', style=discord.ButtonStyle.grey)
        try:
          if user == None:
             user = ctx.author
          else:  
             user = await self.bot.fetch_user(user.id)
        except AttributeError:
            user = ctx.author
        webp = user.avatar.replace(format='webp')
        jpg = user.avatar.replace(format='jpg')
        png = user.avatar.replace(format='png')
        view = discord.ui.View()
        view.add_item(button2)
        view.add_item(button)
        view.add_item(button3)
        async def button2_callback(interaction: discord.Interaction):
          embed1 = discord.Embed(
            color=0xdbdbdb,
            title=f"{user}'s Avatar",description=f"[[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp})]"
            if not user.avatar.is_animated()
            else f"[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp}) | [`GIF`]({user.avatar.replace(format='gif')})")
          embed1.set_image(url=user.avatar.url)
          embed1.set_footer(text=f"Requested by {ctx.author}")
          await interaction.response.send_message(embed=embed1, ephemeral=True)
       # await ctx.send(embed=avemb)

        async def button_callback(interaction: discord.Interaction):
          embed5=discord.Embed(color = 0xdbdbdb, title=f"{user}'s Banner").set_footer(text=f"Requested by {ctx.author}")
          bannerUser = await self.bot.fetch_user(user.id)
          if not bannerUser.banner:
             await interaction.response.send_message('User has no banner!', ephemeral=True)   
          embed5.set_image(url=bannerUser.banner) 
          await interaction.response.send_message(embed=embed5, ephemeral=True)

        async def button3_callback(interaction: discord.Interaction):
          serverav = discord.Embed(color=0xdbdbdb,title=f"{user}'s Server Avatar")
          serverav.set_image(url=user.display_avatar.url)
          await interaction.response.send_message(embed=serverav, ephemeral=True)

        avemb = discord.Embed(
            color=0xdbdbdb,
            title="User's Avatar", url="https://discord.gg/ZrcXSdnM46", description="*Click on __Buttons__ Below To View User's __Avatar__ and __Banner__*").set_thumbnail(url =ctx.author.avatar.url).set_footer(text="Powered by Sputnik!")
        button2.callback = button2_callback
        button.callback = button_callback
        button3.callback = button3_callback
        await ctx.send(embed=avemb, mention_author=True, view=view)

    


    @commands.hybrid_command(
                      help="Get total guild members status info",
                      usage="memberstats",
                      aliases=["mstatus","gms","mst","statusall"])
    @blacklist_check()
    async def memberstats(self, ctx):
        online = 0
        offline = 0
        dnd = 0
        idle = 0
        bots = 0
        for member in ctx.guild.members:
            if member.status == discord.Status.online:
                online += 1
            if member.status == discord.Status.offline:
                offline += 1
            if member.status == discord.Status.dnd:
                dnd += 1
            if member.status == discord.Status.idle:
                idle += 1
            if member.bot:
                bots += 1
        embed = discord.Embed(
            title=f"Guild Memebers Status!",
            description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** `{ctx.guild.owner}`\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n\n<:rightshort:1053176997481828452> **Counts:**\n<:1spacer:1056545806943006760><:Roles:1057491608603467838> **Memeber(s):** `%s`\n<:1spacer:1056545806943006760><a:bots:1057611653572726824> **Bot(s):** `{bots}`\n\n<:rightshort:1053176997481828452> **Status:**\n<:1spacer:1056545806943006760><:Online:1057609953248030750> **Online Users:** `{online}`\n<:1spacer:1056545806943006760><:idle:1057610060290867321> **Idle Users:** `{idle}`\n<:1spacer:1056545806943006760><:dnd:1057610035875827753> **Dnd Users:** `{dnd}`\n<:1spacer:1056545806943006760><:offline:1057609999729315890> **Invisible Users:** `{offline}`" % (len(ctx.guild.members)),color=0xdbdbdb)
           # (ctx.guild.name),
            
        embed.set_footer(text="Powered by Sputnik!")
        
        await ctx.send(embed=embed)


    @commands.hybrid_command(
                      help="Get total guild members count",
                      usage="membercount",
                      aliases=["mc","memberscount"])
    @blacklist_check()
    async def membercount(self, ctx):
        online = 0
        offline = 0
        dnd = 0
        idle = 0
        bots = 0
        for member in ctx.guild.members:
            if member.status == discord.Status.online:
                online += 1
            if member.status == discord.Status.offline:
                offline += 1
            if member.status == discord.Status.dnd:
                dnd += 1
            if member.status == discord.Status.idle:
                idle += 1
            if member.bot:
                bots += 1
        embed = discord.Embed(
            title=f"Memebers Count!",
            description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** `{ctx.guild.owner}`\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n\n<:rightshort:1053176997481828452> **Counts:**\n<:1spacer:1056545806943006760><:Roles:1057491608603467838> **Memeber(s):** `%s`\n<:1spacer:1056545806943006760><a:bots:1057611653572726824> **Bot(s):** `{bots}`" % (len(ctx.guild.members)),color=0xdbdbdb)
           # (ctx.guild.name),
            
        embed.set_footer(text="Powered by Sputnik!")
        
        await ctx.send(embed=embed)
      
        


              
                                 #else: ("Sorry, o can't detect any NSFW content!"),
             # if rickRoll is True:
                        
                          
           # color=Color.red() if rickRoll is True else Color.green(),
       # ), mention_author=True)

    @commands.Cog.listener()
    async def on_message_delete(self, message): 
        if message.guild == None: 
            return
        if message.author.bot: 
            return
        if not message.content: 
            return 
        self.sniped[message.channel.id] = message
         #@commands.command(aliases=['sb'])
    @commands.guild_only()
    @commands.has_permissions(view_audit_log=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    @blacklist_check()
    @commands.group(name="snipe", help="Snipes the most recently deleted message", usage="snipe", aliases=["snipemsgs"])
    async def snipe(self, ctx):
        message = self.sniped.get(ctx.channel.id)
        if message == None:
            return await ctx.send(embed=discord.Embed(title="Sniped!", description=f"<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:ctx:1056735079445053481> **Message:** `No msgs found to snipe!`", color=0xdbdbdb))#timestamp=message.created_at))
        embed = discord.Embed(title="Sniped!", description=f"<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:logsx:1053178328846188565> **Sent by:** `{message.author}`\n<:1spacer:1056545806943006760><:ctx:1056735079445053481> **Message:** `{message.content}`", color=0xdbdbdb,timestamp=message.created_at)
        await ctx.reply(embed=embed)

    @commands.group(name="cleanup", help="deletes the bots messages", aliases=["purgebots"], usage="cleanup <amount>")
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    async def cleanup(self, ctx, amount: int):
        msg = await ctx.send("cleaning...")
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == self.bot.user).map(lambda m: m):
            try:
                if message.id == msg.id:
                    pass
                else:
                    await message.delete()
            except:
                pass
        await msg.edit(content="cleaned up successfully 👌")




