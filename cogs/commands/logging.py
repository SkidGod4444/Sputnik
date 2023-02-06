import discord, json
from discord.ext import commands
from core import Cog, Sputnik, Context
from utils.Tools import *
#client = Sputnik()
#############LUND LELO MADARCHOD######
arrow = "<:aaArrow:1068097808269320232>"
msg = "<:aaMsg:1068102062031765575>"
miniArrow = "<:aaMiniArrow:1068853253636366406>"
blank = "<:aaJaduEmo:1068098084501995591>"
mem = "<:aaProfile:1068097557978431538>"
bell = "<:aaGhanta:1068101423272837203>"
#############SABKI MAA KA BHOSDA######
class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    
    

    @commands.Cog.listener()
    async def on_member_join(self, member):
      data = getLogger(member.guild.id)
      x = data["channel"]
      if x != "":
        channel = self.bot.get_channel(int(x))
        member1 = int(member.created_at.timestamp())
        embed = discord.Embed(title=f"{bell} A member has joined this server.", description=f"{mem} {member.mention}\n{blank}{miniArrow} {member.id}\n{blank}{miniArrow} Account created at <t:{member1}:D>", color=0x00ff1b)
        embed.timestamp = discord.utils.utcnow()
        embed.set_footer(text="JOINED")
        embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar}")
        embed.set_thumbnail(url=f"{member.avatar}")
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
      data = getLogger(member.guild.id)
      x = data["channel"]
      if x != "":
        channel = self.bot.get_channel(int(x))
        member1 = int(member.created_at.timestamp())
        embed = discord.Embed(title=f"{bell} A member is no longer in this server.", description=f"{mem} {member.mention}\n{blank}{miniArrow} {member.id}\n{blank}{miniArrow} Account created at <t:{member1}:D>", color=0xff0000)
        embed.timestamp = discord.utils.utcnow()
        embed.set_footer(text="LEFT")
        embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar}")
        embed.set_thumbnail(url=f"{member.avatar}")
        await channel.send(embed=embed)
          
    # CHANNEL LOGGING

    @commands.Cog.listener()
    async def on_guild_channel_create(self,  channel):
      data = getLogger(channel.guild.id)
      x = data["channel"]
      if x != "":
        c = self.bot.get_channel(int(x))
        embed = discord.Embed(description=f"{bell} A channel has been created", color = 0x00ff1b)
        embed.add_field(name=f"{arrow} Name:", value=f"{blank}{miniArrow} {channel.name} (ID: {channel.id})")
        embed.add_field(name=f"{arrow} Position:", value=f"{blank}{miniArrow} {channel.position}")
        embed.add_field(name=f"{arrow} Category:", value=f"{blank}{miniArrow} {channel.category} (ID: {channel.category.id})")
        embed.set_footer(text="CHANNEL CREATED")
        embed.timestamp = discord.utils.utcnow()
        if c:
          await c.send(embed=embed)
          
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
      data = getLogger(channel.guild.id)
      x = data["channel"]
      if x != "":
        c = self.bot.get_channel(int(x))
        embed = discord.Embed(description=f"{bell} A channel has been created", color = 0xff0000)
        embed.add_field(name=f"{arrow} Name:", value=f"{blank}{miniArrow} {channel.name} (ID: {channel.id})")
        embed.add_field(name=f"{arrow} Position:", value=f"{blank}{miniArrow} {channel.position}")
        embed.set_footer(text="CHANNEL DELETED")
        embed.timestamp = discord.utils.utcnow()
        if c:
          await c.send(embed=embed)
    # ROLE LOGGING
    
    @commands.Cog.listener()
    async def on_guild_role_create(self, ctx, role):
        data = getConfig(ctx.guild.id)
        x = data["logChannel"]
        if x == None:
          return
        else:  
          channel = self.bot.get_channel(x)
          embed = discord.Embed(description=f"New role ({role.mention}) has been Created", color=0x00FFE4)
          embed.add_field(name="Name", value=f"{role.name} (ID: {role.id})")
          embed.add_field(name="Color", value=f"{role.colour}")
          embed.add_field(name="Postion", value=f"{role.position}")
          embed.set_footer(text="ROLE CREATE")
          embed.timestamp = discord.utils.utcnow()
          await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_delete(self, ctx, role):
        data = getConfig(ctx.guild.id)
        x = data["logChannel"]
        if x == None:
          return
        else:  
          channel = self.bot.get_channel(x)
          embed = discord.Embed(description=f"Role ({role.mention}) has been Deleted", color=0x00FFE4)
          embed.add_field(name="Name", value=f"{role.name} (ID: {role.id})")
          embed.add_field(name="Color", value=f"{role.colour}")
          embed.add_field(name="Postion", value=f"{role.position}")
          embed.set_footer(text="ROLE DELETE")
          embed.timestamp = discord.utils.utcnow()
          await channel.send(embed=embed)

    # BAN AND UNBAN
    @commands.Cog.listener()
    async def on_member_ban(self, ctx, member):
        data = getConfig(ctx.guild.id)
        x = data["logChannel"]
        if x == None:
          return
        else:  
          channel = self.bot.get_channel(x)
          embed = discord.Embed(description="Member has been unbanned from this server.",color=0x00FFE4)
          embed.add_field(name="User", value=f"{member.name}")
          embed.set_author(name=f"{member.name}#{member.discriminator}")
          embed.timestamp = discord.utils.utcnow()
          await channel.send(embed=embed)

        
    @commands.Cog.listener()
    async def on_member_unban(self, ctx, member):
        data = getConfig(ctx.guild.id)
        x = data["logChannel"]
        if x == None:
          return
        else:  
          channel = self.bot.get_channel(x)
          embed = discord.Embed(description="Member has been banned from this server.",color=0x00FFE4)
          embed.add_field(name="User", value=f"{member.name}")
          embed.set_author(name=f"{member.name}#{member.discriminator}")
          embed.timestamp = discord.utils.utcnow()
          await channel.send(embed=embed)


        
    # EMOJI CREATE AND EMOJI REMOVE
    @commands.Cog.listener()
    async def on_guild_emoji_create(self, ctx, emoji):
        data = getConfig(ctx.guild.id)
        x = data["logChannel"]
        if x == None:
          return
        else:  
          channel = self.bot.get_channel(x)
          embed = discord.Embed(description=f"Emoji ({emoji}) has been added.", color=0x00FFE4)
          embed.set_footer(text="EMOJI CREATE")
          embed.timestamp = discord.utils.utcnow()
          await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_emoji_remove(self, ctx, emoji):
        data = getConfig(ctx.guild.id)
        x = data["logChannel"]
        if x == None:
          return
        else:  
          channel = self.bot.get_channel(x)
          embed = discord.Embed(description=f"Emoji ({emoji}) has been deleted.", color=0x00FFE4)
          embed.set_footer(text="EMOJI DELETE")
          embed.timestamp = discord.utils.utcnow()
          await channel.send(embed=embed)
