import discord
from discord.ext import commands

class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        # Check if the author's name contains "C³"
        if "C³" not in str(ctx.guild.name):
            await ctx.send("You are not a C³ member, I don't like you!")
            return

        await ctx.send('Hello!')
        
    @commands.command()
    async def hasonh(self, ctx):
        embed = discord.Embed()
        embed.set_image(url='https://media1.tenor.com/m/Hb_sHyuAfqYAAAAC/cillian-murphy-the-boss.gif')
        await ctx.send(embed=embed)
        
    @commands.command()
    async def godzilla(self, ctx):
        embed = discord.Embed()
        embed.set_image(url='https://media1.tenor.com/m/Ge_-hMuViA0AAAAC/godzilla-minus-one-godzilla.gif')
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(FunCommands(bot))