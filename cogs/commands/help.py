import discord
from discord.ext import commands
from difflib import get_close_matches
from contextlib import suppress
from core import Context
from core.Sputnik import Sputnik
from core.Cog import Cog
from utils.Tools import getConfig
from itertools import chain
import json
from discord.ui import Button, View
#from utils import help as vhelp
from utils.emo import *

client = Sputnik()

class HelpView(discord.ui.Select):
  def __init__(self):
    opts = [discord.SelectOption(label="Security"), 
           discord.SelectOption(label="Moderation"), 
           discord.SelectOption(label="Trusted"), 
           discord.SelectOption(label="General"), 
           discord.SelectOption(label="Extras"), 
          discord.SelectOption(label="Customize"),  
            discord.SelectOption(label="Setup")]
    
    super().__init__(placeholder="Click here to select modules...", max_values=1, min_values=1, options=opts)

  async def callback(self, interaction: discord.Interaction):
      embed_sec = discord.Embed(title=f"Hey", description="Mein Security hu")
      embed_mod = discord.Embed(title=f"Hey", description="Mein Moderation hu")
      embed_trust = discord.Embed(title=f"Hey", description="Mein Trusted hu")
      embed_gen = discord.Embed(title=f"Hey", description="Mein General hu")
      embed_ext = discord.Embed(title=f"Hey", description="Mein Extra hu")
      embed_custom = discord.Embed(title=f"Hey", description="Mein Customized hu")
      embed_set = discord.Embed(title=f"Hey", description="Mein Setup hu")

      if self.values[0] == "Security":
        await interaction.response.send_message(embed=embed_sec, ephemeral=True)
      elif self.values[0] == "Moderation":
        await interaction.response.send_message(embed=embed_mod, ephemeral=True)
      elif self.values[0] == "Trusted":
        await interaction.response.send_message(embed=embed_trust, ephemeral=True)
      elif self.values[0] == "General":
        await interaction.response.send_message(embed=embed_gen, ephemeral=True)
      elif self.values[0] == "Extras":
        await interaction.response.send_message(embed=embed_ext, ephemeral=True)
      elif self.values[0] == "Customize":
        await interaction.response.send_message(embed=embed_custom, ephemeral=True)
      elif self.values[0] == "Setup":
        await interaction.response.send_message(embed=embed_set, ephemeral=True)

class dropdown(discord.ui.View):
  def __init__(self, *, timeout=180):
     super().__init__(timeout=timeout)
     self.add_item(HelpView())
     self.response = None
    

  async def on_timeout(self):
    for child in self.children:
      child.disabled = True
   # await self.response.edit(view=self)


