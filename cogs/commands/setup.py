from __future__ import annotations
from discord.ext import commands
from core import Cog, Sputnik, Context
import discord
from utils import *
from utils.Tools import *
from discord.ui import Button, View
import datetime
from typing import Optional
client = Sputnik()
#############LUND LELO MADARCHOD######
TICK = "<:xxtick:1064599740081246279>"
CROSS = "<:xxcross:1064599805797609494>"
PASS = "0x00ff1b"
FAIL = "0xff0000"
WARN = "<:ellor:1053894610272931950>"
#############SABKI MAA KA BHOSDA######
class verificationb(discord.ui.View):
  def __init__(self):
    super().__init__(timeout=None)

  @discord.ui.button(label='Verify', style=discord.ButtonStyle.success, custom_id=f'verifybutton')
  async def button_callback(self, interaction: discord.Interaction,button):
    await interaction.user.send(f"failed to verify")
    @discord.ui.button2(label='Help', style=discord.ButtonStyle.grey, custom_id=f'helpbutton')
    async def button2_callback(self, interaction: discord.Interaction,button):
      await interaction.response.send_message(f"failed to verify", ephemeral=True)
class Setup(Cog):
  """Shows a list of commands regarding antinuke"""
  def __init__(self, client:Sputnik):
    self.client = client
      
  @commands.group(name="Setup", aliases=["set", "setups"], help="Setups any commands in your server!", invoke_without_command=True, usage="setup <command> <value>")
  @blacklist_check()
  @ignore_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _setup(self, ctx: Context):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_setup.command(name="verification", help="Server owner should enable antinuke for the server!",usage="Antinuke Enable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def setup_verification(self, ctx, verification_channel:discord.TextChannel, verified_role:discord.Role):
    with open("verification.json", "r") as f:
      idk = json.load(f)
      mm = {"channel": verification_channel.id, "role": verified_role.id}
      idk[str(ctx.guild.id)] = mm
      await ctx.reply(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"successfully setuped"))
      await verification_channel.send(embed=discord.Embed(color=discord.Colour(0x2f3136), description=f"To access {ctx.guild.name}, you need to pass the verification first, Press the verify button below.", title=f"Verification").set_footer(text="Powered by Universal Sec™"), view=verificationb())
      with open('verification.json', 'w') as f:
        json.dump(idk, f, indent=4)