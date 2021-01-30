import asyncio,discord
import os
from discord.ext import commands
from discord.ext.commands import bot
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from Modules import make_module

class Find(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def find(self, ctx, problem_number):
        problem = make_module.find_problem(str(problem_number))

        number = problem.get_number()
        title = problem.get_title()
        tier = problem.get_tier()
        url = problem.get_url()

        embed = discord.Embed(title=problem_number, color=0x660066)
        embed.add_field(name=f"number", value=number, inline=False)
        embed.add_field(name=f"title", value=title, inline=False)
        embed.add_field(name=f"tier", value=tier, inline=False)
        embed.add_field(name=f"url", value=url, inline=False)
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Find(bot))