class HelpCommand(commands.HelpCommand):
  async def on_help_command_error(self, ctx, error):
    damn = [commands.CommandOnCooldown, 
           commands.CommandNotFound, discord.HTTPException, 
           commands.CommandInvokeError]
    if not type(error) in damn:
      await self.context.reply(f"Unknown Error Occurred\n{error.original}", mention_author=False)
    else:
      if type(error) == commands.CommandOnCooldown:
        return
      
        return await super().on_help_command_error(ctx, error)

  async def command_not_found(self, string: str) -> None:
    with open('blacklist.json', 'r') as f:
      data = json.load(f)
    if str(self.context.author.id) in data["ids"]:
      embed = discord.Embed(title="<:xross:1053176060759515218> Blacklisted User", description="You Are Blacklisted From Using My Commands.\n<:person:1053178413478838312> **Moderator:** `Auto Detection`\n<:Notification:1053149447506374666> ***Reason:** `Spamming My Commands`", color=0xdbdbdb)
      await self.context.reply(embed=embed, mention_author=True)
    else:
      

      if string in ("oknchhfehheng3g", "oknchhfehheng3g"):
        cog = self.context.bot.get_cog("Antinuke")
        with suppress(discord.HTTPException):
          await self.send_cog_help(cog)
      elif string in ("oknchhfehheng3g"):
        cog = self.context.bot.get_cog("Games")
        with suppress(discord.HTTPException):
          await self.send_cog_help(cog)
      else:
        msg = f"Command `{string}` is not found...\n"
        cmds = (str(cmd) for cmd in self.context.bot.walk_commands())
        mtchs = get_close_matches(string, cmds)
        if mtchs:
          for okaay, okay in enumerate(mtchs, start=1):
            msg += f"Did You Mean: \n`[{okaay}]`. `{okay}`\n"
        embed1 = discord.Embed(color=0x00FFE4,title=f"Command `{string}` is not found...\n",description=f"Did You Mean: \n`[{okaay}]`. `{okay}`\n")
        embed1.set_footer(name="Reminder : Hooks such as <> must not be used when executing commands.")
        return embed1

  
  async def send_bot_help(self, mapping):
    await self.context.typing()
    with open('blacklist.json', 'r') as f:
      bled = json.load(f)
    if str(self.context.author.id) in bled["ids"]:
      embed = discord.Embed(title="<:xross:1053176060759515218> Blacklisted User", description="You Are Blacklisted From Using My Commands.\n<:person:1053178413478838312> **Moderator:** `Auto Detection`\n<:Notification:1053149447506374666> ***Reason:** `Spamming My Commands`", color=0xdbdbdb)
      return await self.context.reply(embed=embed, mention_author=False)
    data = getConfig(self.context.guild.id)
    prefix = data["prefix"]
    perms = discord.Permissions.none()
    perms.read_messages = True
    perms.external_emojis = True
    perms.send_messages = True
    perms.manage_roles = True
    perms.manage_channels = True
    perms.ban_members = True
    perms.kick_members = True
    perms.manage_messages = True
    perms.embed_links = True
    perms.read_message_history = True
    perms.attach_files = True
    perms.add_reactions = True
    perms.administrator = True
    inv = discord.utils.oauth_url(self.context.bot.user.id, permissions=perms)
    embed = discord.Embed(description=f"> For commands & modules help do; **``{prefix}helpcmd <command/module>``**\n> If you need further help pls join our **[Support Server](https://discord.gg/ZrcXSdnM46)**")
    embed.set_footer(text="Thnkx for selecting Sputnik!", icon_url="")
    embed.add_field(name=f"<:xzsetup:1064569930768466030> Command Categories", value="> <:xxsecstar:1064489290786144306> `:` **Security**\n> <:xxtools:1064487743905865789> `:` **Moderation**\n> <:xxhuman:1064487881042837514> `:` **Trusted**\n> <:xxuniverse:1064489201279701062> `:` **General**\n> <:xxburnout:1064489320167251969> `:` **Extras**\n> <:xxbann:1064486880789413940> `:` **Customise**")
    embed.add_field(name=f"<:xzinfinity:1064569881267294248> Sputnik Links",value=f"> **[Invite Sputnik]({inv})** `.` **[Support Server](https://discord.gg/ZrcXSdnM46)** `.` **[Website](https://discord.gg/ZrcXSdnM46)**")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1065214371585867879/1066181111484530749/1674171149881.png")

    embed.set_author(name="Sputnik Help", icon_url="https://media.discordapp.net/attachments/1065214371585867879/1066181111484530749/1674171149881.png")
    embed.timestamp = discord.utils.utcnow()
    button2=discord.ui.Button(label='Page 1',style=discord.ButtonStyle.primary)
    button3=discord.ui.Button(label='Page 2',style=discord.ButtonStyle.primary)
    button0=discord.ui.Button(label='Home',style=discord.ButtonStyle.danger)
    
    view = discord.ui.View()
    view = dropdown()
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button0)
  #  view.add_item(lund)
                             
                             
                             
                             
    

    
        
    



    async def button2_callback(interaction: discord.Interaction):
          embed2 = discord.Embed(description=f'> For commands/modules help do; **``{prefix}helpcmd <command/module>``**\n> **```<> - Required Args, ([]) - Optional Args```**')
          embed2.add_field(name=f"<:xxsecstar:1064489290786144306> . Security - [6]",value=f"`antinuke` , `antinuke <value> [value=enable/disable]` *(Enables/Disables all Antinuke events)*, `antinuke show` , `antinuke punishment set <type> [type=ban,kick,none]` *(sets a particular type for all Antinuke events)* , `antinuke channelclean` , `antinuke roleclean` , `antinuke setvanity`")
      
          embed2.add_field(name=f"<:xxtools:1064487743905865789> . Moderation",value="`softban` ,  `mute` , `unmute` , `kick` , `roleallhumans` , `roleallbots` , `removeallhumans` , `removeallbots` , `warn`  , `ban` , `unban` , `unbanall` , `slowmode` ,  `unslowmode` , `lock` , `unlock`")
      
          embed2.add_field(name=f"<:xxhuman:1064487881042837514> . Trusted - [12]",value="`antinuke admin add <user>` , `antinuke admin remove` , `antinuke admin show` , `antinuke admin reset` , `antinuke mod add` , `antinuke mod remove` , `antinuke mod show` , `antinuke mod reset` , `antinuke whitelist add` , `antinuke whitelist remove` , `antinuke whitelist show` , `antinuke whitelist reset`")
          
      
          embed2.set_author(name="Sputnik Help Page 1/2", icon_url="https://media.discordapp.net/attachments/1065214371585867879/1066181111484530749/1674171149881.png")
      
          embed2.set_footer(text="Reminder : Hooks such as `<>` or `[]` must not be used when executing commands.", icon_url="")
          embed.timestamp = discord.utils.utcnow()
       
      
          await interaction.response.edit_message(embed=embed2)
    async def button3_callback(interaction: discord.Interaction):
          embed3 = discord.Embed(description=f'> For commands/modules help do; **``{prefix}helpcmd <command/module>``**\n> **```<> - Required Args, ([]) - Optional Args```**')

          embed3.add_field(name=f"<:xxuniverse:1064489201279701062> . General",value=f"`afk` , `avatar` , `banner` , `servericon` , `membercount` , `memberstats` , `voting` , `snipe` , `userinfo`")
      
          embed3.add_field(name=f"<:xxburnout:1064489320167251969> . Extras",value=f"`invite` , `serverinfo` , `botinfo` ,  `joined-at` , `note` , `notes` , `trashnotes` , `badges` ")

          embed3.add_field(name=f"<:xxbann:1064486880789413940> . Customise Toggles - [11]",value="`Antiban <value> [value=enable/disable]`, `Antikick <value>`, `Antiguild <value>`, `Antiprune <value>`, `Antiping <value>`, `Antiemoji <value>`, `Antisticker <value>`, `Antirole <value>`, `Antichannel <value>`, `Antiwebhook <value>`, `Antiintig <value>`")

      
          embed3.set_author(name="Sputnik Help Page 2/2", icon_url="https://media.discordapp.net/attachments/1065214371585867879/1066181111484530749/1674171149881.png")
          embed.timestamp = discord.utils.utcnow()      
          embed3.set_footer(text="Reminder : Hooks such as `<>` or `[]` must not be used when executing commands.", icon_url="")
          await interaction.response.edit_message(embed=embed3)
    async def button0_callback(interaction: discord.Interaction):
          
          await interaction.response.edit_message(embed=embed)

    button2.callback =button2_callback
    button3.callback =button3_callback
    button0.callback =button0_callback
    

    await self.context.send(embed=embed, mention_author=False, view = view, delete_after = 200)

    
  async def send_command_help(self, command):
        
    with open('blacklist.json', 'r') as f:
       data = json.load(f)
    if str(self.context.author.id) in data["ids"]:
       embed = discord.Embed(title="<:xross:1053176060759515218> Blacklisted User", description="You Are Blacklisted From Using My Commands.\n<:person:1053178413478838312> **Moderator:** `Auto Detection`\n<:Notification:1053149447506374666> ***Reason:** `Spamming My Commands`")
       await self.context.reply(embed=embed, mention_author=False)
    else:
       hacker = f"{command.help}" if command.help else 'No Description Provided...'
       embed = discord.Embed( title="Here's some help",description=f"<:urrow:1053243283549204520> **[Join Support Server](https://discord.gg/3YmDAzbuRR)** ***[discord.gg/3YmDAzbuRR]***\n<:urrow:1053243283549204520> **[Documentation](https://discord.gg/3YmDAzbuRR)**")
       alias = ' | '.join(command.aliases)

       embed.add_field(name="**Command Category:**", value=f"<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Category:** `{command.cog.qualified_name.title()}`")
       embed.add_field(name="Command Aliases:",value=f"<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Aliases:** `{alias}`" if command.aliases else "<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Aliases:** `No Aliases found!`", inline=False)
       embed.add_field(name="**Command Usage:**", value=f"<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Usage:** `{self.context.prefix}{command.signature}`\n")
       embed.add_field(name="**Command Description:**", value=f"<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Description:** `{hacker}`")
      
       embed.set_footer(text="Reminder : Hooks such as `<>` or `[]` must not be used when executing commands.", icon_url="")
    
       embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/l7vKMv604vRFUX251EGvc9MWNmFqwBYmcF_8IVYRmug/https/cdn.discordapp.com/emojis/1053153617353396234.png")
       await self.context.reply(embed=embed, mention_author=False, delete_after = 60)

  def get_command_signature(self, command: commands.Command) -> str:
        parent = command.full_parent_name
        if len(command.aliases) > 0:
            aliases = ' | '.join(command.aliases)
            fmt = f'[{command.name} | {aliases}]'
            if parent:
                fmt = f'{parent}'
            alias = f'[{command.name} | {aliases}]'
        else:
            alias = command.name if not parent else f'{parent} {command.name}'
        return f'{alias} {command.signature}'

  def common_command_formatting(self, embed_like, command):
        embed_like.title = self.get_command_signature(command)
        if command.description:
            embed_like.description = f'{command.description}\n\n{command.help}'
        else:
            embed_like.description = command.help or 'No help found...'

  
  async def send_group_help(self, group):
    with open('blacklist.json', 'r') as f:
        idk = json.load(f)
    if str(self.context.author.id) in idk["ids"]:
        embed = discord.Embed(title="<:xross:1053176060759515218> Blacklisted User", description="You Are Blacklisted From Using My Commands.\n<:person:1053178413478838312> **Moderator:** `Auto Detection`\n<:Notification:1053149447506374666> ***Reason:** `Spamming My Commands`", color=0xdbdbdb)
        await self.context.reply(embed=embed, mention_author=False)
    else:
        await self.context.typing()
        data = getConfig(self.context.guild.id)
        prefix = data["prefix"]
        Wtf = ".send"
        if not group.commands:
            return await self.send_command_help(group)
        _cmds = "\n\n".join(f" • `{c.qualified_name}`\n{c.short_doc}" for c in group.commands)
        button2 = discord.ui.Button(label='Help',style=discord.ButtonStyle.success)
        button1 = discord.ui.Button(label='Support',style=discord.ButtonStyle.primary)

        view = discord.ui.View()
        view.add_item(button2)
        view.add_item(button1)
        async def button2_callback(interaction: discord.Interaction):
          await interaction.response.defer()
          embed1 = discord.Embed(description=f'**Commands Info:** \n\n`{_cmds}`')
          await interaction.user.send(embed=embed1)
          
          
        async def button1_callback(interaction: discord.Interaction):
          embed5=discord.Embed(description="Go there -> [Support Server](https://discord.gg/3YmDAzbuRR)")
          await interaction.response.send_message(embed=embed5, ephemeral=True)        

        embed = discord.Embed(color=0x7350EB)

        embed.title = f" Need Help ?"
        
        embed.description = f" *Click on `Help` button for command info!*\n*If you fails to get any `DM` from `Sputnik` try enabling this option!*"
        
        embed.set_image(url="https://media.discordapp.net/attachments/1065214371585867879/1066187868596342834/Screenshot_2023_0121_081511.png")
        embed.set_footer(text="Reminder : Must have DMs opened! ")
        button2.callback = button2_callback
        button1.callback = button1_callback

        if group.aliases:
            
             embed.timestamp = discord.utils.utcnow()
        await self.context.send(embed=embed,view=view, delete_after = 60)

  async def send_cog_help(self, cog):
    with open('blacklist.json', 'r') as f:
      data = json.load(f)
    if str(self.context.author.id) in data["ids"]:
      embed = discord.Embed(title="<:xross:1053176060759515218> Blacklisted User", description="You Are Blacklisted From Using My Commands.\n<:person:1053178413478838312> **Moderator:** `Auto Detection`\n<:Notification:1053149447506374666> ***Reason:** `Spamming My Commands`", color=0xdbdbdb)
      return await self.context.reply(embed=embed, mention_author=False)
    await self.context.typing()
    embed = discord.Embed( color=0xdbdbdb)
    embed.title ="Here's some help!"
    embed.description = f"<:urrow:1053243283549204520> **[Join Support Server](https://discord.gg/3YmDAzbuRR)** ***[discord.gg/3YmDAzbuRR]***\n<:urrow:1053243283549204520> **[Documentation](https://discord.gg/3YmDAzbuRR)**"
    for cmd in cog.get_commands():
      if not cmd.hidden:
        _brief = cmd.short_doc if cmd.short_doc else "No Help Provided..."
     # otay = ', '.join(f"`<{param}>`" for param in cmd.clean_params)
      #params = [param for param in cmd.clean_params]
        embed.add_field(name=f"Command Details:", value=f"<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Name:** `{self.context.prefix}{cmd.name}`\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Description:** `{_brief}`\n\n", inline=False)
    embed.timestamp = discord.utils.utcnow()
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/l7vKMv604vRFUX251EGvc9MWNmFqwBYmcF_8IVYRmug/https/cdn.discordapp.com/emojis/1053153617353396234.png")    
        
    embed.set_footer(text="Reminder : Hooks such as <> must not be used when executing commands.", icon_url="")
    await self.context.send(embed=embed)

class Help(Cog, name="help "):
  def __init__(self, client:Sputnik):
    self._original_help_command = client.help_command
    attributes = {
            'name': "Commands",
            'aliases': ['command','cmd','cmds','helpcmd','helpcmds','hc','h','help'],
            'cooldown': commands.CooldownMapping.from_cooldown(1, 5, commands.BucketType.user),
            'help': 'Shows commands of this bot'
        }
    client.help_command = HelpCommand(command_attrs=attributes)
    client.help_command.cog = self

  async def cog_unload(self):
    self.help_command = self._original_help_command
