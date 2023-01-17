from discord.ext import commands
import discord

intents=discord.Intents.all()

bot = commands.Bot(command_prefix='/', intents=intents) 

@bot.command()
async def info(ctx):
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)

@bot.command()
async def punch(ctx, arg):
    await ctx.send(f'Punched {arg}')

bot.run('haha')