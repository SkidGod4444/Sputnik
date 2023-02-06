import discord, json
from discord.ext import commands
from core import Sputnik, Cog, Context
#############LUND LELO MADARCHOD######
TICK = "<:xxtick:1064599740081246279>"
CROSS = "<:xxcross:1064599805797609494>"
PASS = "0x00ff1b"
FAIL = "0xff0000"
WARN = "<:ellor:1053894610272931950>"
#############SABKI MAA KA BHOSDA######
class Errors(Cog):
  def __init__(self, client:Sputnik):
    self.client = client
   # print(f"Cog Loaded: {self.__class__.__name__}")

  @commands.Cog.listener()
  async def on_command_error(self, ctx: Context, error):
    with open('blacklist.json', 'r') as f:
      data = json.load(f)
    if isinstance(error, commands.CommandNotFound):
      return
    elif isinstance(error, commands.MissingRequiredArgument):
      await ctx.send_help(ctx.command)
      ctx.command.reset_cooldown(ctx)
    elif isinstance(error, commands.NoPrivateMessage):
      hacker = discord.Embed(description=f"{CROSS} | You Can\'t Use My Commands In Dm(s)", timestamp=ctx.message.created_at)
      hacker.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
      hacker.set_thumbnail(url =f"{ctx.author.avatar}")
      await ctx.reply(embed=hacker)
    elif isinstance(error, commands.TooManyArguments):
      await ctx.send_help(ctx.command)
      ctx.command.reset_cooldown(ctx)

    elif isinstance(error, commands.CommandOnCooldown):
      hacker = discord.Embed(description=f"{WARN} | This Command is on cooldown retry after `{error.retry_after:.2f}` second(s)!", timestamp=ctx.message.created_at)
      #hacker.set_author(name=f"Cooldown!")
    #  hacker.set_thumbnail(url =f"{ctx.author.avatar}")
      await ctx.reply(embed=hacker)
    elif isinstance(error, commands.MaxConcurrencyReached):
      hacker = discord.Embed(description=f"{WARN} |  This Command is already going on, let it finish and retry after!", timestamp=ctx.message.created_at)
    #  hacker.set_author(name=f"Running Command!")
     # hacker.set_thumbnail(url =f"{ctx.author.avatar}")
      await ctx.reply(embed=hacker)
      ctx.command.reset_cooldown(ctx)
    elif isinstance(error, commands.MissingPermissions):
      missing = [
                perm.replace("_", " ").replace("guild", "server").title()
                for perm in error.missing_permissions
            ]
      if len(missing) > 2:
                fmt = "{}, and {}".format(", ".join(missing[:-1]), missing[-1])
      else:
                fmt = " and ".join(missing)
      hacker = discord.Embed(title=f"{WARN} {ctx.author}",description=f" ```You are lacking `{fmt}` permissions to use this command!```", timestamp=ctx.message.created_at)
   #   hacker.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
     # hacker.set_thumbnail(url =f"{ctx.author.avatar}")
      await ctx.reply(embed=hacker)
      ctx.command.reset_cooldown(ctx)

    elif isinstance(error, commands.BadArgument):
      await ctx.send_help(ctx.command)
      ctx.command.reset_cooldown(ctx)

    elif isinstance(error, discord.HTTPException):
      pass
    elif isinstance(error, commands.CommandInvokeError):
      pass
    elif isinstance(error, commands.CheckFailure):
      if str(ctx.author.id) in data["ids"]:
        embed = discord.Embed( description=f"{WARN} | You Are Blacklisted From Using My Commands.\n Join our [Support Server](https://discord.gg/ZrcXSdnM46) to appeal.")
        await ctx.reply(embed=embed, mention_author=False)
