import os          
from core.Sputnik import Sputnik
import asyncio, time, aiohttp, json
import jishaku, cogs
import psutil
import discord
from discord.ext import commands
from discord import app_commands
import traceback
from discord.ui import Button, View
from discord.ext.commands import Context


os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"


client = Sputnik()
#tree = client.tree

      

async def Sputnik_stats():
    while True:
        servers = len(client.guilds)
        users = sum(g.member_count for g in client.guilds
                    if g.member_count != None)
        sv_ch = client.get_channel(1069075625425518623)
        users_ch = client.get_channel(1069075662146637884)
        await asyncio.sleep(3000)
        await sv_ch.edit(name="Sputnik Servers : {}".format(servers))
        await users_ch.edit(name="Sputnik Users ; {}".format(users))
      



#class Embed(discord.ui.Modal, title='Embed Configuration'):
   # tit = discord.ui.TextInput(
        #label='Embed Title',
      #  placeholder='Embed title here',
    #)

    #description = discord.ui.TextInput(
        #label='Embed Description',
       # style=discord.TextStyle.long,
      #  placeholder='Embed description optional',
        #required=False,
       # max_length=400,
   # )

    #thumbnail = discord.ui.TextInput(
   #     label='Embed Thumbnail',
       # placeholder='Embed thumbnail here optional',
        ##required=False,
  #  )

    #img = discord.ui.TextInput(
        #label='Embed Image',
       # placeholder='Embed image here optional',
        #required=False,
    #)
#
    #footer = discord.ui.TextInput(
        #label='Embed footer',
        #placeholder='Embed footer here optional',
        #required=False,
   # )

    #async def on_submit(self, interaction: discord.Interaction):
       # embed = discord.Embed(title=self.tit.value, description=self.description.value,color=0x00FFE4)
        #if not self.thumbnail.value is None:
          #embed.set_thumbnail(url=self.thumbnail.value)
        ##if not self.img.value is None:
          #embed.set_image(url=self.img.value)
       # if not self.footer.value is None:
          #embed.set_footer(text=self.footer.value)
        #await interaction.response.send_message(embed=embed)

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)


        traceback.print_tb(error.__traceback__)


      
#@tree.command(name="embed", description="Create A Embed Using Sputnik")
#async def _embed(interaction: discord.Interaction) -> None:
  #await interaction.response.send_modal(Embed())



########################################



async def protect_vanity(guildid):
      start = time.perf_counter()
      with open('vanity.json') as idk:
        code = json.load(idk)
        if code[str(guildid)] != "":
          header = {"Authorization": "Bot MTAzNDQ1MzkzOTkzMzkzNzczNA.GASulU.95KgzwiRyc2_uKXGdbNSpiMwqq2B7wZjx8CvX0", "X-Audit-Log-Reason": "Sputnik | Anti Vanity"}
          async with aiohttp.ClientSession(headers=header) as session:
            jsonn = {"code": code[str(guildid)]}
            async with session.patch(f"https://ptb.discord.com/api/v10/guilds/{guildid}/vanity-url", json=jsonn) as response:
              end = time.perf_counter()
              print(f"{end - start} | {response.status}")
        else:
          return


    
@client.listen("on_guild_update")
async def on_vanity_update(before, after):
  with open("vanity.json", "r") as f:
    data = json.load(f)
  if before.vanity_url_code != after.vanity_url_code:
    await asyncio.gather(*[asyncio.gather(*[asyncio.gather(*[asyncio.gather(*[asyncio.gather(*[asyncio.gather(*[asyncio.gather(*[asyncio.gather(*[asyncio.gather(*[asyncio.gather(*[asyncio.gather(*[asyncio.gather(*[protect_vanity(before.id)])])])])])])])])])])])])
  else:
    return





@client.event
async def on_ready():
    print("Successfully Loaded ...................")
    print(f"Logged in as: {client.user}, Connected to: {len(client.guilds)} guilds with {len(client.users)} users!")
    print(f"{client.user.name} by ~ Himanshu_xD")
    await client.loop.create_task(Sputnik_stats())
    try:
        synced = await client.tree.sync()
        print(f"synced {len(synced)} commands")
    except Exception as e:
        print (e)
      
@client.event
async def on_guild_join(guild):
       # for x in client.guilds:
         if guild.member_count < 1:

          embed = discord.Embed(
            title="It looks like your server is too small!",description=f"<:NotifyBadge:1053153617353396234> `Sputnik` has left your server `{guild.name}`\n<:1spacer:1056545806943006760>\nYou can't add `Sputnik` in below `1` members server sorry for inconvenience!\nIf it was a mistake then re-add `Sputnik` to your server or report it in `Support Server`",
            color=0xff0000
          )
         skidgod = Button(label='Support Server', style=discord.ButtonStyle.link, url='https://discord.gg/ZrcXSdnM46')
 
         view = View()
         
         view.add_item(skidgod) 
                    
         await guild.owner.send(embed=embed,view=view)

          # await guild.owner.send("Cant Join Guild Less Than 30 Member")
         await guild.leave()

 #   
#@client.event
#async def on_member_leave(member):
    #embed = discord.Embed(title="**Sputnik's Advertisement!**", description =f"We offers  the fastest server protection with a powerful **anti-nuke**, **Moderation**, ***`Sputnik`*** can protect your server in multiple ways today!\n<:Category_Sputnik:1061081353506009198> **There are many more FAQs about Sputnik bot must join the below server for more info.**")
    #await member.send(f"- Join for more help!\nhttps://discord.gg/ZrcXSdnM46",embed = embed , mention_author = True)




    
@client.event
async def on_command_completion(context: Context) -> None:

    full_command_name = context.command.qualified_name
    split = full_command_name.split(" | ")
    executed_command = str(split[0])
    me = client.get_channel(1059094189532516443) 
    if context.guild is not None:
        SkidGod = discord.Embed(title="Sputnik's Cmd Logs", description = f"<:urrow:1053243283549204520> **Executor:**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452>[{context.author}](https://discord.com/users/{context.author.id}) | [{context.author.id}](https://discord.com/users/{context.author.id})\n<:urrow:1053243283549204520> **Command Name:**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> *s!{executed_command}*\n<:urrow:1053243283549204520> **Executed Guild:**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> `{context.guild.name}` | `{context.guild.id}`\n<:urrow:1053243283549204520> **Executed Channel:**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> [{context.channel.name}](https://discord.com/channels/{context.guild.id}/{context.channel.id}) | [{context.channel.id}](https://discord.com/channels/{context.guild.id}/{context.channel.id})\n<:tixk:1053178188613820468> **__Command executed without any errors__**").set_footer(text=f"{context.author} Executed s!{executed_command} in {context.guild.name}",icon_url=context.author.avatar).set_thumbnail(url=context.author.avatar)
        await me.send(embed=SkidGod)
    else:
        await me.send(
            f"Executed `{executed_command}` command by `{context.author}` (ID: `{context.author.id}`) in DMs")
#import os
#os.system("pip install flask")
from flask import Flask
from threading import Thread

app = Flask(__name__) 
@app.route('/')
def home():
    return "Sputnik"
def run():
  app.run(host='0.0.0.0',port=8080)
def keep_alive():  
  server=Thread(target=run)
  server.start()
keep_alive()




async def main():
    async with client:
      os.system("clear")
      await client.load_extension("cogs")
      await client.load_extension("jishaku")
      await client.start(os.getenv("token"))
     # await client.start("")

if __name__ == "__main__":
  asyncio.run(main())

#client.start("")