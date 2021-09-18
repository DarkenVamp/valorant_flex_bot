from discord import File
from discord.ext import commands
from modules.valo_image import getImg
from modules.valo_data import getData
import os
TOKEN = os.environ.get('DC_TOKEN')
bot = commands.Bot(command_prefix='!')


@bot.command()
async def valo(ctx, name):
    async with ctx.typing():
        data = getData(name)
        if isinstance(data, dict):
            await ctx.send(file=File(fp=getImg(data), filename=f'{name}.png'))
        else:
            await ctx.send(data)

bot.run(TOKEN)
