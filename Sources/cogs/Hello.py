import asyncio,discord
import os
from discord.ext import commands
from discord.ext.commands import bot

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hello(self, ctx):
        embed = discord.Embed(title="Welcome to BHB.", description=f"To help solving baekjoon online judge!", color=0x660066)
        embed.add_field(name=f"Developer", value=f"JSW, LJH, SSW", inline=False)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Hello(bot))
