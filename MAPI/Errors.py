import json
from datetime import datetime
import discord
from discord.ext import commands

class MiErrors():
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, ctx, error):
        # Ignore CommandNotFound
        if isinstance(error, commands.CommandNotFound):
            return

        # MAPI cooldown is active
        if str(error) == "Command raised an exception: CooldownActive: Cooldown is active":
            await ctx.send(embed=discord.Embed(color=0xff0000).add_field(name="API Cooldown", value="This command is being ratelimited by the Mila Bot API, please try again in a few seconds!"))

        # Not enough arguments
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=discord.Embed(color=0xff0000).add_field(name="Input Error", value=f"You did not provide enough arguments! Check the usage instructions then try again!\n\n**Usage:** {Utils.usage(ctx.command)}").set_footer(text="<> = Required | [] = Optional | (x|y|z) = Aliases"))

        # Arguments aren't of correct type
        if isinstance(error, commands.BadArgument):
            await ctx.send(embed=discord.Embed(color=0xff0000).add_field(name="Input Error", value=f"You did not provide the correct arguements! Check the usage instructions then try again!\n\n**Usage:** {Utils.usage(ctx.command)}").set_footer(text="<> = Required | [] = Optional | (x|y|z) = Aliases"))

        # Command is on cooldown
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(embed=discord.Embed(color=0xff0000).add_field(name="Cooldown Active", value=f"This command is on cooldown, check the waiting time before trying again!\n\n**Retry after:** {round(error.retry_after)} seconds"))

        # Invoker lacks needed permissions
        if isinstance(error, commands.MissingPermissions):
            if getattr(error, "missing_perms"):
                await ctx.send(embed=discord.Embed(color=0xff0000).add_field(name="Missing Permissions", value=f"You are missing required permissions to use this command! Check that you are authorized to do this!\n\n**Missing permissions:** {[x for x in error.missing_perms]}"))

        # Bot lacks needed permissions
        if isinstance(error, commands.BotMissingPermissions) or isinstance(error, discord.Forbidden):
            await ctx.send(embed=discord.Embed(color=0xff0000).add_field(name="Missing Permissions", value=f"I am missing required permissions to execute this action! Check that I have permission to do this!\n\n**Missing permissions:** {'|'.join([f'`{x}`' for x in error.missing_perms])}"))

        # Check failure
        if isinstance(error, commands.CheckFailure):
            owner = False
            nsfw = False
            for x in ctx.command.checks:
                # Bot developer
                if str(x).startswith("<function is_owner.<locals>.predicate"):
                    owner = True
                    break

                # NSFW command
                if str(x).startswith("<function is_nsfw"):
                    nsfw = True
                    break

            if owner:
                if not ctx.author.id in self.bot.owner_id:
                    await ctx.send(embed=discord.Embed(color=0xff0000).add_field(name="Missing Authorization", value="You are not a developer of me. You cannot use this command!"))
            if nsfw:
                if not ctx.channel.is_nsfw():
                    await ctx.send(embed=discord.Embed(color=0xff0000).add_field(name="NSFW Command", value="That command is restricted to NSFW channels only, you cannot use it outside of channels marked as NSFW!"))

        # Unknown error
        else:
            await ctx.send(embed=discord.Embed(color=0xff0000).add_field(name="Unknown Error", value=f"An unknown error has occured! I am not sure why this has happened!\n\n**Error:** {error}"))

def setup(bot):
    bot.add_cog(MErrors(bot))
