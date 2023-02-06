import contextlib
from traceback import format_exception
import discord
from discord.ext import commands
import io
import asyncio
import textwrap
import datetime
from typing import *
import sys
from discord.ui import Button, View
import psutil
import time
import datetime
import platform
from utils.Tools import *
import os
os.system("pip install pymongo[srv]")
import logging
from discord.ext import commands
import motor.motor_asyncio
from pymongo import MongoClient
from discord.ext.commands import BucketType, cooldown
import requests
import motor.motor_asyncio as mongodb
from typing import Optional

arrow = "<:aaArrow:1068097808269320232>"
space = "<:aaJaduEmo:1068098084501995591>"
color = "<:aaColor:1067829519731392573>"
profile = "<:aaProfile:1068097557978431538>"

import aiohttp
import urllib.parse
import json

start_time = time.time()
#########3
def datetime_to_seconds(thing: datetime.datetime):
    current_time = datetime.datetime.fromtimestamp(time.time())
    return round(round(time.time()) + (current_time - thing.replace(tzinfo=None)).total_seconds())
cluster = motor.motor_asyncio.AsyncIOMotorClient(       "mongodb+srv://insane:op5@cluster0.5qyw6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

notedb = cluster["discord"]["note"]

class Extra(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.connection = mongodb.AsyncIOMotorClient(
          "mongodb+srv://insane:op5@cluster0.5qyw6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        )
        self.db = self.connection["Sputnik"]["servers"]    

    @commands.group(name="Quarantine", description="Quarantines a user", usage="Quarantine <user>", aliases=["qu", "isolate", "q", "iso"])
    @blacklist_check()
    @ignore_check()
    @commands.has_permissions(administrator=True)
    async def Quarantine(self, ctx, member: discord.Member):
        lund = discord.utils.get(ctx.guild.text_channels, name="isolation")
        roles = discord.utils.get(ctx.guild.roles, name="Isolated by Sputnik")
        if not roles:      
          await ctx.send(embed=discord.Embed(title="Isolation",description="```No `Isolated` role found in this server!\nPlease type `s!autosetup` to complete the setup process automatically.```"), delete_after=100)
        #else:
          
        elif not lund:
            await ctx.send(embed=discord.Embed(title="Isolation",description="```No `Isolation` channel found in this server!\nPlease type `s!autosetup` to complete the setup process automatically.```"), delete_after=100)
        else:
          await member.edit(roles=[role for role in member.roles if not role.permissions.administrator])
          await member.add_roles(roles)
          await ctx.reply(embed=discord.Embed(description="Successfully Isolated **%s**" % (member.mention)), delete_after=101)
          await member.send(embed=discord.Embed(description="You have been isolated in **`%s`** by **%s**" % (ctx.guild.name, ctx.author.mention)))
       

    @commands.command(aliases=['inv'])
    @blacklist_check()
    async def invite(self, ctx: commands.Context):
        embed = discord.Embed(title="**Invite Sputnik:**", description = f"Add **[Sputnik](https://discord.com/oauth2/authorize?client_id=1034453939933937734&permissions=2113268958&scope=bot)** & also join our **[Support Server](https://discord.gg/ZrcXSdnM46)** for more help!",timestamp=ctx.message.created_at)
        embed.set_footer(text="Invite with all perms for better experience!") #,icon_url="https://media.discordapp.net/attachments/1004709672588161044/1005073754889654343/a_9a2d97cca8cf934ac4b3624051ed9baf.gif")
       # embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
        b = Button(label='Invite Me', style=discord.ButtonStyle.link, url='https://discord.com/oauth2/authorize?client_id=1034453939933937734&permissions=2113268958&scope=bot')
        himanshu = Button(label='Support Server', style=discord.ButtonStyle.link, url='https://discord.gg/ZrcXSdnM46')
        #SkidGod = Button(label='Vote Me', style=discord.ButtonStyle.link, url='https://discord.com/oauth2/authorize?client_id=1021416292185546854&permissions=2113268958&scope=bot')
        view = View()
        view.add_item(b)
        view.add_item(himanshu)
        #view.add_item(SkidGod)
        await ctx.send(embed=embed,view=view)
      

    @commands.cooldown(1, 60, commands.BucketType.user)
    @blacklist_check()
    @commands.hybrid_command(aliases=['bi'], help="Bot Information!")
    async def botinfo(self, ctx: commands.Context):
        embed = discord.Embed(
            title="Sputnik Information:",
            description="Sputnik is a best security bot for your **[server](https://discord.gg/3YmDAzbuRR)** and its the **[v2](https://discord.gg/3YmDAzbuRR)** of Sputnik!",
            
            timestamp=datetime.datetime.utcnow()
        ).add_field(
            name="__Sputnik Stats:__",
            value=f"""<:1spacer:1056545806943006760><:profile:1056855971839873054> **Servers:** `{len(self.bot.guilds)}`
<:1spacer:1056545806943006760><:person:1053178413478838312> **Users:** `{len(self.bot.users)}`
<:1spacer:1056545806943006760><:Mod:1051999330745209002> **Commands:** `{len(set(self.bot.walk_commands()))}`
<:1spacer:1056545806943006760><:tiktik:1056815610199285800> **Uptime:** `{str(datetime.timedelta(seconds=int(round(time.time()-start_time))))}`
<:1spacer:1056545806943006760><:bots:1058524565929738290> **Version:** `v2`
            """,
            inline=True
        
        ).set_footer(text=self.bot.user.name, icon_url=self.bot.user.display_avatar.url
                    )
        await ctx.reply(embed=embed)


    @commands.hybrid_command(aliases=["sinfo","si"])
    @blacklist_check()
    async def serverinfo(self, ctx: commands.Context):
        nsfw_level = ''
        if ctx.guild.nsfw_level.name == 'default':
          nsfw_level = 'Default'
        if ctx.guild.nsfw_level.name == 'explicit':
          nsfw_level = 'Explicit'
        if ctx.guild.nsfw_level.name == 'safe':
          nsfw_level = 'Safe'
        if ctx.guild.nsfw_level.name == 'age_restricted':
          nsfw_level = 'Age Restricted'
        guild: discord.Guild = ctx.guild
        button2 = discord.ui.Button(label='Channels',style=discord.ButtonStyle.grey)
        button1 = discord.ui.Button(label='Settings',style=discord.ButtonStyle.grey)
       # button3 = discord.ui.Button(label='Features',style=discord.ButtonStyle.grey)
        view = discord.ui.View()
        view.add_item(button2)
        view.add_item(button1)
       # view.add_item(button3)
        async def button2_callback(interaction: discord.Interaction):
          embed1 = discord.Embed(description=f'**__Channels Info:__**\n\n__Categories:__ `{len(guild.categories)}`\n__Channels:__ `{len(guild.text_channels)}`\n__Voice:__ `{len(guild.voice_channels)}`\n__Threads:__ `{len(guild.threads)}`', color=0xdbdbdb)
          await interaction.response.send_message(embed=embed1, ephemeral=True)
        async def button1_callback(interaction: discord.Interaction):
          embed5=discord.Embed(description=f'**__Settings Info__:**\n\n__System Channel:__ {"None" if guild.system_channel is None else guild.system_channel.mention}\n__Verification Level:__ `{str(guild.verification_level).title()}`\n__NSFW level:__ `{nsfw_level}`\n__Explicit Content Filter:__ `{guild.explicit_content_filter.name}`\n__Boost Tier:__ `{guild.premium_tier}`\n__Max Talk Bitrate:__ `{int(guild.bitrate_limit)} kbps`\n__Roles:__ `{len(guild.roles)}`\n__Emojis:__ `{len(guild.emojis)}`\n__Stickers:__ `{len(guild.stickers)}',color=0xdbdbdb)
          await interaction.response.send_message(embed=embed5, ephemeral=True)        
        
        
        embed = discord.Embed(color=0xdbdbdb,
            title=" **__Server Information__**"#,
 #         description=f"**Description:** {guild.description}"
        )#.set_author(
            #name=guild.name,
  #          icon_url=guild.me.display_avatar.url if guild.icon is None else guild.icon.url
        #)#.set_footer(text=f"ID: {guild.id}")
        if guild.icon is not None:
            embed.set_thumbnail(url=guild.icon.url)
        embed.add_field(
            name=f"*Basic Info:*",
            value=f"""
<:profile:1056855971839873054> **Name:** {ctx.guild.name}
<:1spacer:1056545806943006760><:urrow:1053243283549204520> ID: {guild.id}
<:rowner:1053178553161760778> **Owner:** <@{guild.owner_id}>
<:1spacer:1056545806943006760><:urrow:1053243283549204520> ID: {guild.owner_id}
<:Creation_Sputnik:1061081782969184296> **Creation:** {guild.created_at.month}/{guild.created_at.day}/{guild.created_at.year}
<:Category_Sputnik:1061081353506009198> **Description:** {guild.description}
<:1spacer:1056545806943006760><:Bot_Sputnik:1061081612365877298> Managed: {len(list(filter(lambda m: m.bot, guild.members)))}
<:1spacer:1056545806943006760><:Danger_Sputnik:1061081041789530123> Dangerous: {len([
            skidgod for skidgod in ctx.guild.members
            if skidgod.guild_permissions.administrator
        ])}           """,
            inline=False
        )
        #embed.add_field(
           # name="**Members Info:**",
          #  value=f"""
#**Members:** {len(guild.members)}
#**Humans:** {len(list(filter(lambda m: not m.bot, guild.members)))}
#**Bots:** {len(list(filter(lambda m: m.bot, guild.members)))}
           # """,
           # inline=True
       # )
        
        
       # if guild.features:
           # embed.add_field(
   #             name="**__Features:__**",
             #   value=' | '.join([feature.replace('_', ' ').title() for feature in guild.features]),
               # inline=False
            #)
        #if guild.banner is not None:
  #          embed.set_image(url=guild.banner.url)
        button2.callback = button2_callback
        button1.callback = button1_callback
        return await ctx.reply(embed=embed,view=view)

    @commands.hybrid_command(name="userinfo",
                             aliases=["whois", "ui"],
                             usage="Userinfo [user]",with_app_command = True)
    @commands.cooldown(1, 2, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    async def _userinfo(self,
                        ctx,
                        member: Optional[Union[discord.Member, discord.User]] = None):
        if member == None or member == "":
            member = ctx.author
        elif member not in ctx.guild.members:
            member = await self.bot.fetch_user(member.id)

        badges = ""
        if member.public_flags.hypesquad:
            badges += "<:EventosHypesquad:1071604263425417310> "
        if member.public_flags.hypesquad_balance:
            badges += "<:Hypesquad_Balance:1070559023864229918> "
        if member.public_flags.hypesquad_bravery:
            badges += "<:hypesquadbravery:1070559034496798850> "
        if member.public_flags.hypesquad_brilliance:
            badges += "<:hypesquadbriliance:1070559056554639450> "
        if member.public_flags.early_supporter:
            badges += "<:early:1070559304240861195> "
        if member.public_flags.active_developer:
            badges += "<:activedev:1070557702977228840> "
        if member.public_flags.verified_bot_developer:
            badges += "<:Devloper:1070558311130345492> "
        if member.public_flags.discord_certified_moderator:
            badges += "<:mod_programs_alumni:1070561635019800606> "
        if member.public_flags.staff:
            badges += "<:staff:1070560615455793174> "
        if member.public_flags.bug_hunter:
            badges += "<:BugHunter_Level1:1070563817739788358> "
        if member.public_flags.partner:
            badges += "<:Partner:1070560021970169866> "
        if badges == None or badges == "":
            badges += "None"

        if member in ctx.guild.members:
            nickk = f"{member.nick if member.nick else 'None'}"
            joinedat = f"<t:{round(member.joined_at.timestamp())}:R>"
        else:
            nickk = "None"
            joinedat = "None"

        kp = ""
        if member in ctx.guild.members:
            if member.guild_permissions.kick_members:
                kp += "Kick Members"
            if member.guild_permissions.ban_members:
                kp += " , Ban Members"
            if member.guild_permissions.administrator:
                kp += " , Administrator"
            if member.guild_permissions.manage_channels:
                kp += " , Manage Channels"
            if member.guild_permissions.manage_messages:
                kp += " , Manage Messages"
            if member.guild_permissions.mention_everyone:
                kp += " , Mention Everyone"
            if member.guild_permissions.manage_nicknames:
                kp += " , Manage Nicknames"
            if member.guild_permissions.manage_roles:
                kp += " , Manage Roles"
            if member.guild_permissions.manage_webhooks:
                kp += " , Manage Webhooks"
            if member.guild_permissions.manage_emojis:
                kp += " , Manage Emojis"

            if kp is None or kp == "":
                kp = "None"

        if member in ctx.guild.members:
            if member == ctx.guild.owner:
                aklm = "Server Owner"
            elif member.guild_permissions.administrator:
                aklm = "Server Admin"
            elif member.guild_permissions.ban_members or member.guild_permissions.kick_members:
                aklm = "Server Moderator"
            else:
                aklm = "Server Member"

        bannerUser = await self.bot.fetch_user(member.id)
        embed = discord.Embed(color=0x2f3136)
        embed.timestamp = discord.utils.utcnow()
        if not bannerUser.banner:
            pass
        else:
            embed.set_image(url=bannerUser.banner)
        embed.set_author(name=f"{member.name}'s Information",
                         icon_url=member.avatar.url
                         if member.avatar else member.default_avatar.url)
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.
                            default_avatar.url)
        embed.add_field(name="__General Information__",
                        value=f"""
**Name:** {member}
**ID:** {member.id}
**Nickname:** {nickk}
**Bot?:** {'Yes' if member.bot else 'No'}
**Badges:** {badges}
**Account Created:** <t:{round(member.created_at.timestamp())}:R>
**Server Joined:** {joinedat}
            """,
                        inline=False)
        if member in ctx.guild.members:
            r = (', '.join(role.mention for role in member.roles[1:][::-1])
                 if len(member.roles) > 1 else 'None.')
            embed.add_field(name="__Role Info__",
                            value=f"""
**Highest Role:** {member.top_role.mention if len(member.roles) > 1 else 'None'}
**Roles [{f'{len(member.roles) - 1}' if member.roles else '0'}]:** {r if len(r) <= 1024 else r[0:1006] + ' and more...'}
**Color:** {member.color if member.color else '000000'}
                """,
                            inline=False)
        if member in ctx.guild.members:
            embed.add_field(
                name="__Extra__",
                value=
                f"**Boosting:** {f'<t:{round(member.premium_since.timestamp())}:R>' if member in ctx.guild.premium_subscribers else 'None'}\n**Voice <:jk_vc171771:1050950158566821999>:** {'None' if not member.voice else member.voice.channel.mention}",
                inline=False)
        if member in ctx.guild.members:
            embed.add_field(name="__Key Permissions__",
                            value=", ".join([kp]),
                            inline=False)
        if member in ctx.guild.members:
            embed.add_field(name="__Acknowledgement__",
                            value=f"{aklm}",
                            inline=False)
        if member in ctx.guild.members:
            embed.set_footer(
                text=f"Requested by {ctx.author}",
                icon_url=ctx.author.avatar.url
                if ctx.author.avatar else ctx.author.default_avatar.url)
        else:
            if member not in ctx.guild.members:
                embed.set_footer(
                    text=f"{member.name} not in this this server.",
                    icon_url=ctx.author.avatar.url
                    if ctx.author.avatar else ctx.author.default_avatar.url)
        await ctx.send(embed=embed)
    @commands.hybrid_command(help="Shows you all information about a role.",usage="Roleinfo <role>")
    @blacklist_check()
    @ignore_check()
    #@commands.is_owner()
    async def roleinfo(self, ctx: commands.Context, *, role: discord.Role):
        """Get information about a role"""
        content = discord.Embed(title=f"Role Information!")
        if role.permissions.administrator:
          tut = "<:aaTick:1068082961368489984>"
        else:
          tut = "<:aaCross:1068083356853600256>"
        #content.colour = role.color
        if role.hoist is True:
          lund = "<:aaTick:1068082961368489984>"
        else:
          lund = "<:aaCross:1068083356853600256>"
        if role.mentionable is True:
          fof = "<:aaTick:1068082961368489984>"
        else:
          fof = "<:aaCross:1068083356853600256>"
        if isinstance(role.icon, discord.Asset):
            content.set_thumbnail(url=role.icon.url)
        elif isinstance(role.icon, str):
            content.title = f"{role.icon} @{role.name} | #{role.id}"
        
        content.add_field(name="General Informations:", value=f"{profile} **Name:** `{role.name}`\n{space}{arrow} **Id:** `{role.id}`\n{color} **Color:** `{str(role.color).upper()}`")
        content.add_field(name="Extra Informations:", value=f"{arrow} **Mention:** {role.mention}\n{arrow} **Inrole:** `{len(role.members)}`\n{arrow} **Hoisted?** {lund}\n{arrow} **Mentionable?** {fof}\n{arrow} **Dangerous?** {tut}")
       # content.add_field(name="Role Type:", value=f"**Bot?**{lol}\n**Integration?** {lmaoo}\n**Subscription?** {sub}")
            
        


       # perms = []
       # for perm, allow in iter(role.permissions):
           # if allow:
         #       perms.append(f"`{perm.upper()}`")

        #if perms:
         #   content.add_field(name="Allowed permissions", value=", ".join(perms), inline=False)

        await ctx.send(embed=content)



    @blacklist_check()
    @commands.is_owner()
    @commands.group(
                      description="Shows users status",
                      usage="status <member>")
    async def status(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        status = member.status
        if status == discord.Status.offline:
            status_location = "Not Applicable"
        elif member.mobile_status != discord.Status.offline:
            status_location = "Mobile"
        elif member.web_status != discord.Status.offline:
            status_location = "Browser"
        elif member.desktop_status != discord.Status.offline:
            status_location = "Desktop"
        else:
            status_location = "Not Applicable"
        await ctx.send(embed=discord.Embed(title="**<a:zOR_lulladance:1002196227229761566> | status**",
                                           description="`%s`: `%s`" %
                                           (status_location, status),
                                           color=0x00FFE4))



    @commands.group(name="list")
    async def __list_(self, ctx):
      print("list cmd by Sputnik!")    
    @__list_.command(name="boosters", aliases=["boost", "booster"],usage="List boosters")
    async def list_boost(self, ctx):
      guild = ctx.guild
      embed = discord.Embed(title=f"List of Boosters in {guild.name} - {len(guild.premium_subscribers)}", color=0x00FFE4, description="")
      for no, member in enumerate(guild.premium_subscribers, start=1):
        embed.description += f"`[{no}]` | {member} [{member.mention}] - <t:{round(member.premium_since.timestamp())}:R>\n"
      embed.set_footer(text="Made By ~ Hacker_xD#0001", icon_url="https://media.discordapp.net/attachments/1036538198236614676/1037664035186954270/blue_circle.jpg")
      await ctx.send(embed=embed)

    @__list_.command(name="inrole", aliases=["inside-role"])
    async def list_inrole(self, ctx, role: discord.Role):
      guild = ctx.guild
      embed = discord.Embed(title=f"List of Members in {role} - {len(role.members)}", color=0xdbdbdb, description="")
      for no, member in enumerate(role.members, start=1):
        embed.description += f"`[{no}]` | {member} [{member.mention}]\n"
      await ctx.send(embed=embed)

      
    @commands.group(
                  help="Adds a emoji",
                      usage="steal <emoji>",
                      aliases=["eadd"])
    @blacklist_check()
    @commands.is_owner()
    @commands.has_permissions(manage_emojis=True)
    async def steal(self, ctx, emote):
        try:
            if emote[0] == '<':
                name = emote.split(':')[1]
                emoji_name = emote.split(':')[2][:-1]
                anim = emote.split(':')[0]
                if anim == '<a':
                    url = f'https://cdn.discordapp.com/emojis/{emoji_name}.gif'
                else:
                    url = f'https://cdn.discordapp.com/emojis/{emoji_name}.png'
                try:
                    response = requests.get(url)
                    img = response.content
                    emote = await ctx.guild.create_custom_emoji(name=name,
                                                                image=img)
                    return await ctx.send(
                        embed=discord.Embed(title="emoji-add",
                                            description="added \"**`%s`**\"!" %
                                            (emote),
                                            color=0x00FFE4))
                except Exception:
                    return await ctx.send(
                        embed=discord.Embed(title="emoji-add",
                                            description=f"failed to add emoji",
                                            color=0x00FFE4))
            else:
                return await ctx.send(
                    embed=discord.Embed(title="emoji-add",
                                        description=f"invalid emoji",
                                        color=0x00FFE4))
        except Exception:
            return await ctx.send(
                embed=discord.Embed(title="emoji-add",
                                    description=f"failed to add emoji",
                                    color=0x00FFE4))

    @commands.command(help="Deletes the emoji from the server",usage="removeemoji <emoji>")
    @blacklist_check()
    @commands.is_owner()
    @commands.has_permissions(manage_emojis=True)
    async def removeemoji(self, ctx, emoji: discord.Emoji):
        await emoji.delete()
        await ctx.send(f"**<a:black_astroz:1002204507985432666> emoji has been deleted.**")

    @commands.command(help="Unbans Everyone In The Guild!", aliases=['massunban'],usage="Unbanall")
    @blacklist_check()
    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only() 
    @commands.has_permissions(ban_members=True)
    async def unbanall(self, ctx):
        button = Button(label="Yes", style=discord.ButtonStyle.green)
        button1 = Button(label="No", style=discord.ButtonStyle.red)
        async def button_callback(interaction: discord.Interaction):
          a = 0
          if interaction.user == ctx.author:
            #if interaction.guild.me.guild_permissions.ban_members:
              await interaction.response.edit_message(content=f"Unbanning All Banned Member(s)", embed=None, view=None)
              async for idk in interaction.guild.bans(limit=None):
                await interaction.guild.unban(user=idk.user, reason="Unbanall By: {}".format(ctx.author))
                a += 1
              await interaction.channel.send(content=f"Interaction Completed Successfully!")
           # else:
             # await interaction.response.edit_message(content="I am missing ban members permission.\ntry giving me permissions and retry", embed=None, view=None)
          else: 
            await interaction.response.send_message("This Is Not For You Dummy!", embed=None, view=None, ephemeral=True) 

        async def button1_callback(interaction: discord.Interaction): 
          if interaction.user == ctx.author: 
            await interaction.response.edit_message(content="Ok I will not unban anyone in this guild", embed=None, view=None)
          else:
            await interaction.response.send_message("This Is Not For You Dummy!", embed=None, view=None, ephemeral=True)
        embed = discord.Embed(title='Confirmation',
                          color=0xdbdbdb,
                          description=f'**Are you sure you want to unban everyone in this guild?**')
        embed.set_footer(text="Powered by Sputnik!")
        
        view = View()
        button.callback = button_callback
        button1.callback = button1_callback
        view.add_item(button)
        view.add_item(button1)
        await ctx.reply(embed=embed, view=view, mention_author=False)




    @commands.command(
                      help="Shows when a user joined",
                      usage="joined-at [user]",
                      aliases=["joined-at"])
    @blacklist_check()
    async def joined_at(self, ctx):
        joined = ctx.author.joined_at.strftime("%a, %d %b %Y %I:%M %p")
        await ctx.send(embed=discord.Embed(title="joined Position!",
                                           description="**`%s`**" % (joined),
                                            color=0xdbdbdb))


    @commands.command(
                      help="Shows the latency",
                      usage="ping",
                      aliases=["latency"])
    @blacklist_check()
    @ignore_check()
    async def ping(self, ctx):
        before = time.monotonic()
        await self.db.find_one({"ping": 1})
        db = round(time.monotonic() - before) * 1000
        shard = shard = self.bot.get_shard(ctx.guild.shard_id)
        ping_ = int(shard.latency * 1000)
       # lund = int(shard.guilds)
        if ping_ < 25:
            client_emoji = "<:icons_online:1002486864076353547>"
        elif ping_ < 50:
            client_emoji = "<a:ping:1038031810283708508>"
        else:
            client_emoji = "<:icons_online:1002486864076353547>"
        if db < 25:
            db_emoji = "<:icons_online:1002486864076353547>"
        elif db < 50:
            db_emoji = "<a:ping:1038031810283708508>"
        else:
            db_emoji = "<a:ping:1038031846769971250>"
        embed=discord.Embed(
            title="Sputnik Status:")#.add_field(name=f"Shard [{ctx.guild.shard_id}]", value=f"**Latency:** `{ping_}`\n**Db Latency:** `{db}`")
        await ctx.send(embed)

            
            #"**%s Shard **`%s`** latency: `%sms`\n%s Database latency: `%sms`**"
           # % (client_emoji, ctx.guild.shard_id, ping_, db_emoji, db)))


    @commands.command(help="get info about voice channel",usage="Vcinfo <VoiceChannel>")
    @blacklist_check()
    @commands.is_owner()
    async def vcinfo(self, ctx: Context, vc: discord.VoiceChannel):
      e = discord.Embed(title='VC Information', color=0x00FFE4)
      e.add_field(name='VC name', value=vc.name, inline=False)
      e.add_field(name='VC ID', value=vc.id, inline=False)
      e.add_field(name='VC bitrate', value=vc.bitrate, inline=False)
      e.add_field(name='Mention', value=vc.mention, inline=False)
      e.add_field(name='Category name', value=vc.category.name, inline=False)
      #e.add_field(name='VC Created', value=format_date(vc.created_at), inline=False)
      await ctx.send(embed=e)




    @commands.command(help="shows info about channel",aliases=['channeli', 'cinfo', 'ci'], pass_context=True, no_pm=True,usage="Channelinfo [channel]")
    @blacklist_check()
    @commands.is_owner()
    async def channelinfo(self, ctx, *, channel: int = None):
        """Shows channel information"""
        if not channel:
            channel = ctx.message.channel
        else:
            channel = self.bot.get_channel(channel)
        data = discord.Embed()
        if hasattr(channel, 'mention'):
            data.description = "**Information about Channel:** " + channel.mention
        if hasattr(channel, 'changed_roles'):
            if len(channel.changed_roles) > 0:
                data.color = 0x00FFE4 if channel.changed_roles[0].permissions.read_messages else 0x00FFE4
        if isinstance(channel, discord.TextChannel): 
            _type = "Text"
        elif isinstance(channel, discord.VoiceChannel): 
            _type = "Voice"
        else: 
            _type = "Unknown"
        data.add_field(name="Type", value=_type)
        data.add_field(name="ID", value=channel.id, inline=False)
        if hasattr(channel, 'position'):
            data.add_field(name="Position", value=channel.position)
        if isinstance(channel, discord.VoiceChannel):
            if channel.user_limit != 0:
                data.add_field(name="User Number", value="{}/{}".format(len(channel.voice_members), channel.user_limit))
            else:
                data.add_field(name="User Number", value="{}".format(len(channel.voice_members)))
            userlist = [r.display_name for r in channel.members]
            if not userlist:
                userlist = "None"
            else:
                userlist = "\n".join(userlist)
            data.add_field(name="Users", value=userlist)
            data.add_field(name="Bitrate", value=channel.bitrate)
        elif isinstance(channel, discord.TextChannel):
            try:
                pins = await channel.pins()
                data.add_field(name="Pins", value=len(pins), inline=True)
            except discord.Forbidden:
                pass
            data.add_field(name="Members", value="%s"%len(channel.members))
            if channel.topic:
                data.add_field(name="Topic", value=channel.topic, inline=False)
            hidden = []
            allowed = []
            for role in channel.changed_roles:
                if role.permissions.read_messages is True:
                    if role.name != "@everyone":
                        allowed.append(role.mention)
                elif role.permissions.read_messages is False:
                    if role.name != "@everyone":
                        hidden.append(role.mention)
            if len(allowed) > 0: 
                data.add_field(name='Allowed Roles ({})'.format(len(allowed)), value=', '.join(allowed), inline=False)
            if len(hidden) > 0:
                data.add_field(name='Restricted Roles ({})'.format(len(hidden)), value=', '.join(hidden), inline=False)
        if channel.created_at:
            data.set_footer(text=("Created on {} ({} days ago)".format(channel.created_at.strftime("%d %b %Y %H:%M"), (ctx.message.created_at - channel.created_at).days)))
        await ctx.send(embed=data)



    @commands.command(cooldown_after_parsing=True, help="Creates a note for you",usage="Note <message>")
    @cooldown(1, 10, BucketType.user)
    @blacklist_check()
    async def note(self, ctx, *, message):
        message = str(message)
        print(message)
        stats = await notedb.find_one({"id": ctx.author.id})
        if len(message) <= 50:
            #
            if stats is None:
                newuser = {"id": ctx.author.id, "note": message}
                await notedb.insert_one(newuser)
                await ctx.send("**Your note has been stored**")
                await ctx.message.delete()

            else:
                x = notedb.find({"id": ctx.author.id})
                z = 0
                async for i in x:
                    z += 1
                if z > 2:
                    await ctx.send("**You cannot add more than 3 notes**")
                else:
                    newuser = {"id": ctx.author.id, "note": message}
                    await notedb.insert_one(newuser)
                    await ctx.send("**Yout note has been stored**")
                    await ctx.message.delete()

        else:
            await ctx.send("**Message cannot be greater then 50 characters**")

    @commands.command(help="Shows your note",usage="Notes")
    @blacklist_check()
    async def notes(self, ctx):
        stats = await notedb.find_one({"id": ctx.author.id})
        if stats is None:
            embed = discord.Embed(
                timestamp=ctx.message.created_at,
                title="Notes",
                description=f"{ctx.author.mention} has no notes",
                color=0xdbdbdb,
            )
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
                title="Notes", description=f"Here are your notes", color=0xdbdbdb
            )
            x = notedb.find({"id": ctx.author.id})
            z = 1
            async for i in x:
                msg = i["note"]
                embed.add_field(name=f"Note {z}", value=f"{msg}", inline=False)
                z += 1
            await ctx.send(embed=embed)
          #  await ctx.send("**Please check your private messages to see your notes**")

    @commands.command(help="Delete the notes , it's a good practice",usage="Trashnotes")
    @blacklist_check()
    async def trashnotes(self, ctx):
        try:
            await notedb.delete_many({"id": ctx.author.id})
            await ctx.send("**Your notes have been deleted , thank you**")
        except:
            await ctx.send("**You have no record**")


    @commands.command(name="badges", help="Check what premium badges a user have.", aliases=["badge","bg","pr","profile"],usage="Badges [user]")
    @blacklist_check()
    async def _badges(self, ctx, user: Optional[discord.User] = None):
      mem = user or ctx.author
      badges = getbadges(mem.id)
      if badges == []:
        embed2 = discord.Embed(description="<a:premium:1056725098641494167> **Premium:**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> No premium plan found!\n<:profile:1056855971839873054> **Profile Badges:**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> No badges found!\n\n**Need Badges?**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> Join our [Support Server](https://discord.gg/3YmDAzbuRR) to achieve some badges.", color=0xdbdbdb)
        embed2.set_author(name=f"{mem}'s Profile Overview:", icon_url =mem.avatar.url if mem.avatar else mem.default_avatar.url)
        embed2.set_thumbnail(url=mem.avatar.url if mem.avatar else mem.default_avatar.url)  
        embed2.timestamp = discord.utils.utcnow()   
        await ctx.reply(embed=embed2, mention_author=False)
      else:
        embed = discord.Embed(description="<a:premium:1056725098641494167> **Premium:**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> No premium plan found!\n<:profile:1056855971839873054> **Profile Badges:**\n",color=0xdbdbdb)
        embed.set_author(name=f"{mem}'s Profile Overview:", icon_url =mem.avatar.url if mem.avatar else mem.default_avatar.url)
        embed.set_thumbnail(url=mem.avatar.url if mem.avatar else mem.default_avatar.url)
        embed.timestamp = discord.utils.utcnow()
        for badge in badges:
          embed.description += f"**{badge}**\n"
        await ctx.reply(embed=embed, mention_author=False)


    def parse_google_card(self, node):
        if node is None or type(node) is int:
            return None

        e = discord.Embed(colour=0x0057e7)

        # check if it's a calculator card:
        calculator = node.find(".//table/tr/td/span[@class='nobr']/h2[@class='r']")
        if calculator is not None:
            e.title = 'Calculator'
            e.description = ''.join(calculator.itertext())
            return e

        parent = node.getparent()

        # check for unit conversion card
        unit = parent.find(".//ol//div[@class='_Tsb']")
        if unit is not None:
            e.title = 'Unit Conversion'
            e.description = ''.join(''.join(n.itertext()) for n in unit)
            return e

        # check for currency conversion card
        currency = parent.find(".//ol/table[@class='std _tLi']/tr/td/h2")
        if currency is not None:
            e.title = 'Currency Conversion'
            e.description = ''.join(currency.itertext())
            return e

        # check for release date card
        release = parent.find(".//div[@id='_vBb']")
        if release is not None:
            try:
                e.description = ''.join(release[0].itertext()).strip()
                e.title = ''.join(release[1].itertext()).strip()
                return e
            except:
                return None

        # check for definition card
        words = parent.find(".//ol/div[@class='g']/div/h3[@class='r']/div")
        if words is not None:
            try:
                definition_info = words.getparent().getparent()[1]
            except:
                pass
            else:
                try:
                    e.title = words[0].text
                    e.description = words[1].text
                except:
                    return None
                for row in definition_info:
                    if len(row.attrib) != 0:
                        break
                    try:
                        data = row[0]
                        lexical_category = data[0].text
                        body = []
                        for index, definition in enumerate(data[1], 1):
                            body.append('%s. %s' % (index, definition.text))
                        e.add_field(name=lexical_category, value='\n'.join(body), inline=False)
                    except:
                        continue
                return e

        # check for translate card
        words = parent.find(".//ol/div[@class='g']/div/table/tr/td/h3[@class='r']")
        if words is not None:
            e.title = 'Google Translate'
            e.add_field(name='Input', value=words[0].text,  inline=True)
            e.add_field(name='Out', value=words[1].text,  inline=True)
            return e

        # check for "time in" card
        time_in = parent.find(".//ol//div[@class='_Tsb _HOb _Qeb']")
        if time_in is not None:
            try:
                time_place = ''.join(time_in.find("span[@class='_HOb _Qeb']").itertext()).strip()
                the_time = ''.join(time_in.find("div[@class='_rkc _Peb']").itertext()).strip()
                the_date = ''.join(time_in.find("div[@class='_HOb _Qeb']").itertext()).strip()
            except:
                return None
            else:
                e.title = time_place
                e.description = '%s\n%s' % (the_time, the_date)
                return e

        weather = parent.find(".//ol//div[@class='e']")
        if weather is None:
            return None

        location = weather.find('h3')
        if location is None:
            return None

        e.title = ''.join(location.itertext())

        table = weather.find('table')
        if table is None:
            return None

        try:
            tr = table[0]
            img = tr[0].find('img')
            category = img.get('alt')
            image = 'https:' + img.get('src')
            temperature = tr[1].xpath("./span[@class='wob_t']//text()")[0]
        except:
            return None
        else:
            e.set_thumbnail(url=image)
            e.description = '*%s*' % category
            e.add_field(name='Temperature', value=temperature)

        try:
            wind = ''.join(table[3].itertext()).replace('Wind: ', '')
        except:
            return None
        else:
            e.add_field(name='Wind', value=wind)

        try:
            humidity = ''.join(table[4][0].itertext()).replace('Humidity: ', '')
        except:
            return None
        else:
            e.add_field(name='Humidity', value=humidity)

        return e




    @commands.command(pass_context=True)
    async def g(self, ctx, *, query):
        """Google web search. Ex: [p]g what is discordapp?"""
        if not embed_perms(ctx.message):
            config = load_optional_config()
            async with self.bot.session.get("https://www.googleapis.com/customsearch/v1?q=" + urllib.parse.quote_plus(query) + "&start=1" + "&key=" + config['google_api_key'] + "&cx=" + config['custom_search_engine']) as resp:
                result = json.loads(await resp.text())
            return await ctx.send(result['items'][0]['link'])

        try:
            entries, root = await get_google_entries(query, session=self.bot.session)
            card_node = root.find(".//div[@id='topstuff']")
            card = self.parse_google_card(card_node)
        except RuntimeError as e:
            await ctx.send(str(e))
        else:
            if card:
                value = '\n'.join(entries[:2])
                if value:
                    card.add_field(name='Search Results', value=value, inline=False)
                return await ctx.send(embed=card)
            if not entries:
                return await ctx.send('No results.')
            next_two = entries[1:3]
            if next_two:
                formatted = '\n'.join(map(lambda x: '<%s>' % x, next_two))
                msg = '{}\n\n**See also:**\n{}'.format(entries[0], formatted)
            else:
                msg = entries[0]
            await ctx.send(msg)
    @commands.group(name="autoresponder",
                    invoke_without_command=True,
                    aliases=['ar'])
    @blacklist_check()
    
    async def _ar(self, ctx: commands.Context):
        if ctx.subcommand_passed is None:
            await ctx.send_help(ctx.command)
            ctx.command.reset_cooldown(ctx)


            

    @_ar.command(name="create")
    @commands.has_permissions(administrator=True)
    @blacklist_check()
    
    async def _create(self, ctx, name, *, message):
        with open("autoresponse.json", "r") as f:
            autoresponse = json.load(f)
        numbers = []
        if str(ctx.guild.id) in autoresponse:
            for autoresponsecount in autoresponse[str(ctx.guild.id)]:
                numbers.append(autoresponsecount)
            if len(numbers) >= 10:
                hacker6 = discord.Embed(
                    title="Autoresponder!",
                    description=
                    f"<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:rightshort:1053176997481828452> Sorry you can't add more this server has reached the max no.of autoresponders!",
                    color=0xdbdbdb)
    #            hacker6.set_author(name=f"{ctx.author}",
   #                                icon_url=f"{ctx.author.avatar}")
                hacker6.set_thumbnail(url=f"{ctx.author.avatar}")
                return await ctx.send(embed=hacker6)
        if str(ctx.guild.id) in autoresponse:
            if name in autoresponse[str(ctx.guild.id)]:
                hacker = discord.Embed(
                    title="Autoresponder!",
                    description=
                    f"<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:rightshort:1053176997481828452> The autoresponse with the `{name}` is already exists!",
                    color=0xdbdbdb)
   #             hacker.set_author(name=f"{ctx.author}",
   #                               icon_url=f"{ctx.author.avatar}")
                hacker.set_thumbnail(url=f"{ctx.author.avatar}")
                return await ctx.send(embed=hacker)
        if str(ctx.guild.id) in autoresponse:
            autoresponse[str(ctx.guild.id)][name] = message
            with open("autoresponse.json", "w") as f:
                json.dump(autoresponse, f, indent=4)
            hacker1 = discord.Embed(
                title="Autoresponder!",
                description=
                f"<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:rightshort:1053176997481828452> Successfully Created Autoresponder named `{name}`",
                color=0xdbdbdb)
       #     hacker1.set_author(name=f"{ctx.author}",
  #                             icon_url=f"{ctx.author.avatar}")
            hacker1.set_thumbnail(url=f"{ctx.author.avatar}")
            return await ctx.reply(embed=hacker1)

        data = {
            name: message,
        }
        autoresponse[str(ctx.guild.id)] = data

        with open("autoresponse.json", "w") as f:
            json.dump(autoresponse, f, indent=4)
            hacker2 = discord.Embed(
                title="Autoresponder!",
                description=
                f"<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:rightshort:1053176997481828452> Successfully Created Autoresponder named `{name}`",
                color=0xdbdbdb)
     #       hacker2.set_author(name=f"{ctx.author}",
  #                             icon_url=f"{ctx.author.avatar}")
            hacker2.set_thumbnail(url=f"{ctx.author.avatar}")
            return await ctx.reply(embed=hacker2)

    @_ar.command(name="delete")
    @commands.has_permissions(administrator=True)
    @blacklist_check()
    
    async def _delete(self, ctx, name):
        with open("autoresponse.json", "r") as f:
            autoresponse = json.load(f)

        if str(ctx.guild.id) in autoresponse:
            if name in autoresponse[str(ctx.guild.id)]:
                del autoresponse[str(ctx.guild.id)][name]
                with open("autoresponse.json", "w") as f:
                    json.dump(autoresponse, f, indent=4)
                hacker1 = discord.Embed(
                    title="Autoresponder!",
                    description=
                    f"<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:rightshort:1053176997481828452> Successfully Deleted Autoresponder named `{name}`",
                    color=0xdbdbdb)
#                hacker1.set_author(name=f"{ctx.author}",
                                   #icon_url=f"{ctx.author.avatar}")
                hacker1.set_thumbnail(url=f"{ctx.author.avatar}")
                return await ctx.reply(embed=hacker1)
            else:
                hacker = discord.Embed(
                    title="Autoresponder!",
                    description=
                    f"<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:rightshort:1053176997481828452> No Autoresponder Found With The Name `{name}`!",
                    color=0xdbdbdb)
#                hacker.set_author(name=f"{ctx.author}",
                                  #icon_url=f"{ctx.author.avatar}")
                hacker.set_thumbnail(url=f"{ctx.author.avatar}")
                return await ctx.reply(embed=hacker)
        else:
            hacker2 = discord.Embed(
                title="Autoresponder!",
                description=
                f"<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:rightshort:1053176997481828452> There is no Autoresponder Created Before!",
                color=0xdbdbdb)
            #hacker2.set_author(name=f"{ctx.author}",
                               #icon_url=f"{ctx.author.avatar}")
            hacker2.set_thumbnail(url=f"{ctx.author.avatar}")
            return await ctx.reply(embed=hacker2)

    @_ar.command(name="config")
    @commands.has_permissions(administrator=True)
    @blacklist_check()
    
    async def _config(self, ctx):
        with open("autoresponse.json", "r") as f:
            autoresponse = json.load(f)
        autoresponsenames = []
        guild = ctx.guild
        if str(ctx.guild.id) in autoresponse:
            for autoresponsecount in autoresponse[str(ctx.guild.id)]:
                autoresponsenames.append(autoresponsecount)
            embed = discord.Embed(color=0xdbdbdb)
            st, count = "", 1
            for autoresponse in autoresponsenames:
                st += f"`{'0' + str(count) if count < 10 else count}. `    **{autoresponse.upper()}**\n"
                test = count
                count += 1

                embed.title = f"<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:rightshort:1053176997481828452> There are `{test}` autoresponders in this server!"
        embed.description = st
      #  embed.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")
        embed.set_thumbnail(url=f"{ctx.author.avatar}")
        await ctx.send(embed=embed)

    @_ar.command(name="edit")
    @commands.has_permissions(administrator=True)
    @blacklist_check()
    async def _edit(self, ctx, name, *, message):
        with open("autoresponse.json", "r") as f:
            autoresponse = json.load(f)
        if str(ctx.guild.id) in autoresponse:
            if name in autoresponse[str(ctx.guild.id)]:
                autoresponse[str(ctx.guild.id)][name] = message
                with open("autoresponse.json", "w") as f:
                    json.dump(autoresponse, f, indent=4)
                hacker1 = discord.Embed(
                    title="Autoresponder!",
                    description=
                    f"<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:rightshort:1053176997481828452> Successfully Edited Autoresponder named `{name}`!",
                    color=0xdbdbdb)
                #hacker1.set_author(name=f"{ctx.author}",
                                   #icon_url=f"{ctx.author.avatar}")
                hacker1.set_thumbnail(url=f"{ctx.author.avatar}")
                return await ctx.send(embed=hacker1)
        else:
            hacker2 = discord.Embed(
                title="Autoresponder!",
                description=
                f"<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:rightshort:1053176997481828452> No Autoresponder Found With The Name `{name}` In {ctx.guild.name}",
                color=0xdbdbdb)
         #   hacker2.set_author(name=f"{ctx.author}",
                               #icon_url=f"{ctx.author.avatar}")
            hacker2.set_thumbnail(url=f"{ctx.author.avatar}")
            return await ctx.send(embed=hacker2)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if message.author == self.bot.user:
            return
        try:
            if message is not None:
                with open("autoresponse.json", "r") as f:
                    autoresponse = json.load(f)
                if str(message.guild.id) in autoresponse:
                    ans = autoresponse[str(
                        message.guild.id)][message.content.lower()]
                    return await message.channel.send(ans)
        except:
            pass




