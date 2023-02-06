import discord
from discord.ext import commands
import datetime
import re
import json
from core import Sputnik, Cog
from utils.Tools import getConfig


class AntiSpam(Cog):
    def __init__(self, client: Sputnik):
        self.client = client
        self.spam_cd_mapping = commands.CooldownMapping.from_cooldown(4, 7, commands.BucketType.member)
        self.spam_punish_cooldown_cd_mapping = commands.CooldownMapping.from_cooldown(1, 10, commands.BucketType.member)
        #print("Cog Loaded: AntiSpam")
    @commands.Cog.listener()    
    async def on_message(self, message):
      if not message.guild:
        return
      mem = message.author
      invite_regex = re.compile(r"(?:https?://)?discord(?:app)?\.(?:com/invite|gg)/[a-zA-Z0-9]+/?")
      link_regex = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
      invite_matches = invite_regex.findall(message.content)
      link_matches = link_regex.findall(message.content)
      data = getConfig(message.guild.id)
      antiSpam = data["antiSpam"]
      antiLink = data["antiLink"]
      wled = data["whitelisted"]
      wl = data["spamwl"]
     # punish = data["aspampunish"]
      

      try:
                if antiSpam is True:
                  if  str(message.author.id) in wl or wled:
                    return
                  bucket = self.spam_cd_mapping.get_bucket(message)
                  retry = bucket.update_rate_limit()

                  if retry:
                    #punish_cd_bucket = self.spam_punish_cooldown_cd_mapping.get_bucket(message)
                 #   if not punish_cd_bucket.update_rate_limit():
                      if data["aspampunish"] == "kick":
                        await message.author.kick(reason=f"Sputnik | Anti Spam")
                        hacker = discord.Embed(description=f"Successfully Kicked {message.author} For Spamming")
                        hacker.set_author(name=f"{message.author}", icon_url=f"{message.author.avatar}")
                        hacker.set_thumbnail(url =f"{message.author.avatar}")
                        await message.channel.send(embed=hacker)

                      if data["aspampunish"] == "ban":
                        await message.author.ban(reason=f"Sputnik | Anti Spam")
                        hacker1 = discord.Embed(description=f" Successfully Banned {message.author} For Spamming")
                        hacker1.set_author(name=f"{message.author}", icon_url=f"{message.author.avatar}")
                        hacker1.set_thumbnail(url =f"{message.author.avatar}")
                        await message.channel.send(embed=hacker1)

                      if data["aspampunish"] == "none":
                        now = discord.utils.utcnow()
                        await message.author.timeout(now + datetime.timedelta(minutes=30), reason="Sputnik | Anti Spam")
                        hacker2 = discord.Embed(description=f"Successfully Muted {message.author} For Spamming")
                        hacker2.set_author(name=f"{message.author}", icon_url=f"{message.author.avatar}")
                        hacker2.set_thumbnail(url =f"{message.author.avatar}")
                        await message.channel.send(embed=hacker2)

                if antiLink is True:
                    if  str(message.author.id) in wl or wled:
                        return
                    if invite_matches:
                        await message.delete()

                        if data["aspampunish"] == "kick":
                            await message.author.kick(reason=f"Sputnik | Anti Discord Invites")
                            hacker3 = discord.Embed(description=f" Successfully Kicked {message.author} For Sending Invites")
                            hacker3.set_author(name=f"{message.author}", icon_url=f"{message.author.avatar}")
                            hacker3.set_thumbnail(url =f"{message.author.avatar}")
                            await message.channel.send(embed=hacker3)

                        if data["aspampunish"] == "ban":
                            await message.author.ban(reason=f"Sputnik | Anti Discord Invites", delete_message_days=0)
                            hacker4 = discord.Embed(description=f" Successfully Banned {message.author} For Sending Invites")
                            hacker4.set_author(name=f"{message.author}", icon_url=f"{message.author.avatar}")
                            hacker4.set_thumbnail(url =f"{message.author.avatar}")
                            await message.channel.send(embed=hacker4)

                        if data["aspampunish"] == "none":
                             now = discord.utils.utcnow()
                             await message.author.timeout(now + datetime.timedelta(minutes=30), reason="Sputnik | Anti Discord Invites")
                             hacker5 = discord.Embed(description=f"Successfully Muted {message.author} For Sending Discord Server Invites")
                             hacker5.set_author(name=f"{message.author}", icon_url=f"{message.author.avatar}")
                             hacker5.set_thumbnail(url =f"{message.author.avatar}")
                             await message.channel.send(embed=hacker5)
                    if link_matches:
                        if data["aspampunish"] == "kick":
                          await message.author.kick(reason="Sputnik | Anti Link") 
                          hacker6 = discord.Embed(description=f" Successfully Kicked {message.author} For Sending Links")
                          hacker6.set_author(name=f"{message.author}", icon_url=f"{message.author.avatar}")
                          hacker6.set_thumbnail(url =f"{message.author.avatar}") 
                          await message.channel.send(embed=hacker6)



                        if data["aspampunish"] == "ban":
                          await message.author.ban(reason="Sputnik | Anti Link")  
                          hacker7 = discord.Embed(description=f"Successfully Banned {message.author} For Sending Links")
                          hacker7.set_author(name=f"{message.author}", icon_url=f"{message.author.avatar}")
                          hacker7.set_thumbnail(url =f"{message.author.avatar}")  
                          await message.channel.send(embed=hacker7)

                        if data["aspampunish"] == "none":
                          now = discord.utils.utcnow()
                          await message.author.timeout(now + datetime.timedelta(minutes=15), reason="Sputnik | Anti Link")
                          hacker8 = discord.Embed(description=f" Successfully Muted {message.author} For Sending Links")
                          hacker8.set_author(name=f"{message.author}", icon_url=f"{message.author.avatar}")
                          hacker8.set_thumbnail(url =f"{message.author.avatar}") 
                          await message.channel.send(embed=hacker8)
                    else:
                      return
      except Exception as error:
                print(error)