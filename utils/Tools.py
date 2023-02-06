import json, sys, os
from discord.ext import commands
from core import Context
import aiohttp



def DotEnv(query: str):
  return os.getenv(query)

def getConfig(guildID):
    with open("config.json", "r") as config:
        data = json.load(config)
    if str(guildID) not in data["guilds"]:
        defaultConfig = {
            "backupkey": "none",
            "antiSpam": False,
            "antiLink": False,
            "whitelisted": [],
            "banwl": [],
            "unbanwl": [],
            "kickwl": [],   
            "prunewl": [],
            "spamwl": [],
            "pingswl": [],
            "webwl": [],
            "channelcwl": [],
            "channelrwl": [],
            "rolecwl": [],
            "rolerwl": [],
            "linkwl": [],
            "integrationwl": [],
            "emowl": [],
            "stickerwl": [],
            "guildwl": [],
            "botwl": [],
            "abanpunish": "none",
            "aunbanpunish": "none",
            "akickpunish": "none",
            "aspampunish": "none",
            "awebpunish": "none",
            "arolepunish": "none",
            "achannelpunish": "none",
            "apingpunish": "none",
            "alinkpunish": "none",
            "aintigpunish": "none",
            "aemopunish": "none",
            "aprunepunish": "none",
            "aguildpunish": "none",
            "astickpunish": "none",
            "abotpunish": "none",
            "beastmode":"none",
            "prefix": ".",
            "mod": [],
            "admin": [],
            "owner": []
        }
        updateConfig(guildID, defaultConfig)
        return defaultConfig
    return data["guilds"][str(guildID)]


