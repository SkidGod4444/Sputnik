import os
import discord
import aiohttp
from discord.ext import commands, tasks
from discord.colour import Color
import json
import random
from discord.ui import Button, View
from utils.Tools import *
#############LUND LELO MADARCHOD######
TICK = "<:xxtick:1064599740081246279>"
CROSS = "<:xxcross:1064599805797609494>"
PASS = "0x00ff1b"
FAIL = "0xff0000"
WARN = "<:ellor:1053894610272931950>"
#############SABKI MAA KA BHOSDA######
#from utils.checks import getConfig, updateConfig

#https://cdn.discordapp.com/attachments/1027593292642275418/1028516662221226024/Proton.png

class Join(commands.Cog):
    def __init__(self, client):
        self.client = client

    

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
          data = getConfig(guild.id)
          key = "".join(random.choice("aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStT0123456789.+&_-*#$@!?:%=") for _ in range(8))
          data['backupkey'] = key
          updateConfig(guild.id, data)
          embed = discord.Embed(
            description=f"{TICK} `Sputnik` has been added to `{guild.name}` successfully!\n<:1spacer:1056545806943006760>\nYou can setup the whole bot in your server by  doing; **[s!help](https://discord.gg/sputnikbot)** and following the needed steps",
            
          )
          embed.set_author(
            name="Thnkx for inviting Sputnik!"
          )
          
          embed.add_field(
            name=f"OwnerKey - `{key}`",
            value="You can add yourself as a bot owner by using this Ownerkey\nIt will be usefull in future if you loose your server ownership\n**NOTE:** The Ownerkey is valid till the bot is in your server!",
            inline=False
          ) 
          
          skidgod = Button(label='Support Server', style=discord.ButtonStyle.link, url='https://discord.gg/ZrcXSdnM46')
         # web = Button(label='Website', style=discord.ButtonStyle.link, url='https://discord.gg/3YmDAzbuRR')
          docs = Button(label='Documentation',style=discord.ButtonStyle.link,url='https://discord.gg/ZrcXSdnM46')
       # premium = Button(label='Premium',style=discord.ButtonStyle.link,url='https://discord.gg/3YmDAzbuRR')
       # vote = Button(label='Vote Me', style=discord.ButtonStyle.link, url='https://discord.com/oauth2/authorize?client_id=1021416292185546854&permissions=2113268958&scope=bot')
          view = View()
         # view.add_item(b)
          view.add_item(skidgod) 
          #view.add_item(web)
          view.add_item(docs)          
          await guild.owner.send(embed=embed, view=view)
       #   himanshu = discord.Embed(
      #      title="Security!",description=f"Key - `{key}`\n<:1spacer:1056545806943006760>\nYou must keep this key safe this will be usefull in future!",
          #  color=0xdbdbdb
         # )
      

                   
         # await guild.owner.send(embed=himanshu)


    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
          data = getConfig(guild.id)
          key = "none"
          data['backupkey'] = key
          updateConfig(guild.id, data)
          embed = discord.Embed(
            title="It looks like someone has removed Sputnik!",description=f"{WARN} `Sputnik` has been removed from `{guild.name}`\n<:1spacer:1056545806943006760>\nIf it was a mistake then re-add `Sputnik` to your server\nDon't worry you can restore all the settings by just re-adding!\nYou can also read the **[Documentation](https://discord.gg/ZrcXSdnM46)** if your want to know more about."
          )
          skidgod = Button(label='Support Server', style=discord.ButtonStyle.link, url='https://discord.gg/ZrcXSdnM46')
         # web = Button(label='Website', style=discord.ButtonStyle.link, url='https://discord.gg/3YmDAzbuRR')
          docs = Button(label='Documentation',style=discord.ButtonStyle.link,url='https://discord.gg/ZrcXSdnM46')
       # premium = Button(label='Premium',style=discord.ButtonStyle.link,url='https://discord.gg/3YmDAzbuRR')
       # vote = Button(label='Vote Me', style=discord.ButtonStyle.link, url='https://discord.com/oauth2/authorize?client_id=1021416292185546854&permissions=2113268958&scope=bot')
          view = View()
         # view.add_item(b)
          view.add_item(skidgod) 
          #view.add_item(web)
          view.add_item(docs)          
          await guild.owner.send(embed=embed,view=view)
    
