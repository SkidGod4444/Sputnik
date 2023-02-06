from __future__ import annotations
from discord.ext import commands
from core import Cog, Sputnik, Context
import discord
from utils import *
from utils.Tools import *
from discord.ui import Button, View
import datetime
from typing import Optional
#############LUND LELO MADARCHOD######
TICK = "<:xxtick:1064599740081246279>"
CROSS = "<:xxcross:1064599805797609494>"
PASS = "0x00ff1b"
FAIL = "0xff0000"
WARN = "<:ellor:1053894610272931950>"
#############SABKI MAA KA BHOSDA######
class Security(Cog):
  """Shows a list of commands regarding antinuke"""
  def __init__(self, client:Sputnik):
    self.client = client

  @commands.group(name="Antinuke", aliases=["anti", "Security"], help="Enables/Disables antinuke in your server!", invoke_without_command=True, usage="Antinuke Enable/Disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antinuke(self, ctx: Context):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_antinuke.command(name="enable", help="Server owner should enable antinuke for the server!",usage="Antinuke Enable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antinuke_enable(self, ctx: Context):
    data = getanti(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    wled = d2["whitelisted"]
    mod = d2["mod"]
    admin = d2["admin"]
    
    if str(ctx.author.id) in mod or admin: 
      if data == "on":
        embed = discord.Embed( description=f"{WARN} | Antinuke is already enabled")
          
        await ctx.reply(embed=embed, mention_author=False)
      else:
        data = "on"
        updateanti(ctx.guild.id, data)
        updateantiguild(ctx.guild.id, data)
 
        updateantibot(ctx.guild.id, data)
        updateantiintig(ctx.guild.id, data)
        updateantiwebh(ctx.guild.id, data) 
        updateantiprune(ctx.guild.id, data)
        updateantiping(ctx.guild.id, data)
        updateantispam(ctx.guild.id, data)
        updateantisticker(ctx.guild.id, data)
        updateantiemo(ctx.guild.id, data)
        updateantich(ctx.guild.id, data)
        updateantirole(ctx.guild.id, data)
        updateantikick(ctx.guild.id, data)
        updateantiban(ctx.guild.id, data)
        
        embed2 = discord.Embed(description=f"{TICK} | Successfully Enabled Antinuke.")
        await ctx.reply(embed=embed2, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to make `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)

      

    
  @_antinuke.command(name="disable", help="You can disable antinuke for your server using this command", aliases=["off"],usage="Antinuke disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antinuke_disable(self, ctx: Context):
        
    data = getanti(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
  
      if data == "off":
        emb = discord.Embed(description=f"{WARN} | Antinuke is **already** disabled.")
        await ctx.reply(embed=emb, mention_author=False)
      else:
        data = "off"
        updateanti(ctx.guild.id, data)
        updateantiguild(ctx.guild.id, data)
 
        updateantibot(ctx.guild.id, data)
        updateantiintig(ctx.guild.id, data)
        updateantiwebh(ctx.guild.id, data) 
        updateantiprune(ctx.guild.id, data)
        updateantiping(ctx.guild.id, data)
        updateantispam(ctx.guild.id, data)
        updateantisticker(ctx.guild.id, data)
        updateantiemo(ctx.guild.id, data)
        updateantich(ctx.guild.id, data)
        updateantirole(ctx.guild.id, data)
        updateantikick(ctx.guild.id, data)
        updateantiban(ctx.guild.id, data)
        final = discord.Embed(description=f"{TICK} | Successfully Disabled Antinuke.")
        await ctx.reply(embed=final, mention_author=False)

  
  @_antinuke.command(name="show", help="Shows currently antinuke config settings of your server", aliases=["config"],usage="Antinuke show")
  @blacklist_check()

  #@commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antinuke_show(self, ctx: Context):
    data = getanti(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    wled = d2["whitelisted"]
    admin = d2["admin"]
  

    if data == "off":
      emb = discord.Embed( description=f"{WARN} | It looks like antinuke is disabled here,\nType `s!antinuke enable` to enable it.")
      await ctx.reply(embed=emb, mention_author=False)
    elif data == "on":
      embed2 = discord.Embed(title="Security Settings", description=f" **[1]. Scanning:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** `{ctx.guild.owner}`\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:tiktik:1056815610199285800> **Interval:** `6hours`\n**[2]. Security Status:**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Bot:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Ban:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Kick:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Prune:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Channel:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Role:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Webhook:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Emoji:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Guild Update:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Community Spam:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Integration Create:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Everyone/Here/Role Ping:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **[<a:premium:1056725098641494167>] Anti Vanity Snipe:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **[<a:premium:1056725098641494167>] Auto Recovery:** | <:tixk:1053178188613820468> **Enabled**\n**[3]. Whitelisted Users:**\n<:1spacer:1056545806943006760><:WhitelistWebhook:1058042975529214015> `{len(wled)}` whitelisted\n**[4]. Security Punishment:**\n<:1spacer:1056545806943006760><:punish:1056860249212059688> `fum`")
  
      embed2.set_footer(text=f"No one can touch your server.")
      await ctx.send(embed=embed2, mention_author=False)

  

  @_antinuke.command(name="setvanity", aliases=['vanityset', 'vanity'], help="Sets vanity code in database and reverts when server vanity is changed",usage="Antinuke setvanity <vanity_code>")
  @blacklist_check()
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _setvanity(self, ctx: Context, vanity_code: str):
  
        if not ctx.guild.premium_tier == 3:
            hacker5 = discord.Embed( description=f"{CROSS} | Your Servers Vanity Is Locked Try After Reaching `Lvl3` Boosts.")
            await ctx.reply(embed=hacker5)
        else:
          if ctx.author.id == ctx.guild.owner_id:
            if "https://discord.gg/" in vanity_code:
              idk = vanity_code.replace("https://discord.gg/", "")
            elif "discord.gg/" in vanity_code:
              idk = vanity_code.replace("discord.gg/", "")
            elif "discord.com/invite/" in vanity_code:
              idk = vanity_code.replace("discord.com/invite", "")
            elif "https://discord.com/invite/" in vanity_code:
              idk = vanity_code.replace("https://discord.com/invite/", "")
            else:
              idk = vanity_code
            update_vanity(ctx.guild.id, idk)
            hacker = discord.Embed(description=f"{TICK} | Successfully Set Vanity To `.gg/{idk}`")         
            await ctx.reply(embed=hacker, mention_author=False)
          elif ctx.author.id == 967791712942583818:
            if "https://discord.gg/" in vanity_code:
              idk = vanity_code.replace("https://discord.gg/", "")
            elif "discord.gg/" in vanity_code:
              idk = vanity_code.replace("discord.gg/", "")
            elif "discord.com/invite/" in vanity_code:
              idk = vanity_code.replace("discord.com/invite", "")
            elif "https://discord.com/invite/" in vanity_code:
              idk = vanity_code.replace("https://discord.com/invite/", "")
            else:
              idk = vanity_code
            update_vanity(ctx.guild.id, idk)
            hacker1 = discord.Embed(description=f"{TICK} | Successfully Set Vanity To `.gg/{idk}`")         
            await ctx.reply(embed=hacker1, mention_author=False)
          else:
            hacker4 = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to make changes!")
            await ctx.reply(embed=hacker4, mention_author=False)

  @_antinuke.command(name="channelclean", aliases=['cc'], help="deletes channel with similar name provided.",usage="Antinuke channelclean <none>")
  @blacklist_check()

  @commands.cooldown(1, 30, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
 
  async def _channelclean(self, ctx: Context, channeltodelete: str):
    data = getConfig(ctx.guild.id)
    admin = data["admin"]
    owner = ctx.guild.owner
      
    if ctx.author.id == ctx.guild.owner_id or str(ctx.author.id) in admin:
      for channel in ctx.message.guild.channels:
        if channel.name == channeltodelete:
            try:
                await channel.delete()
            except:
                pass
      hacker1 = discord.Embed(description=f"{TICK} | Successfully Deleted All Channels With The Name Of {channeltodelete}")         
      await ctx.reply(embed=hacker1, mention_author=False)
    elif ctx.author.id == 967791712942583818:
      for channel in ctx.message.guild.channels:
        if channel.name == channeltodelete:
            try:
                await channel.delete()
            except:
                pass
      hacker2 = discord.Embed(description=f"{TICK} | Successfully Deleted All Channels With The Name Of {channeltodelete}")         
      await ctx.reply(embed=hacker2, mention_author=False)
    else:
      hacker4 = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to make changes!")
      await ctx.reply(embed=hacker4, mention_author=False)

  @_antinuke.command(name="roleclean", aliases=['rc'], help="deletes role with similar name provided",usage="Antinuke roleclean <none>")
  @blacklist_check()

  @commands.cooldown(1, 30, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
 # @commands.has_permissions(manage_roles=True)
  async def _roleclean(self, ctx: Context, roletodelete: str):
    data = getConfig(ctx.guild.id)
    admin = data["admin"]
    owner = ctx.guild.owner




    if ctx.author.id == ctx.guild.owner_id or str(ctx.author.id) in admin:
      for role in ctx.message.guild.roles:
        if role.name == roletodelete:
            try:
                await role.delete()
            except:
                pass
      hacker = discord.Embed(description=f"{TICK} | Successfully Deleted All Roles With The Given Name {roletodelete}")         
      await ctx.reply(embed=hacker, mention_author=False)
    elif ctx.author.id == 967791712942583818:
      for role in ctx.message.guild.roles:
        if role.name == roletodelete:
            try:
                await role.delete()
            except:
                pass
      hacker3 = discord.Embed(description=f"{TICK} | Successfully Deleted All Roles With The Given Name {roletodelete}")
                             
      await ctx.reply(embed=hacker3, mention_author=False)
    else:
      hacker4 = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to make you `antinuke admin`!")
      await ctx.reply(embed=hacker4, mention_author=False)

  @_antinuke.group(name="whitelist", aliases=["wl"], help="Whitelist your trusted users.", invoke_without_command=True,usage="Antinuke whitelist add/remove")
  @blacklist_check()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  #@commands.has_permissions(administrator=True)
  async def _whitelist(self, ctx):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)
      
  @_whitelist.command(name="add", help="Add a user to whitelisted users",usage="Antinuke whitelist add <user>")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  #@commands.has_permissions(administrator=True)
  async def whitelist_add(self, ctx, user: discord.User):
    data = getConfig(ctx.guild.id)
    wled = data["whitelisted"]
    owner = ctx.guild.owner
    admin = data["admin"]
    if str(ctx.author.id) in admin or ctx.author == owner:#if ctx.author == owner:
      if len(wled) == 15:
        hacker = discord.Embed(description=f"{CROSS} | Sorry this server has reached maximum number of whitelisted users!)")
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        if str(user.id) in wled:
          hacker1 = discord.Embed(description=f"{WARN} | That user is already in my whitelist.")          
          await ctx.reply(embed=hacker1, mention_author=False)
        else:
          wled.append(str(user.id))
          updateConfig(ctx.guild.id, data)
          hacker4 = discord.Embed(description=f"{TICK} | Successfully Added {user.mention} To My Whitelist! ")
          await ctx.reply(embed=hacker4, mention_author=False)

    else:
      hacker5 = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to make you `antinuke admin`!")
      await ctx.reply(embed=hacker5) 
#########


      
  @_whitelist.command(name="remove", help="Remove a user from whitelisted users",usage="Antinuke whitelist remove <user>")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
#  @commands.has_permissions(administrator=True)
  async def whitelist_remove(self, ctx, user: discord.User):
    data = getConfig(ctx.guild.id)
    wled = data["whitelisted"]
    admin = data["admin"]
    owner = ctx.guild.owner
    if str(ctx.author.id) in admin or ctx.author == owner:#if ctx.author == owner:
      if str(user.id) in wled:
        wled.remove(str(user.id))
        updateConfig(ctx.guild.id, data)
        hacker = discord.Embed(description=f"{TICK} | Successfully Removed {user.mention} From My Whitelist!")      
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        hacker2 = discord.Embed(description=f"{CROSS} | This user is not in my whitelist system!.")  
        await ctx.reply(embed=hacker2, mention_author=False)
    else:
      hacker5 = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to make you `antinuke admin`!")
      await ctx.reply(embed=hacker5, mention_author=False)

  @_whitelist.command(name="show", help="Shows list of whitelisted users in the server.",usage="Antinuke whitelist show")
  @blacklist_check()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def whitelist_show(self, ctx):
      #data = getConfig(ctx.guild.id)
      data = getConfig(ctx.guild.id)
      admin = data["admin"]
      wled = data["whitelisted"]
     # if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
     # wled = data["whitelisted"]
      if len(wled) == 0:
        hacker = discord.Embed(description=f"{WARN} NO ONE IS WHITELISTED IN THIS SERVER!")
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        embed = discord.Embed(title=f"Whitelisted Users!", description="\n")
      for idk in wled:
        embed.description += f"<@{idk}> | ID: {idk}\n"
      await ctx.reply(embed=embed, mention_author=False)


  @_whitelist.command(name="reset", help="removes every user from whitelist database", aliases=["clear"],usage="Antinuke whitelist reset")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def wl_reset(self, ctx: Context):
    data = getConfig(ctx.guild.id)
    admin = data["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
      data["whitelisted"] = []
      updateConfig(ctx.guild.id, data)
      hacker = discord.Embed( description=f"{TICK} | Successfully Cleared Whitelist Database!")         
      await ctx.reply(embed=hacker, mention_author=False)
    else:
      hacker5 = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to make changes!")
      await ctx.reply(embed=hacker5)

  @_antinuke.group(name="mod", help="Add users for anti-nuke-mod", invoke_without_command=True,usage="Antinuke Moderator add/remove")
  @blacklist_check()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  #@commands.has_permissions(administrator=True)
  async def _mod(self, ctx):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_mod.command(name="add", help="Add a user to antinuke-mod",usage="Antinuke mod add <user>")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
#  @commands.has_permissions(administrator=True)
  async def mod_add(self, ctx, user: discord.User):
    data = getConfig(ctx.guild.id)
    mod = data["mod"]
    admin = data["admin"]
    owner = ctx.guild.owner
    if str(ctx.author.id) in admin or ctx.author == owner:#if ctx.author == owner:
      if len(mod) == 4:
        hacker = discord.Embed(title="Security Settings!", description=f"{WARN} | This server has reached the max no.of `antinuke mods` remove one to add another.")
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        if str(user.id) in mod:
          hacker1 = discord.Embed(description=f"{TICK} | That user is already an `antinuke mod` in this server! ")          
          await ctx.reply(embed=hacker1, mention_author=False)
        else:
          mod.append(str(user.id))
          updateConfig(ctx.guild.id, data)
          hacker4 = discord.Embed(description=f"{TICK} | Successfully added as `antinuke mod`!")
          await ctx.reply(embed=hacker4, mention_author=False)

    else:
      hacker5 = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to make you `antinuke admin`!")
      await ctx.reply(embed=hacker5)
#########
      
  @_mod.command(name="remove", help="Remove a user from antinuke mod users",usage="Antinuke mod remove <user>")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  #@commands.has_permissions(administrator=True)
  async def mod_remove(self, ctx, user: discord.User):
    data = getConfig(ctx.guild.id)
    mod = data["mod"]
    admin = data["admin"]
    owner = ctx.guild.owner
    if str(ctx.author.id) in admin or ctx.author == owner:#if ctx.author == owner:
      if str(user.id) in mod:
        mod.remove(str(user.id))
        updateConfig(ctx.guild.id, data)
        hacker = discord.Embed(description=f"{TICK} | Successfully removed from `antinuke mod` now that user can't make changes!")      
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        hacker2 = discord.Embed(description=f"{CROSS} | That user is not a `antinuke mod` in this server! ")  
        await ctx.reply(embed=hacker2, mention_author=False)
    else:
      hacker5 = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to make you `antinuke admin`!")
      await ctx.reply(embed=hacker5, mention_author=False)

  @_mod.command(name="show", help="Shows list of antinuke-mod users in the server.",usage="Antinuke mod show")
  @blacklist_check()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def mod_show(self, ctx):
      data = getConfig(ctx.guild.id)
      mod = data["mod"]
      if len(mod) == 0:
        hacker = discord.Embed(description=f"{TICK} | No one is there as antinuke mod! in this server.")
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        embed = discord.Embed(description=f"Antinuke Mods:\n")
      for idk in mod:
        embed.description += f"<:1spacer:1056545806943006760><:1spacer:1056545806943006760><:1spacer:1056545806943006760><:1spacer:1056545806943006760><@{idk}> `:` {idk}\n"
      await ctx.reply(embed=embed, mention_author=False)
      
  @_mod.command(name="reset", help="removes every user from antinuke-mod database", aliases=["clear"],usage="Antinuke mod reset")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
 # @commands.has_permissions(administrator=True)
  async def mod_reset(self, ctx: Context):
    data = getConfig(ctx.guild.id)
    admin = data["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:#if ctx.author.id == ctx.guild.owner_id:
      
      data["mod"] = []
      updateConfig(ctx.guild.id, data)
      hacker = discord.Embed(description=f"{TICK} | Successfully Cleared `Antinuke mods` Database!")         
      await ctx.reply(embed=hacker, mention_author=False)
    else:
      hacker5 = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to make you `antinuke admin`!")
      await ctx.reply(embed=hacker5)

  @_antinuke.group(name="admin", help="Add your Trusted users for antinuke-admin", invoke_without_command=True,usage="Antinuke admin add/remove")
  @blacklist_check()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  #@commands.has_permissions(administrator=True)
  async def _admin(self, ctx):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_admin.command(name="add", help="Add a user to antinuke-admin",usage="Antinuke admin add <user>")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
#  @commands.has_permissions(administrator=True)
  async def admin_add(self, ctx, user: discord.User):
    data = getConfig(ctx.guild.id)
   # mod = data["mod"]
    admin = data["admin"]
    owner = ctx.guild.owner
    if ctx.author == owner:#if ctx.author == owner:
      if len(admin) == 2:
        hacker = discord.Embed(title="Security Settings!", description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> This server has reached the max no.of `antinuke admins` remove one to add another.",color=0xdbdbdb)
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        if str(user.id) in admin:
          hacker1 = discord.Embed(title="Security Settings!", description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:WhitelistUser:1056918373381971998> **Victim:** {user.mention}\n<:rightshort:1053176997481828452> That user is already an `antinuke admin` in this server! ",color=0xdbdbdb)
          await ctx.reply(embed=hacker1, mention_author=False)
        else:
          admin.append(str(user.id))
          updateConfig(ctx.guild.id, data)
          hacker4 = discord.Embed(color=0xdbdbdb,title="Security Settings!", description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:WhitelistUser:1056918373381971998> **Victim:** {user.mention}\n<:rightshort:1053176997481828452> Successfully added as `antinuke admin` now you can make changes!")
          await ctx.reply(embed=hacker4, mention_author=False)

    else:
      hacker5 = discord.Embed(title="Security Settings!", description=f"** Security Alert!:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> Sorry you can't use this command ask guild owner to make changes!",color=0xdbdbdb)
      await ctx.reply(embed=hacker5)
#########

  @_admin.command(name="remove",help="Remove a user from antinuke admin users",usage="Antinuke admin remove <user>")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  #@commands.has_permissions(administrator=True)
  async def admin_remove(self, ctx, user: discord.User):
    data = getConfig(ctx.guild.id)
    #mod = data["mod"]
    admin = data["admin"]
    owner = ctx.guild.owner
    if ctx.author == owner:#if ctx.author == owner:
      if str(user.id) in admin:
        admin.remove(str(user.id))
        updateConfig(ctx.guild.id, data)
        hacker = discord.Embed(color=0xdbdbdb,title="Security Settings!", description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:WhitelistUser:1056918373381971998> **Victim:** {user.mention}\n<:rightshort:1053176997481828452> Successfully removed from `antinuke admin` now that user can't make changes!")      
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        hacker2 = discord.Embed(color=0xdbdbdb,title="Security Settings!", description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:WhitelistUser:1056918373381971998> **Victim:** {user.mention}\n<:rightshort:1053176997481828452> That user is not a `antinuke admin` in this server! ")  
        await ctx.reply(embed=hacker2, mention_author=False)
    else:
      hacker5 = discord.Embed(title="Security Settings!", description=f"** Security Alert!:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> Sorry you can't use this command ask guild owner to make changes!",color=0xdbdbdb)
      await ctx.reply(embed=hacker5, mention_author=False)

  @_admin.command(name="show", help="Shows list of antinuke-admin users in the server.",usage="Antinuke admin show")
  @blacklist_check()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def admin_show(self, ctx):
      data = getConfig(ctx.guild.id)
      admin = data["admin"]
      if len(admin) == 0:
        hacker = discord.Embed(color=0xdbdbdb,title="Security Settings!", description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:WhitelistRole:1058042681772740629> **Admins:** `No one is there as antinuke admin! in this server.`")
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        embed = discord.Embed(title="Security Settings!", description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:WhitelistRole:1058042681772740629> **Admins:**\n", color=0xdbdbdb)
      for idk in admin:
        embed.description += f"<:1spacer:1056545806943006760><:1spacer:1056545806943006760><:1spacer:1056545806943006760><:1spacer:1056545806943006760><@{idk}> `:` {idk}\n"
      await ctx.reply(embed=embed, mention_author=False)
      
  @_admin.command(name="reset", help="removes every user from antinuke-admin database", aliases=["clear"],usage="Antinuke admin reset")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  #@commands.has_permissions(administrator=True)
  async def admin_reset(self, ctx: Context):
    data = getConfig(ctx.guild.id)
    admin = data["admin"]
    if ctx.author == ctx.guild.owner:#if ctx.author.id == ctx.guild.owner_id:
      
      data["admin"] = []
      updateConfig(ctx.guild.id, data)
      hacker = discord.Embed(color=0xdbdbdb,title="Security Settings!", description=f"Successfully Cleared `Antinuke admins` Database!")         
      await ctx.reply(embed=hacker, mention_author=False)
    else:
      hacker5 = discord.Embed(title="Security Settings!", description=f"** Security Alert!:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> Sorry you can't use this command ask guild owner to make changes!",color=0xdbdbdb)
      await ctx.reply(embed=hacker5)
      
  @commands.group(name="Antiban", aliases=["antib"], help="Enables/Disables antiban in your server!", invoke_without_command=True, usage="Antiban Enable/Disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antiban(self, ctx: Context):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_antiban.command(name="enable", help="Server owner should enable antiban for the server!",usage="Antiban Enable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antiban_enable(self, ctx: Context):
    data = getantiban(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    wled = d2["whitelisted"]
    punish = d2["punishment"]
    mod = d2["mod"]
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
      if data == "on":
        embed = discord.Embed( description=f"{WARN} | **Antiban** is already **enabled**")
          
        await ctx.reply(embed=embed, mention_author=False)
      else:
        data = "on"
        updateantiban(ctx.guild.id, data)
        embed2 = discord.Embed(description=f"{TICK} | Successfully Enabled **Antiban**")
        await ctx.reply(embed=embed2, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)

  @_antiban.command(name="disable", help="You can disable antiban for your server using this command", aliases=["off"],usage="Antiban disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antiban_disable(self, ctx: Context):
        
    data = getantiban(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
  
      if data == "off":
        emb = discord.Embed(description=f"{WARN} | **Antiban** is already **disabled**")
        await ctx.reply(embed=emb, mention_author=False)
      else:
        data = "off"
        updateantiban(ctx.guild.id, data)
        final = discord.Embed(description=f"{TICK} | Successfully Disabled **Antiban**")
        await ctx.reply(embed=final, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)
#antikick
  @commands.group(name="Antikick", aliases=["antik"], help="Enables/Disables antikick in your server!", invoke_without_command=True, usage="Antikick Enable/Disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antikick(self, ctx: Context):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_antikick.command(name="enable", help="Server owner should enable antikick for the server!",usage="Antikick Enable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antikick_enable(self, ctx: Context):
    data = getantikick(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    wled = d2["whitelisted"]
    punish = d2["punishment"]
    mod = d2["mod"]
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
      if data == "on":
        embed = discord.Embed( description=f"{WARN} | **Antikick** is already **enabled**")
          
        await ctx.reply(embed=embed, mention_author=False)
      else:
        data = "on"
        updateantikick(ctx.guild.id, data)
        embed2 = discord.Embed(description=f"{TICK} | Successfully Enabled **Antikick**")
        await ctx.reply(embed=embed2, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)

  @_antikick.command(name="disable", help="You can disable antikick for your server using this command", aliases=["off"],usage="Antikick disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antikick_disable(self, ctx: Context):
        
    data = getantikick(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
  
      if data == "off":
        emb = discord.Embed(description=f"{WARN} | **Antikick** is already **disabled**")
        await ctx.reply(embed=emb, mention_author=False)
      else:
        data = "off"
        updateantikick(ctx.guild.id, data)
        final = discord.Embed(description=f"{TICK} | Successfully Disabled **Antikick**")
        await ctx.reply(embed=final, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)
#antiguild#
  @commands.group(name="Antiguild", aliases=["antig"], help="Enables/Disables antiguild in your server!", invoke_without_command=True, usage="Antiguild Enable/Disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antiguild(self, ctx: Context):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_antiguild.command(name="enable", help="Server owner should enable antiguild for the server!",usage="Antiguild Enable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antiguild_enable(self, ctx: Context):
    data = getantiguild(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    wled = d2["whitelisted"]
    punish = d2["punishment"]
    mod = d2["mod"]
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
      if data == "on":
        embed = discord.Embed( description=f"{WARN} | **AntiGuild** is already **enabled**")
          
        await ctx.reply(embed=embed, mention_author=False)
      else:
        data = "on"
        updateantiguild(ctx.guild.id, data)
        embed2 = discord.Embed(description=f"{TICK} | Successfully Enabled **AntiGuild**")
        await ctx.reply(embed=embed2, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)

  @_antiguild.command(name="disable", help="You can disable antiguild for your server using this command", aliases=["off"],usage="Antiguild disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antiguild_disable(self, ctx: Context):
        
    data = getantiguild(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
  
      if data == "off":
        emb = discord.Embed(description=f"{WARN} | **AntiGuild** is already **disabled**")
        await ctx.reply(embed=emb, mention_author=False)
      else:
        data = "off"
        updateantiguild(ctx.guild.id, data)
        final = discord.Embed(description=f"{TICK} | Successfully Disabled **AntiGuild**")
        await ctx.reply(embed=final, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)
#antirole#
  @commands.group(name="Antirole", aliases=["antir"], help="Enables/Disables antirole in your server!", invoke_without_command=True, usage="Antirole Enable/Disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antirole(self, ctx: Context):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_antirole.command(name="enable", help="Server owner should enable antirole for the server!",usage="Antirole Enable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antirole_enable(self, ctx: Context):
    data = getantirole(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    wled = d2["whitelisted"]
    punish = d2["punishment"]
    mod = d2["mod"]
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
      if data == "on":
        embed = discord.Embed( description=f"{WARN} | **AntiRole** is already **enabled**")
          
        await ctx.reply(embed=embed, mention_author=False)
      else:
        data = "on"
        updateantirole(ctx.guild.id, data)
        embed2 = discord.Embed(description=f"{TICK} | Successfully Enabled **AntiRole**")
        await ctx.reply(embed=embed2, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)

  @_antirole.command(name="disable", help="You can disable antirole for your server using this command", aliases=["off"],usage="Antirole disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antirole_disable(self, ctx: Context):
        
    data = getantirole(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
  
      if data == "off":
        emb = discord.Embed(description=f"{WARN} | **AntiRole** is already **disabled**")
        await ctx.reply(embed=emb, mention_author=False)
      else:
        data = "off"
        updateantirole(ctx.guild.id, data)
        final = discord.Embed(description=f"{TICK} | Successfully Disabled **AntiRole**")
        await ctx.reply(embed=final, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)
#antichannel
  @commands.group(name="Antichannel", aliases=["antich","antic"], help="Enables/Disables antiban in your server!", invoke_without_command=True, usage="Antichannel Enable/Disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antichannel(self, ctx: Context):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_antichannel.command(name="enable", help="Server owner should enable antichammel for the server!",usage="Antichannel Enable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antichannel_enable(self, ctx: Context):
    data = getantich(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    wled = d2["whitelisted"]
    punish = d2["punishment"]
    mod = d2["mod"]
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
      if data == "on":
        embed = discord.Embed( description=f"{WARN} | **AntiChannel** is already **enabled**")
          
        await ctx.reply(embed=embed, mention_author=False)
      else:
        data = "on"
        updateantich(ctx.guild.id, data)
        embed2 = discord.Embed(description=f"{TICK} | Successfully Enabled **AntiChannel**")
        await ctx.reply(embed=embed2, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)

  @_antichannel.command(name="disable", help="You can disable antichannel for your server using this command", aliases=["off"],usage="Antichannel disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antichannel_disable(self, ctx: Context):
        
    data = getantich(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
  
      if data == "off":
        emb = discord.Embed(description=f"{WARN} | **AntiChannel** is already **disabled**")
        await ctx.reply(embed=emb, mention_author=False)
      else:
        data = "off"
        updateantich(ctx.guild.id, data)
        final = discord.Embed(description=f"{TICK} | Successfully Disabled **AntiChannel**")
        await ctx.reply(embed=final, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)
#antiemoji#
  @commands.group(name="Antiemoji", aliases=["antiemo"], help="Enables/Disables antiemoji in your server!", invoke_without_command=True, usage="Antiemoji Enable/Disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antiemoji(self, ctx: Context):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_antiemoji.command(name="enable", help="Server owner should enable antiemoji for the server!",usage="Antiemoji Enable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antiemoji_enable(self, ctx: Context):
    data = getantiemo(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    wled = d2["whitelisted"]
    punish = d2["punishment"]
    mod = d2["mod"]
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
      if data == "on":
        embed = discord.Embed( description=f"{WARN} | **AntiEmoji** is already **enabled**")
          
        await ctx.reply(embed=embed, mention_author=False)
      else:
        data = "on"
        updateantiemo(ctx.guild.id, data)
        embed2 = discord.Embed(description=f"{TICK} | Successfully Enabled **AntiEmoji**")
        await ctx.reply(embed=embed2, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)

  @_antiemoji.command(name="disable", help="You can disable antiemoji for your server using this command", aliases=["off"],usage="Antiemoji disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antiemoji_disable(self, ctx: Context):
        
    data = getantiemo(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
  
      if data == "off":
        emb = discord.Embed(description=f"{WARN} | **AntiEmoji** is already **disabled**")
        await ctx.reply(embed=emb, mention_author=False)
      else:
        data = "off"
        updateantiemo(ctx.guild.id, data)
        final = discord.Embed(description=f"{TICK} | Successfully Disabled **AntiEmoji**")
        await ctx.reply(embed=final, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)
#antisticker#
  @commands.group(name="Antisticker", aliases=["antistick"], help="Enables/Disables antisticker in your server!", invoke_without_command=True, usage="Antisticker Enable/Disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antisticker(self, ctx: Context):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_antisticker.command(name="enable", help="Server owner should enable antisticker for the server!",usage="Antisticker Enable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antisticker_enable(self, ctx: Context):
    data = getantisticker(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    wled = d2["whitelisted"]
    punish = d2["punishment"]
    mod = d2["mod"]
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
      if data == "on":
        embed = discord.Embed( description=f"{WARN} | **AntiSticker** is already **enabled**")
          
        await ctx.reply(embed=embed, mention_author=False)
      else:
        data = "on"
        updateantisticker(ctx.guild.id, data)
        embed2 = discord.Embed(description=f"{TICK} | Successfully Enabled **AntiSticker**")
        await ctx.reply(embed=embed2, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)

  @_antisticker.command(name="disable", help="You can disable antisticker for your server using this command", aliases=["off"],usage="Antisticker disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antisticker_disable(self, ctx: Context):
        
    data = getantisticker(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
  
      if data == "off":
        emb = discord.Embed(description=f"{WARN} | **AntiSticker** is already **disabled**")
        await ctx.reply(embed=emb, mention_author=False)
      else:
        data = "off"
        updateantisticker(ctx.guild.id, data)
        final = discord.Embed(description=f"{TICK} | Successfully Disabled **AntiSticker**")
        await ctx.reply(embed=final, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)
#antiprune#
  @commands.group(name="Antiprune", aliases=["antip"], help="Enables/Disables antiprune in your server!", invoke_without_command=True, usage="Antiprune Enable/Disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antiprune(self, ctx: Context):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_antiprune.command(name="enable", help="Server owner should enable antiprune for the server!",usage="Antiprune Enable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antiprune_enable(self, ctx: Context):
    data = getantiprune(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    wled = d2["whitelisted"]
    punish = d2["punishment"]
    mod = d2["mod"]
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
      if data == "on":
        embed = discord.Embed( description=f"{WARN} | **AntiPrune** is already **enabled**")
          
        await ctx.reply(embed=embed, mention_author=False)
      else:
        data = "on"
        updateantiprune(ctx.guild.id, data)
        embed2 = discord.Embed(description=f"{TICK} | Successfully Enabled **AntiPrune**")
        await ctx.reply(embed=embed2, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)

  @_antiprune.command(name="disable", help="You can disable antiprune for your server using this command", aliases=["off"],usage="Antiprune disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antiprune_disable(self, ctx: Context):
        
    data = getantiprune(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
  
      if data == "off":
        emb = discord.Embed(description=f"{WARN} | **AntiPrune** is already **disabled**")
        await ctx.reply(embed=emb, mention_author=False)
      else:
        data = "off"
        updateantiprune(ctx.guild.id, data)
        final = discord.Embed(description=f"{TICK} | Successfully Disabled **AntiPrune**")
        await ctx.reply(embed=final, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)
#antipings#
  @commands.group(name="Antiping", aliases=["antipings"], help="Enables/Disables antiping in your server!", invoke_without_command=True, usage="Antiping Enable/Disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antiping(self, ctx: Context):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_antiping.command(name="enable", help="Server owner should enable antiping for the server!",usage="Antiping Enable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antiping_enable(self, ctx: Context):
    data = getantiping(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    wled = d2["whitelisted"]
    punish = d2["punishment"]
    mod = d2["mod"]
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
      if data == "on":
        embed = discord.Embed( description=f"{WARN} | **AntiPing** is already **enabled**")
          
        await ctx.reply(embed=embed, mention_author=False)
      else:
        data = "on"
        updateantiping(ctx.guild.id, data)
        embed2 = discord.Embed(description=f"{TICK} | Successfully Enabled **AntiPing**")
        await ctx.reply(embed=embed2, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)

  @_antiping.command(name="disable", help="You can disable antiping for your server using this command", aliases=["off"],usage="Antiping disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antiping_disable(self, ctx: Context):
        
    data = getantiping(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
  
      if data == "off":
        emb = discord.Embed(description=f"{WARN} | **Antiping** is already **disabled**")
        await ctx.reply(embed=emb, mention_author=False)
      else:
        data = "off"
        updateantiping(ctx.guild.id, data)
        final = discord.Embed(description=f"{TICK} | Successfully Disabled **AntiPing**")
        await ctx.reply(embed=final, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)
#antiintig#
  @commands.group(name="Antiintigration", aliases=["antiintig"], help="Enables/Disables antiintigration in your server!", invoke_without_command=True, usage="Antiintigration Enable/Disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antiintigration(self, ctx: Context):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_antiintigration.command(name="enable", help="Server owner should enable antiintigration for the server!",usage="Antiintigration Enable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antiintigration_enable(self, ctx: Context):
    data = getantiintig(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    wled = d2["whitelisted"]
    punish = d2["punishment"]
    mod = d2["mod"]
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
      if data == "on":
        embed = discord.Embed( description=f"{WARN} | **AntiIntigration** is already **enabled**")
          
        await ctx.reply(embed=embed, mention_author=False)
      else:
        data = "on"
        updateantiintig(ctx.guild.id, data)
        embed2 = discord.Embed(description=f"{TICK} | Successfully Enabled **AntiIntigration**")
        await ctx.reply(embed=embed2, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)

  @_antiintigration.command(name="disable", help="You can disable antiintigration for your server using this command", aliases=["off"],usage="Antiintigration disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antiintigration_disable(self, ctx: Context):
        
    data = getantiintig(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
  
      if data == "off":
        emb = discord.Embed(description=f"{WARN} | **AntiIntigration** is already **disabled**")
        await ctx.reply(embed=emb, mention_author=False)
      else:
        data = "off"
        updateantiintig(ctx.guild.id, data)
        final = discord.Embed(description=f"{TICK} | Successfully Disabled **AntiIntigration**")
        await ctx.reply(embed=final, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)
#antiwebhook#
  @commands.group(name="Antiwebhook", aliases=["antiwebh"], help="Enables/Disables antiwebhook in your server!", invoke_without_command=True, usage="Antiwebhoom Enable/Disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antiwebhook(self, ctx: Context):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_antiwebhook.command(name="enable", help="Server owner should enable antiban for the server!",usage="Antiwebhook Enable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antiwebhook_enable(self, ctx: Context):
    data = getantiwebh(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    wled = d2["whitelisted"]
    punish = d2["punishment"]
    mod = d2["mod"]
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
      if data == "on":
        embed = discord.Embed( description=f"{WARN} | **AntiWebhook** is already **enabled**")
          
        await ctx.reply(embed=embed, mention_author=False)
      else:
        data = "on"
        updateantiwebh(ctx.guild.id, data)
        embed2 = discord.Embed(description=f"{TICK} | Successfully Enabled **AntiWebhook**")
        await ctx.reply(embed=embed2, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)

  @_antiwebhook.command(name="disable", help="You can disable antiwebhook for your server using this command", aliases=["off"],usage="Antiwebhook disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antiwebhook_disable(self, ctx: Context):
        
    data = getantiwebh(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    admin = d2["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
  
      if data == "off":
        emb = discord.Embed(description=f"{WARN} | **AntiWebhook** is already **disabled**")
        await ctx.reply(embed=emb, mention_author=False)
      else:
        data = "off"
        updateantiwebh(ctx.guild.id, data)
        final = discord.Embed(description=f"{TICK} | Successfully Disabled **AntiWebhook**")
        await ctx.reply(embed=final, mention_author=False)
    else:
      Sputnik = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to permit you `antinuke admin`!")
      await ctx.reply(embed=Sputnik, mention_author=False)

  @commands.group(name="Logging", aliases=["log", "audit"], help="Enables/Disables audit in your server!", invoke_without_command=True, usage="Audit channel add/remove/list")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _logging(self, ctx: Context):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_logging.group(name="channel", aliases=["ch"], help="Add a logging channel .", invoke_without_command=True,usage="Logging channel add/remove")
  @blacklist_check()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  #@commands.has_permissions(administrator=True)
  async def _channel(self, ctx):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)
      
  @_channel.command(name="add", help="Add a channel as logging channel",usage="Audit channel add <channel>")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  #@commands.has_permissions(administrator=True)
  async def channel_add(self, ctx, c: discord.TextChannel):
    data = getConfig(ctx.guild.id)
    lug = data["logChannel"]
    owner = ctx.guild.owner
    admin = data["admin"]
    if str(ctx.author.id) in admin or ctx.author == owner:#if ctx.author == owner:
      if len(lug) == 1:
        hacker = discord.Embed(description=f"{CROSS} | Sorry this server has already an existing logging channel!")
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        if str(c.id) in lug:
          hacker1 = discord.Embed(description=f"{WARN} | That channel is already a default logging channel.")          
          await ctx.reply(embed=hacker1, mention_author=False)
        else:
          lug.append(str(c.id))
          updateConfig(ctx.guild.id, data)
          hacker4 = discord.Embed(description=f"{TICK} | Successfully Added {c.mention} as logging channel! ")
          await ctx.reply(embed=hacker4, mention_author=False)

    else:
      hacker5 = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to make you `antinuke admin`!")
      await ctx.reply(embed=hacker5)

  @_channel.command(name="remove", help="Remove a channel from logging",usage="Audit channel remove remove <channel>")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
#  @commands.has_permissions(administrator=True)
  async def channel_remove(self, ctx, c: discord.TextChannel):
    data = getConfig(ctx.guild.id)
    lug = data["logChannel"]
    admin = data["admin"]
    owner = ctx.guild.owner
    if str(ctx.author.id) in admin or ctx.author == owner:#if ctx.author == owner:
      if str(c.id) in lug:
        lug.remove(str(c.id))
        updateConfig(ctx.guild.id, data)
        hacker = discord.Embed(description=f"{TICK} | Successfully Removed {c.mention} From My Logging!")      
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        hacker2 = discord.Embed(description=f"{CROSS} | This channel is not a logging channel!.")  
        await ctx.reply(embed=hacker2, mention_author=False)
    else:
      hacker5 = discord.Embed(description=f"{WARN} | Sorry you can't use this command ask guild owner to make you `antinuke admin`!")
      await ctx.reply(embed=hacker5, mention_author=False)

  @_channel.command(name="show", help="Shows list of logging channel.",usage="Audit channel show")
  @blacklist_check()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def channel_show(self, ctx):
      #data = getConfig(ctx.guild.id)
      data = getConfig(ctx.guild.id)
      admin = data["admin"]
      lug = data["logChannel"]
     # if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
     # wled = data["whitelisted"]
      if len(lug) == 0:
        hacker = discord.Embed(description=f"{WARN} | No logging channel found!")
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        embed = discord.Embed(description="Logging channel for this server is\n")
      for idk in lug:
        embed.description += f"<#{idk}> | ID: {idk}\n"
      await ctx.reply(embed=embed, mention_author=False)