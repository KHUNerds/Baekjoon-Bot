import asyncio,discord
import os
from discord.ext import commands
from discord.ext.commands import bot

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def help(self, ctx, *kind):
        if not kind:
            embed = discord.Embed(title="Commands.", description=f"You can know some commands below this text.", color=0x660066)
            embed.add_field(name=f"Everyone commands", value=f"help, hello", inline=False)
            embed.add_field(name=f"Developer commands", value=f"find", inline=False)
            await ctx.send(embed = embed)
        else:
            if kind[0] == 'find':
                embed = discord.Embed(title="FIND.", description=f"You can find problem.", color=0x660066)
                embed.add_field(name=f"problem's number", value=f"ex) ;find 1000", inline=False)
                embed.add_field(name=f"???", value=f"???", inline=False)
                await ctx.send(embed = embed)
            elif kind[0] == 'ssw':
                embed = discord.Embed(title="SSW.", description=f"Seungwon Seo", color=0x660066)
                embed.add_field(name=f"GitHub URL", value=f"https://github.com/ssw03270", inline=False)
                await ctx.send(embed = embed)
            elif kind[0] == 'jsw':
                embed = discord.Embed(title="JSW.", description=f"SeungWoo Jeong", color=0x660066)
                embed.add_field(name=f"GitHub URL", value=f"https://github.com/SW0000J", inline=False)
                await ctx.send(embed = embed)
            elif kind[0] == 'ljh':
                embed = discord.Embed(title="LJH.", description=f"Jun Hyeok Lee", color=0x660066)
                embed.add_field(name=f"GitHub URL", value=f"https://github.com/bluehyena", inline=False)
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(title="Syntax Error.", description=f"", color=0x660066)
                await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Help(bot))