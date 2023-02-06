from __future__ import annotations
from discord.ext import commands
from utils.Tools import *
from utils.config import OWNER_IDS, No_Prefix
import json, discord
import typing
from typing import Optional
class UniversalBan(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.owner_ids = OWNER_IDS

  @commands.group(name="addbotowner", help="let's you add someone in blacklist", aliases=["abo","bo"])
  @commands.is_owner()
  async def addbotowner(self, ctx):
    if ctx.invoked_subcommand is None:
      with open("2ndbotowners.json") as file:
                addbotowner = json.load(file)
                embed = discord.Embed(
                title=f"{len(addbotowner['ids'])} blacklisted!",
                description=f"{', '.join(str(id) for id in addbotowner['ids'])}"
            )
                await ctx.reply(embed=embed, mention_author=False)

  @addbotowner.command(name="to")
  @commands.is_owner()
  async def addbotowner_to(self, ctx, member: discord.Member):
    try:
      with open('2ndbotowners.json', 'r') as lund:
        addbotowner = json.load(lund)
        if str(member.id) in addbotowner["ids"]:
          embed = discord.Embed(title="Error!", description=f"{member.name} is already blacklisted", color=0xdbdbdb)
          await ctx.reply(embed=embed, mention_author=False)
        else:
          give_unb(member.id)
          embed = discord.Embed(title="Blacklisted", description=f" Successfully Blacklisted {member.name}", color=0xdbdbdb)
          with open("2ndbotowners.json") as file:
              addbotowner = json.load(file)
              embed.set_footer(
                text=f"There are now {len(addbotowner['ids'])} users in the blacklist"
            )
              await ctx.reply(embed=embed, mention_author=False)
    except:
              embed = discord.Embed(
                title="Error!",
                description=f"**An Error Occurred**",
                color=0xdbdbdb
            )
              
              await ctx.reply(embed=embed, mention_author=False)