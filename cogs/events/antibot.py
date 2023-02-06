import discord
import os
import datetime
from core import Sputnik, Cog
from discord.ext import commands
from utils.Tools import *

class antibot(Cog):
    def __init__(self, client: Sputnik):
      self.client = client
      #print(f"Successfully loaded {client.user.name} AntiBot!")

    @commands.Cog.listener()
    async def on_member_join(self, member) -> None:
      try:
        data = getConfig(member.guild.id)
        anti = getantibot(member.guild.id)
        punish = data["abotpunish"]
        wled = data["whitelisted"]
        wl = data["botwl"]
        guild = member.guild
        owner = guild.owner
        reason = "Adding Bots | Not Whitelisted"
        async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add):
            if entry.user.id == guild.owner_id:
              return None
            elif str(entry.user.id) in wled or wl or anti == "off":
              return None
            else:
              if punish == "ban":
               if member.bot:
                await member.ban(reason=f"{reason}")
                await guild.ban(entry.user, reason=f"{reason}")
              elif punish == "kick":
               if member.bot:
                 await member.kick(reason=reason)
                 await guild.kick(entry.user, reason=reason)
              elif punish == "none":
               if member.bot:
                 mem = guild.get_member(entry.user.id)
                 await mem.edit(roles=[role for role in mem.roles if not role.permissions.administrator], reason=reason)
              else:
                return

      except Exception as error:
        if isinstance(error, discord.Forbidden):
              return