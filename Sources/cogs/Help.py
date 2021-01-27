import asyncio,discord
import os
from discord.ext import commands
from discord.ext.commands import bot

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Welcome to BHB.", description=f"To help solving baekjoon online judge!", color=0x660066)
        embed.add_field(name=f"Everyone commands", value=f"help, hello", inline=False)
        embed.add_field(name=f"Developer commands", value=f"?????", inline=False)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Help(bot))