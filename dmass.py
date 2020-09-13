import discord
from discord.ext import commands
import platform
import random
import time


bot = commands.Bot(command_prefix='-', case_insensitive=True)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}(ID: +{bot.user.id}) |'
          f'Connected to {str(len(bot.guilds))} servers |'
          f'Connected to {str(len(set(bot.get_all_members())))} users')
    print('--------')
    print('CREATED AND HOSTED BY INVADER OP | Fixed Version')


@bot.event
async def on_command_error(ctx, error):
    # Ignore these errors:
    ignored = (
        commands.CommandNotFound, commands.UserInputError, commands.BotMissingPermissions, commands.MissingPermissions, discord.errors.Forbidden, commands.CommandInvokeError, commands.MissingRequiredArgument)
    if isinstance(error, ignored):
        return


@commands.has_permissions(administrator=True)
@bot.command()
async def announce(ctx, role: discord.Role, *, msg): # announces to the specified role
    global members
    members = [m for m in ctx.guild.members if role in m.roles]
    for m in members:
        try:
            await m.send(msg)
            await ctx.send(f":white_check_mark: Message sent to {m}")
        except:
            await ctx.send(f":x: No DM could be sent to {m}")
    await ctx.send("Done!")
@announce.error
# feel free to add another decorator here if you wish for it to send the same messages
# for the same exceptions: e.g. @userinfo.error
async def _announcement_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send(":x: Role couldn't be found!")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f":x: {ctx.author.mention}, you don't have sufficient permissions.")
    else:
        await ctx.send(error)


bot.run("NzU0Nzc2NDA2MDI1ODMwNTEy.X15qTg.KO4VOaqR64gaJZykAyWFkH9mE74")
