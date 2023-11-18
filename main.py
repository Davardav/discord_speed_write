import discord
import time
import random
from discord.ext import commands
from bot_logic import text
id_test = []
id = []

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def q(ctx):
    await ctx.send("potato")

@bot.command()
async def w(ctx):
    
    await ctx.send("aaaa")


@bot.command()
async def write(ctx):
    e = random.randint(1,5)
    with open(f'img/img{e}.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("перепиши текст как можно правильней по команде !check текст вместо пробелов ставьте -")
    if ctx.author.id in id:
        index = id.index(ctx.author.id)
        id.pop(index)
        id_test.pop(index)
    id.append(ctx.author.id)
    id_test.append(e)

@bot.command()
async def check(ctx , abc):
    index = id.index(ctx.author.id)
    await ctx.send(text(id_test[index],abc))


bot.run("TOKEN")