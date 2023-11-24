import discord
import asyncio, time
import random
from discord.ext import commands
from bot_logic import text, wait, wwait
logged = False
id_test = []
id = []
a = []

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
@bot.command()
async def info(ctx):
    task2 = asyncio.create_task(wait(3))
    await ctx.send("Доброго времени суток,это информация про бота")
    await ctx.send("На данный момент сейчас работает только одна фукция")
    await task2
    await ctx.send("Пропишите '!write' для того что бы получить текст")
    await ctx.send("Пропишите '!check текст' для того что бы отправить текст на проверку и получить результат")
    await task2
    await ctx.send("(пишите вместо пробелов -)")


@bot.command()
async def write(ctx):
    e = random.randint(1,9)
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
    if ctx.author.id not in a:
        a.append(ctx.author.id)
    qwe = len(a) - 1
    task1 = asyncio.create_task(wait(55))
    await ctx.send("осталось 60 секунд")
    await task1
    if ctx.author.id in a:
        await ctx.send("осталось 5 секунд")
    task3 = asyncio.create_task(wwait())
    await task3
    if ctx.author.id in a:
        await ctx.send("Время вышло")
        a[qwe] = 'end'

@bot.command()
async def check(ctx , abc):
    if ctx.author.id in a:
        index = id.index(ctx.author.id)
        await ctx.send(f"Результат: {text(id_test[index],abc)} балов")
        if ctx.author.id in a:
            index_a = a.index(ctx.author.id)
            a[index_a] = "end"
    else: await ctx.send("Вы не успели написать текст или вы его не взяли.Пропишите !write что бы попробовать ещё раз.")


bot.run("TOKEN")
