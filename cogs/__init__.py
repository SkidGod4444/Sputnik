from __future__ import annotations
from core import Sputnik

#######<<------CoMMaNDs------>>########

from .commands.help import Help
from .commands.general import General
from .commands.moderation import Moderation
from .commands.A1_Sputnik_v3 import Security
from .commands.setup import Setup
from .commands.autosetup import Autosetup
from .commands.automoderation import Automoderation
from .commands.logging import Logging
from .commands.extra import Extra
from .commands.owner import Owner
from .commands.ignore import Ignore
from .commands.universal_ban import UniversalBan
#<<------EVENTS-------->>########
from .events.antiban import antiban
from .events.antimem import antimem
from .events.antichannel import antichannel
from .events.antiguild import antiguild
from .events.antirole import antirole
from .events.antibot import antibot
from .events.antikick import antikick
from .events.antiprune import antiprune
from .events.antiwebhook import antiwebhook
from .events.antiping import antipinginv
from .events.antiemostick import antiemostick
from .events.antintegration import antintegration
from .events.antispam import AntiSpam
from .events.autoblacklist import AutoBlacklist
from .events.antiemojid import antiemojid
from .events.antiemojiu import antiemojiu

from .events.join import Join
from .events.Errors import Errors
from .events.on_guild import Guild
from .events.ready import ready
from .events.antiupdate import antiupdate
#######<<-------------------->>########

async def setup(bot:Sputnik):
  await bot.add_cog(Help(bot))
  await bot.add_cog(Setup(bot))
  await bot.add_cog(General(bot))
  await bot.add_cog(Moderation(bot))
  await bot.add_cog(Security(bot))
  await bot.add_cog(Automoderation(bot))
  await bot.add_cog(Logging(bot))
  await bot.add_cog(Extra(bot))
  await bot.add_cog(Owner(bot))
  await bot.add_cog(UniversalBan(bot))
  await bot.add_cog(Ignore(bot))
  await bot.add_cog(Autosetup(bot))

#######<<-------------------->>########
  
  await bot.add_cog(antiban(bot))
  await bot.add_cog(antimem(bot))
  await bot.add_cog(antichannel(bot))
  await bot.add_cog(antiguild(bot))
  await bot.add_cog(antirole(bot))
  await bot.add_cog(antibot(bot))
  await bot.add_cog(antikick(bot))
  await bot.add_cog(antiprune(bot))
  await bot.add_cog(antiwebhook(bot))
  await bot.add_cog(antipinginv(bot))
  await bot.add_cog(antiemostick(bot))
  await bot.add_cog(antiupdate(bot))
  await bot.add_cog(antintegration(bot))  
  await bot.add_cog(AntiSpam(bot))
  await bot.add_cog(AutoBlacklist(bot))
  await bot.add_cog(antiemojid(bot))
  await bot.add_cog(antiemojiu(bot))
  await bot.add_cog(Guild(bot))
  await bot.add_cog(Errors(bot))
  await bot.add_cog(Join(bot))
