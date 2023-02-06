import discord
import asyncio
from discord.ext import commands
import datetime
import aiohttp
from io import BytesIO
import discord
import time
from discord import User, errors
import re
from discord.ui import Button, View
import typing
import typing as t
from discord.ext.commands import has_permissions, MissingPermissions, has_role, has_any_role
import asyncio
from datetime import datetime
from discord.ext.commands.cooldowns import BucketType
from discord.ext import commands
from utils.Tools import *
from core import Cog, Sputnik, Context
#############LUND LELO MADARCHOD######
TICK = "<:xxtick:1064599740081246279>"
CROSS = "<:xxcross:1064599805797609494>"
PASS = "0x00ff1b"
FAIL = "0xff0000"
#############SABKI MAA KA BHOSDA######

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tasks = []


    @commands.hybrid_command(name="prefixx", aliases=["setprefix","prefixset"], help="Allows you to change prefix of the bot for this server")
    @blacklist_check()
  #  @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    async def _prefix(self, ctx: commands.Context, prefix):
        data = getConfig(ctx.guild.id)
        mod = data["mod"]
        admin = data["admin"]
        if str(ctx.author.id) in admin or str(ctx.author.id)in mod or ctx.author == ctx.guild.owner:#          data = getConfig(ctx.guild.id)
          data["prefix"] = str(prefix)  
          updateConfig(ctx.guild.id, data)
          await ctx.reply(embed=discord.Embed(description=f"{TICK} Successfully changed my prefix!", color={PASS}))

    @commands.hybrid_command(aliases=['sb'],help="Literally trolling command or you can use to clear all messages by the user.",usage="softban <member>")
    @blacklist_check()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def softban(self, ctx, member: discord.Member, *, reason=None):
      
    
        button = Button(emoji="<:aaTick:1068082961368489984>", style=discord.ButtonStyle.green)
        button1 = Button(emoji="<:aaCross:1068083356853600256>", style=discord.ButtonStyle.red)
        async def button_callback(interaction: discord.Interaction):
          a = 0
          if interaction.user == ctx.author:
              await interaction.response.edit_message(content=f"Lund", embed=True, view=None)
        if reason is None:
              reason = f"No reason given.\nBanned by {ctx.author}"
              await interaction.member.ban(reason=reason)
              await interaction.member.unban(reason=reason)
              a += 1
              await interaction.channel.send(content=f"Interaction Completed Successfully!")
    
        async def button1_callback(interaction: discord.Interaction):
            if interaction.user == ctx.author:
                await interaction.response.edit_message(
                    content="Ok I will Not unban anyone.",
                    embed=None,
                    view=None)
            else:
                await interaction.response.send_message(
                    "This Is Not For You Dummy!",
                    embed=None,
                    view=None,
                    ephemeral=True)

        embed = discord.Embed(
            description=
            '**Are you sure you want to unban everyone in this guild?**')

        view = View()
        button.callback = button_callback
        button1.callback = button1_callback
        view.add_item(button)
        view.add_item(button1)
        await ctx.reply(embed=embed, view=view, mention_author=False)        

        

    @commands.hybrid_command(aliases=['stfu'],help="Ban a user from your server.",usage="ban <member>")
    @blacklist_check()
    @commands.guild_only()
 #   @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
      data = getConfig(ctx.guild.id)
      mod = data["mod"]
      admin = data["admin"]
      if str(ctx.author.id) in admin or str(ctx.author.id)in mod or ctx.author == ctx.guild.owner:
      
        if reason is None:
            reason = f"No reason given.\nBanned by {ctx.author}"

        await member.ban(reason=reason)
        #await member.unban(reason=reason)
        hacker = discord.Embed(color={PASS},description=f"{TICK} Sucessfully banned {member} for {reason}.", timestamp=ctx.message.created_at)
        await ctx.send(embed=hacker)



    @commands.group(invoke_without_command=True,help="Clears the messages",usage="purge <amount>")
    @commands.has_guild_permissions(manage_messages=True)
    @blacklist_check()
    async def purge(self, ctx,amount:int=10):
        if amount >1000:
          return await ctx.send(f"{CROSS} Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        deleted = await ctx.channel.purge(limit=amount+1)
        return await ctx.send(f"{TICK} Successfully Purged {len(deleted)-1} messages")
      

    @purge.command(help="Clears the messages starts with the given letters",usage="purge startswith <text>")
    @blacklist_check()
    @commands.has_guild_permissions(manage_messages=True)
    async def startswith(self, ctx, key, amount: int = 10):
        if amount >1000:
            return await ctx.send(f"{CROSS} Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if m.content.startswith(key):
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"{TICK} Deleted {len(deleted)}/{amount} messages which started with the given keyword!")


    @purge.command(help="Clears the messages ends with the given letter",usage="purge endswith <text>")
    @blacklist_check()
    @commands.has_guild_permissions(manage_messages=True)
    async def endswith(self, ctx, key, amount: int = 10):
        if amount >1000:
            return await ctx.send(f"{CROSS} Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if m.content.endswith(key):
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"{TICK} Deleted {len(deleted)}/{amount} messages which ended with the given keyword!")

    @purge.command(help="Clears the messages contains with the given argument",usage="purge contains <message>")
    @blacklist_check()
    @commands.has_guild_permissions(manage_messages=True)
    async def contains(self, ctx, key, amount: int = 10):
        if amount >1000:
            return await ctx.send(f"{CROSS} Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if key in m.content:
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"{TICK} Deleted {len(deleted)}/{amount} message(s) which contained the given keyword!")

    @purge.command(help="Clears the messages of the given user",usage="purge <user>")
    @blacklist_check()
    @commands.has_guild_permissions(manage_messages=True)
    async def user(self, ctx, user: discord.Member, amount: int = 10):
        if amount >1000:
            return await ctx.send(f"{CROSS} Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if m.author.id == user.id:
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"{TICK} Deleted {len(deleted)}/{amount} messages which were sent by the mentioned user!")

    @purge.command(help="Clears the messages containing invite links",usage="purge invites")
    @blacklist_check()
    @commands.has_guild_permissions(manage_messages=True)
    async def invites(self, ctx, amount: int = 10):
        if amount >1000:
            return await ctx.send(f"{CROSS} Purge limit exceeded. Please provide an integer which is less than or equal to 1000.")
        global counter
        counter = 0

        def check(m):
            global counter
            if counter >= amount:
                return False

            if "discord.gg/" in m.content.lower():
                counter += 1
                return True
            else:
                return False
        deleted = await ctx.channel.purge(limit=100, check=check)
        return await ctx.send(f"{TICK} Deleted {len(deleted)}/{amount} messages which contained invites!")


      
    @commands.hybrid_command(name="mute", description="Timeouts someone for specific time.",usage="mute <member> <time>")
    @commands.cooldown(1, 5, commands.BucketType.user)
   # @commands.has_permissions(manage_messages=True)
    async def mute(self,ctx, member: discord.Member, minutes: int, reason="None"):
      data = getConfig(ctx.guild.id)
      mod = data["mod"]
      admin = data["admin"]
      if str(ctx.author.id) in admin or str(ctx.author.id)in mod or ctx.author == ctx.guild.owner:
      #if member.id == ctx.author.id:
        await ctx.send(embed=discord.Embed(color={FAIL}, description=f"{CROSS} You can't mute yourself"))
      elif member.top_role.position >= ctx.author.top_role.position:
        await ctx.send(embed=discord.Embed(color={FAIL}, description=f"{CROSS} You can only mute members below you"))
      elif member.top_role.position < ctx.author.top_role.position:
        duration = datetime.timedelta(minutes=minutes)
        await member.timeout(duration, reason=reason)
        await ctx.send(embed=discord.Embed(color={FAIL}, description=f"{TICK} Successfully muted {member.mention} for {minutes}, reason: {reason}"))
        await member.send(f"{TICK} You have been muted from: {ctx.guild.name} reason: {reason}")


    @commands.hybrid_command(name="unmute", description="removes a user from timeout",usage="unmute <member>")
    @commands.cooldown(1, 5, commands.BucketType.user)
  #  @commands.has_permissions(manage_messages=True)
    async def unmute(self,ctx, member: discord.Member):
      data = getConfig(ctx.guild.id)
      mod = data["mod"]
      admin = data["admin"]
      if str(ctx.author.id) in admin or str(ctx.author.id)in mod or ctx.author == ctx.guild.owner:
     # if member.id == ctx.author.id:
        await ctx.send(embed=discord.Embed(color={FAIL}, description=f"{CROSS} You are not muted"))
      elif member.top_role.position >= ctx.author.top_role.position:
        await ctx.send(embed=discord.Embed(color={FAIL}, description=f"{CROSS} You can only unmute members below you"))
      elif member.top_role.position < ctx.author.top_role.position:
        duration = datetime.timedelta(minutes=0)
        await member.timeout(duration)
        await ctx.send(embed=discord.Embed(color={PASS}, description=f"{TICK} Successfully Unmuted {member.mention}"))
        hacker1 = discord.Embed(color={PASS},description=f"{TICK} You have been unmuted from: {ctx.guild.name}", timestamp=ctx.message.created_at)
        await member.send(embed=hacker1)



    @commands.hybrid_command(aliases=['kik'],help="Somebody is breaking rules simply kick him from the server as punishment",usage="kick <member>")
    @blacklist_check()
   # @commands.has_permissions(kick_members=True)
    async def kick(self, ctx: commands.Context, member: discord.Member, *, reason=None):
        if member == self.bot:
            await ctx.send(f"{CROSS} You cannot kick me!")
        data = getConfig(ctx.guild.id)
        mod = data["mod"]
        admin = data["admin"]
        if str(ctx.author.id) in admin or str(ctx.author.id)in mod or ctx.author == ctx.guild.owner:#if ctx.author.top_role.position > member.top_role.position or member == ctx.guild.owner:
            await member.kick(reason=reason)
            hacker = discord.Embed(color={PASS},description=f"{TICK} Successfully kicked {member.display_name} from this guild, for: {reason}", timestamp=ctx.message.created_at)
            #hacker.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://media.discordapp.net/attachments/1004709672588161044/1005073754889654343/a_9a2d97cca8cf934ac4b3624051ed9baf.gif")
            hacker.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
            #hacker.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048")
            await ctx.send(embed=hacker)
            hacker1 = discord.Embed(color={PASS},description=f"{TICK} You have been kicked from {ctx.guild.name} for: {reason}!", timestamp=ctx.message.created_at)
            #hacker1.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://media.discordapp.net/attachments/1004709672588161044/1005073754889654343/a_9a2d97cca8cf934ac4b3624051ed9baf.gif")
           # hacker1.set_thumbnail(url = "https://cdn.discordapp.com/avatars/1024854362801057884/af987937665a69cc5fc01f587179d7ae.webp?size=2048")
            await member.send(embed=hacker1)
        if not ctx.author.top_role.position > member.top_role.position and ctx.author != ctx.guild.owner:
            await ctx.send(f"{TICK} You cannot kick someone with a higher role than you!")


  
    @commands.hybrid_command(aliases=['wa'],help="To warn a specific user.",usage="warn <member>")
    @blacklist_check()
  #  @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member, * , reason="No Reason Provided!"):
      data = getConfig(ctx.guild.id)
      mod = data["mod"]
      admin = data["admin"]
      if str(ctx.author.id) in admin or str(ctx.author.id)in mod or ctx.author == ctx.guild.owner:
        hacker = discord.Embed(color={PASS},description=f"{TICK} {member.display_name} has been warned for: {reason}", timestamp=ctx.message.created_at)
        
        hacker.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
        
        await ctx.send(embed=hacker)
        hacker1 = discord.Embed(color={PASS},description=f"{TICK} You have been warned in {ctx.guild.name} for: {reason}", timestamp=ctx.message.created_at)
 
        await member.send(embed=hacker1)

        
    @commands.hybrid_command(help="If someone realizes his mistake you should unban him",usage="unban [user]")
    @blacklist_check()
  #  @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id: int):
      data = getConfig(ctx.guild.id)
      mod = data["mod"]
      admin = data["admin"]
      if str(ctx.author.id) in admin or str(ctx.author.id)in mod or ctx.author == ctx.guild.owner:
        user = await self.bot.fetch_user(id)
        await ctx.guild.unban(user)
        hacker = discord.Embed(color={PASS},description=f"{TICK} {user.name} has been successfully unbanned", timestamp=ctx.message.created_at)


        await ctx.send(embed=hacker)

    @commands.command(help="Clones a channel .")
    @blacklist_check()
    @commands.is_owner()
    @commands.has_permissions(manage_channels=True)
    async def clone(self, ctx, channel: discord.TextChannel):
        await channel.clone()
        hacker = discord.Embed(color={PASS},description=f"{TICK} {channel.name} has been successfully cloned", timestamp=ctx.message.created_at)
        
        hacker.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
        await ctx.send(embed=hacker)

  
    @commands.group(aliases=["c"],invoke_without_command=True,help="Clears the messages")
    @blacklist_check()
    @commands.guild_only()
    @commands.max_concurrency(1, per=commands.BucketType.guild)
    async def clear(self, ctx):
        embed = discord.Embed(color=0xdbdbdb)
        embed.add_field(name="**Clear Commands!**", value="`clear all` , `clear bots` , `clear embeds` , `clear files` , `clear mentions` , `clear images` , `clear contains` , `clear reactions`")
        await ctx.reply(embed=embed, mention_author=False)
    
    async def do_removal(self, ctx, limit, predicate, *, before=None, after=None, message=True):
        if limit > 1000:
            em = discord.Embed(description=f" Too many messages to search given ({limit}/2000)", color=0x00FFE4)
            return await ctx.send(embed=em)

        if not before:
            before = ctx.message
        else:
            before = discord.Object(id=before)

        if after:
            after = discord.Object(id=after)

        try:
            deleted = await ctx.channel.purge(limit=limit, before=before, after=after, check=predicate)
        except discord.HTTPException as e:
            em = discord.Embed(description=f" Try a smaller search?", color=0x00FFE4)
            return await ctx.send(embed=em)

        deleted = len(deleted)
        if message is True:
            await ctx.message.delete()
            await ctx.send(embed= discord.Embed(description=f" Successfully removed {deleted} message{'' if deleted == 1 else 's'}.", color=0x00FFE4, delete_after=3))

    @clear.command(aliases=["e"])
    @blacklist_check()
    @commands.has_permissions(manage_messages=True)
    
    async def embeds(self, ctx, search=1000):
        """Removes messages that have embeds in them."""
        await self.do_removal(ctx, search, lambda e: len(e.embeds))

    @clear.command(aliases=["f"])
    @blacklist_check()
    @commands.has_permissions(manage_messages=True)
    
    async def files(self, ctx, search=1000):
        """Removes messages that have attachments in them."""
        await self.do_removal(ctx, search, lambda e: len(e.attachments))

    @clear.command(aliases=["m"])
    @blacklist_check()
    @commands.has_permissions(manage_messages=True)
    
    async def mentions(self, ctx, search=1000):
        """Removes messages that have mentions in them."""
        await self.do_removal(ctx, search, lambda e: len(e.mentions) or len(e.role_mentions))

    @clear.command(aliases=["i"])
    @blacklist_check()
    @commands.has_permissions(manage_messages=True)
    
    
    async def images(self, ctx, search=1000):
        """Removes messages that have embeds or attachments."""
        await self.do_removal(ctx, search, lambda e: len(e.embeds) or len(e.attachments))

    @clear.command(name="all")
    @blacklist_check()    
    
    async def _remove_all(self, ctx, search=1000):
        """Removes all messages."""
        await self.do_removal(ctx, search, lambda e: True)

    @clear.command(aliases=["co"])
    @blacklist_check()
    @commands.has_permissions(manage_messages=True)  
    
    async def contains(self, ctx, *, substr: str):
        """Removes all messages containing a substring.
        The substring must be at least 3 characters long.
        """
        if len(substr) < 3:
            await ctx.send("The substring length must be at least 3 characters.")
        else:
            await self.do_removal(ctx, 1000, lambda e: substr in e.content)

    @clear.command(name="bots", aliases=["b"])
    @blacklist_check()
    @commands.has_permissions(manage_messages=True)
    
    
    async def _bots(self, ctx, search=100, prefix=None):
        """Removes a bot user's messages and messages with their optional prefix."""

        getprefix = [";", "$", "!", "-", "?", ">", "^", "$", "w!", ".", ",", "a?", "g!", "m!", "s?"]

        def predicate(m):
            return (m.webhook_id is None and m.author.bot) or m.content.startswith(tuple(getprefix))

        await self.do_removal(ctx, search, predicate)

    @clear.command(name="emojis", aliases=["em"])
    @blacklist_check()
    @commands.has_permissions(manage_messages=True)
    
    
    async def _emojis(self, ctx, search=1000):
        """Removes all messages containing custom emoji."""
        custom_emoji = re.compile(r"<a?:(.*?):(\d{17,21})>|[\u263a-\U0001f645]")

        def predicate(m):
            return custom_emoji.search(m.content)

        await self.do_removal(ctx, search, predicate)
        
    @clear.command(name="reactions", aliases=["r"])
    @blacklist_check()
    @commands.has_permissions(manage_messages=True)
    
    
    async def _reactions(self, ctx, search=1000):
        """Removes all reactions from messages that have them."""

        if search > 2000:
            return await ctx.send(f"Too many messages to search for ({search}/2000)")

        total_reactions = 0
        async for message in ctx.history(limit=search, before=ctx.message):
            if len(message.reactions):
                total_reactions += sum(r.count for r in message.reactions)
                await message.clear_reactions()
        await ctx.message.delete()
        await ctx.send(embed=discord.Embed(description=f"<:GreenTick:1029990379623292938> | Successfully Removed {total_reactions}.", color=0x00FFE4))



    @commands.command(
                      help="Nukes a channel",
                      usage="nuke"
                      )
    @blacklist_check()
    @commands.is_owner()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(manage_channels=True)
    async def nuke(self, ctx, channel: discord.TextChannel = None):
        channel = channel if channel else ctx.channel
        newchannel = await channel.clone()
        await newchannel.edit(position=channel.position)
        await channel.delete()
        embed = discord.Embed(
            title="nuke",
            description="Channel has been nuked by **`%s`**" % (ctx.author),
            color=0x00FFE4)
        embed.set_image(
            url="https://media2.giphy.com/media/HhTXt43pk1I1W/giphy.gif")
        await newchannel.send(embed=embed)




    @commands.command(
                      help="Locks down a channel",
                      usage="lock <channel> <reason>",
                      aliases=["lockdown"])
    @blacklist_check()
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_channels=True)
    async def lock(self,
                   ctx,
                   channel: discord.TextChannel = None,
                   *,
                   reason=None):
        if channel is None: channel = ctx.channel
        try:
            await channel.set_permissions(
                ctx.guild.default_role,
                overwrite=discord.PermissionOverwrite(send_messages=False),
                reason=reason)
            await ctx.send(embed=discord.Embed(
                title="Astroz | Lockdown",
                description="<:GreenTick:1018174649198202990> | Successfully locked **%s**" % (channel.mention),
                color=0x00FFE4))
        except:
            await ctx.send(
                embed=discord.Embed(title="Lockdown",
                                    description="Failed to lockdown **%s**" %
                                    (channel.mention),
                                    color=0x00FFE4))
        else:
            pass

    @commands.command(
                      help="Unlocks a channel",
                      usage="unlock <channel> <reason>",
                      aliases=["unlockdown"])
    @blacklist_check()
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_channels=True)
    async def unlock(self,
                     ctx,
                     channel: discord.TextChannel = None,
                     *,
                     reason=None):
        if channel is None: channel = ctx.channel
        try:
            await channel.set_permissions(
                ctx.guild.default_role,
                overwrite=discord.PermissionOverwrite(send_messages=True),
                reason=reason)
            await ctx.send(embed=discord.Embed(
                title="Astroz | Unlockdown",
                description="<:GreenTick:1018174649198202990> | Successfully unlocked **%s**" %
                (channel.mention),
                color=0x00FFE4))
        except:
            await ctx.send(
                embed=discord.Embed(title="Astroz | Unlockdown",
                                    description="Failed to lock **`%s`**" %
                                    (channel.mention),
                                    color=0x00FFE4))
        else:
            pass

    @commands.command(
                      help="Changes the slowmode",
                      usage="slowmode [seconds]",
                      aliases=["slow"])
    @blacklist_check()
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self, ctx, seconds: int = 0):
        if seconds > 120:
            return await ctx.send(embed=discord.Embed(
                title="slowmode",
                description="Slowmode can not be over 2 minutes",
                color=0x00FFE4))
        if seconds == 0:
            await ctx.channel.edit(slowmode_delay=seconds)
            await ctx.send(
                embed=discord.Embed(title="slowmode",
                                    description="Slowmode is disabled",
                                    color=0x00FFE4))
        else:
            await ctx.channel.edit(slowmode_delay=seconds)
            await ctx.send(
                embed=discord.Embed(title="slowmode",
                                    description="Set slowmode to **`%s`**" %
                                    (seconds),
                                    color=0x00FFE4))

    @commands.command(
                      help="Disables slowmode",
                      usage="unslowmode",
                      aliases=["unslow"])
    @blacklist_check()
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.has_permissions(manage_messages=True)
    async def unslowmode(self, ctx):
        await ctx.channel.edit(slowmode_delay=0)
        await ctx.send(embed=discord.Embed(title="unslowmode",
                                           description="Disabled slowmode",
                                           color=0x00FFE4))


 
#Discord bot channel block command