def updateConfig(guildID, data):
    with open("config.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildID)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("config.json", "w") as config:
        config.write(newdata)

def give_unb(user_id: int) -> None:
    with open("2ndbotowners.json", "r") as file:
        file_data = json.load(file)
        if str(user_id) in file_data["ids"]:
            return

        file_data["ids"].append(str(user_id))
    with open("2ndbotowners.json", "w") as file:
        json.dump(file_data, file, indent=4)

def take_unb(user_id: int) -> None:
    with open("2ndbotowners.json", "r") as file:
        file_data = json.load(file)
        file_data["ids"].remove(str(user_id))
    with open("2ndbotowners.json", "w") as file:
        json.dump(file_data, file, indent=4)


def add_user_to_blacklist(user_id: int) -> None:
    with open("blacklist.json", "r") as file:
        file_data = json.load(file)
        if str(user_id) in file_data["ids"]:
            return

        file_data["ids"].append(str(user_id))
    with open("blacklist.json", "w") as file:
        json.dump(file_data, file, indent=4)


def remove_user_from_blacklist(user_id: int) -> None:
    with open("blacklist.json", "r") as file:
        file_data = json.load(file)
        file_data["ids"].remove(str(user_id))
    with open("blacklist.json", "w") as file:
        json.dump(file_data, file, indent=4)

def add_mod(user_id: int) -> None:
    with open("config.json", "r") as file:
        file_data = json.load(file)
        if str(user_id) in file_data["ids"]:
            return

        file_data["ids"].append(str(user_id))
    with open("config.json", "w") as file:
        json.dump(file_data, file, indent=4)


def remove_mod(user_id: int) -> None:
    with open("config.json", "r") as file:
        file_data = json.load(file)
        file_data["ids"].remove(str(user_id))
    with open("config.json", "w") as file:
        json.dump(file_data, file, indent=4)

def update_vanity(guild, code):
    with open('vanity.json', 'r') as vanity:
        vanity = json.load(vanity)
    vanity[str(guild)] = str(code)
    new = json.dumps(vanity, indent=4, ensure_ascii=False)
    with open('vanity.json', 'w') as vanity:
        vanity.write(new)


def blacklist_check():
    def predicate(ctx):
        with open("blacklist.json") as f:
            data = json.load(f)
            if str(ctx.author.id) in data["ids"]:
                return False
            return True

    return commands.check(predicate)

def mod_check():
    def predicate(ctx):
        with open("config.json") as f:
            data = json.load(f)
            if str(ctx.author.id) in data["ids"]:
                return True
            


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def getLogger(guildid):
  with open("logger.json", "r") as op:
    data = json.load(op)
  if str(guildid) not in data:
    default = {
      "channel": ""
    }
    createLogger(guildid, default)
    return default
  return data[str(guildid)]

def createLogger(guildid, data):
  with open("logger.json", "r") as f:
    logs = json.load(f)
  logs[str(guildid)] = data
  new = json.dumps(logs, indent=4, ensure_ascii=False)
  with open("logger.json", "w") as idk:
    idk.write(new)


def getbadges(userid):
  with open("badges.json", "r") as f:
    data = json.load(f)
  if str(userid) not in data:
    default = []
    makebadges(userid, default)
    return default
  return data[str(userid)]

def makebadges(userid, data):
  with open("badges.json", "r") as f:
    badges = json.load(f)
  badges[str(userid)] = data
  new = json.dumps(badges, indent=4, ensure_ascii=False)
  with open("badges.json", "w") as w:
    w.write(new)


#antiban#


def getantiban(guildid):
    with open("antiban.json", "r") as config:
        data = json.load(config)
    if str(guildid) not in data["guilds"]:
        default = "off"
        updateantiban(guildid, default)
        return default
    return data["guilds"][str(guildid)]

def updateantiban(guildid, data):
    with open("antiban.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildid)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("antiban.json", "w") as config:
        config.write(newdata)
#antikick#
def getantikick(guildid):
    with open("antikick.json", "r") as config:
        data = json.load(config)
    if str(guildid) not in data["guilds"]:
        default = "off"
        updateantikick(guildid, default)
        return default
    return data["guilds"][str(guildid)]

def updateantikick(guildid, data):
    with open("antikick.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildid)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("antikick.json", "w") as config:
        config.write(newdata)
#antiguild#
def getantiguild(guildid):
    with open("antiguild.json", "r") as config:
        data = json.load(config)
    if str(guildid) not in data["guilds"]:
        default = "off"
        updateantiguild(guildid, default)
        return default
    return data["guilds"][str(guildid)]

def updateantiguild(guildid, data):
    with open("antiguild.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildid)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("antiguild.json", "w") as config:
        config.write(newdata)

#antiemo#
def getantiemo(guildid):
    with open("antiemo.json", "r") as config:
        data = json.load(config)
    if str(guildid) not in data["guilds"]:
        default = "off"
        updateantiemo(guildid, default)
        return default
    return data["guilds"][str(guildid)]

def updateantiemo(guildid, data):
    with open("antiemo.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildid)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("antiemo.json", "w") as config:
        config.write(newdata)
#antisticker#
def getantisticker(guildid):
    with open("antisticker.json", "r") as config:
        data = json.load(config)
    if str(guildid) not in data["guilds"]:
        default = "off"
        updateantisticker(guildid, default)
        return default
    return data["guilds"][str(guildid)]

def updateantisticker(guildid, data):
    with open("antisticker.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildid)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("antisticker.json", "w") as config:
        config.write(newdata)
#antirole#
def getantirole(guildid):
    with open("antirole.json", "r") as config:
        data = json.load(config)
    if str(guildid) not in data["guilds"]:
        default = "off"
        updateantirole(guildid, default)
        return default
    return data["guilds"][str(guildid)]

def updateantirole(guildid, data):
    with open("antirole.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildid)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("antirole.json", "w") as config:
        config.write(newdata)
#antichannel#
def getantich(guildid):
    with open("antich.json", "r") as config:
        data = json.load(config)
    if str(guildid) not in data["guilds"]:
        default = "off"
        updateantich(guildid, default)
        return default
    return data["guilds"][str(guildid)]

def updateantich(guildid, data):
    with open("antich.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildid)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("antich.json", "w") as config:
        config.write(newdata)
#antibot#
def getantibot(guildid):
    with open("antibot.json", "r") as config:
        data = json.load(config)
    if str(guildid) not in data["guilds"]:
        default = "off"
        updateantibot(guildid, default)
        return default
    return data["guilds"][str(guildid)]

def updateantibot(guildid, data):
    with open("antibot.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildid)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("antibot.json", "w") as config:
        config.write(newdata)
#antiintigration#
def getantiintig(guildid):
    with open("antiintig.json", "r") as config:
        data = json.load(config)
    if str(guildid) not in data["guilds"]:
        default = "off"
        updateantiintig(guildid, default)
        return default
    return data["guilds"][str(guildid)]

def updateantiintig(guildid, data):
    with open("antiintig.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildid)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("antiintig.json", "w") as config:
        config.write(newdata)
#antiping#
def getantiping(guildid):
    with open("antiping.json", "r") as config:
        data = json.load(config)
    if str(guildid) not in data["guilds"]:
        default = "off"
        updateantiping(guildid, default)
        return default
    return data["guilds"][str(guildid)]

def updateantiping(guildid, data):
    with open("antiping.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildid)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("antiping.json", "w") as config:
        config.write(newdata)
#antiprune#
def getantiprune(guildid):
    with open("antiprune.json", "r") as config:
        data = json.load(config)
    if str(guildid) not in data["guilds"]:
        default = "off"
        updateantiprune(guildid, default)
        return default
    return data["guilds"][str(guildid)]

def updateantiprune(guildid, data):
    with open("antiprune.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildid)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("antiprune.json", "w") as config:
        config.write(newdata)
#antispam#
def getantispam(guildid):
    with open("antispam.json", "r") as config:
        data = json.load(config)
    if str(guildid) not in data["guilds"]:
        default = "off"
        updateantispam(guildid, default)
        return default
    return data["guilds"][str(guildid)]

def updateantispam(guildid, data):
    with open("antispam.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildid)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("antispam.json", "w") as config:
        config.write(newdata)
#antiwebhook#
def getantiwebh(guildid):
    with open("antiwebh.json", "r") as config:
        data = json.load(config)
    if str(guildid) not in data["guilds"]:
        default = "off"
        updateantiwebh(guildid, default)
        return default
    return data["guilds"][str(guildid)]

def updateantiwebh(guildid, data):
    with open("antiwebh.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildid)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("antiwebh.json", "w") as config:
        config.write(newdata)

#antianti#
def getanti(guildid):
    with open("anti.json", "r") as config:
        data = json.load(config)
    if str(guildid) not in data["guilds"]:
        default = "off"
        updateanti(guildid, default)
        return default
    return data["guilds"][str(guildid)]

def updateanti(guildid, data):
    with open("anti.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildid)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("anti.json", "w") as config:
        config.write(newdata)

def add_channel_to_ignore(user_id: int) -> None:
    with open("ignore.json", "r") as file:
        file_data = json.load(file)
        if str(user_id) in file_data["ids"]:
            return

        file_data["ids"].append(str(user_id))
    with open("ignore.json", "w") as file:
        json.dump(file_data, file, indent=4)


def remove_channel_from_ignore(user_id: int) -> None:
    with open("ignore.json", "r") as file:
        file_data = json.load(file)
        file_data["ids"].remove(str(user_id))
    with open("ignore.json", "w") as file:
        json.dump(file_data, file, indent=4)


def ignore_check():

    def predicate(ctx):
        with open("ignore.json") as f:
            data = json.load(f)
            if str(ctx.channel.id) in data["ids"]:
                return False
            return True

    return commands.check(predicate)


def getbeastmode(guildid):
    with open("beastmode.json", "r") as config:
        data = json.load(config)
    if str(guildid) not in data["guilds"]:
        default = "off"
        updatebeastmode(guildid, default)
        return default
    return data["guilds"][str(guildid)]

def updatebeastmode(guildid, data):
    with open("beastmode.json", "r") as config:
        config = json.load(config)
    config["guilds"][str(guildid)] = data
    newdata = json.dumps(config, indent=4, ensure_ascii=False)
    with open("beastmode.json", "w") as config:
        config.write(newdata)

