from datetime import datetime
import discord
from discord.ext import commands
import json as js
from termcolor import colored

json = js.load(open(".../config.js",  "r"))  

def display(type, text):
    {
    
    }
    return print(colored(consts[type.upper()].format(datetime.utcnow()) + f" {text}", colours[type.upper()]))

def usage(command: commands.Command):
    f = f"`{command.signature}`"
    call = f.split(" ")[0]
    options = f.split(call)[1]
    return call.replace("[", "(").replace("]", ")") + options

async def get_prefix(bot, m):
    if not m.guild:
        return commands.when_mentioned_or(json["default_prefix"])(bot, m)
    try:
        p = json["default_prefix"] # The source of your guild prefix goes here
        return commands.when_mentioned_or(p)(bot, m)
    except Exception:
        return commands.when_mentioned_or(json["default_prefix"])(bot, m)

async def log_cmd(bot, ctx, error=None):
    if json["cmd_logging"]["enabled"]:
        if error is None:
            if ctx.guild:
                return await bot.get_channel(json["cmd_logging"]["channel"]).send("[`{:%d/%m/%y at %H:%M}`] [`{} ({})`] [`Info`] **{}** used the command: **{}**".format(datetime.utcnow(), str(ctx.guild), ctx.guild.id, str(ctx.author), str(ctx.command)))
            else:
                return await bot.get_channel(json["cmd_logging"]["channel"]).send("[`{:%d/%m/%y at %H:%M}`] [`Info`] **{}** used the command: **{}**".format(datetime.utcnow(), str(ctx.author), str(ctx.command)))
        if error is not None:
            if ctx.guild:
                return await bot.get_channel(json["cmd_logging"]["channel"]).send("[`{:%d/%m/%y at %H:%M}`] [`{} ({})`] [`Error`] **{}** used the command: **{}**\n**Error:** {}".format(datetime.utcnow(), str(ctx.guild), ctx.guild.id, str(ctx.author), str(ctx.command), error))
            else:
                return await bot.get_channel(json["cmd_logging"]["channel"]).send("[`{:%d/%m/%y at %H:%M}`] [`Error`] **{}** used the command: **{}**\n**Error:** {}".format(datetime.utcnow(), str(ctx.author), str(ctx.command), error))

async def log_error(bot, ctx, type, error=None):
    if json["error_logging"]["enabled"]:
        if error is None:
            raise commands.CommandError(message="A foreign error occured which was not recognised by the error handler!")
        if error is not None:
            return await bot.get_channel(json["error_logging"]["channel"]).send(embed=discord.Embed(color=0xD50000, title="Unknow Error").add_field(name="Invoker", value=f"{ctx.author} ({ctx.author.mention})").add_field(name="NSFW Channel", value="Yep" if ctx.channel.is_nsfw() else "Nope").add_field(name="Guild", value=f"{ctx.guild} ({ctx.guild.id})" if ctx.guild else "*Direct Messages*").add_field(name="Command", value=ctx.command).add_field(name="Type", value=type).add_field(name="Error", value=error).set_thumbnail(url=bot.user.avatar_url))

def get_uptime(bot, *, brief=False):
    now = datetime.utcnow()
    delta = now - bot.boot_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if not brief:
        fmt = "{h} hours, {m} minutes and {s} seconds"
        if days:
            fmt = "{d} days, " + fmt
    else:
        fmt = "{h} hrs, {m} mins and {s} secs"
        if days:
            fmt = "{d} days, " + fmt
    return fmt.format(d=days, h=hours, m=minutes, s=seconds)
