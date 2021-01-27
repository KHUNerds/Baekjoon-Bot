import asyncio,discord
import os
from discord.ext import commands
from discord.ext.commands import bot

# setting bot
token = "token"
game = discord.Game(";sex")
bot = commands.Bot(command_prefix=';', status=discord.Status.online, activity=game, help_command=None)

# directory of cogs (exttensions)
os.chdir(os.getcwd() + '/Sources/cogs')
extensions = ["cogs.Help", "cogs.Hello"]

def main():
    for ext in extensions:
        try:
            bot.load_extension(ext)
        except Exception as e:
            print("load fail : " + str(e))

if __name__ == "__main__":
    main()
    

# starting bot
@bot.event
async def on_ready():
    print("start bot")

@bot.event
async def on_member_join(member):
    await member.send("Hello coding slave. Welcome to BHB.")

bot.run(token)

