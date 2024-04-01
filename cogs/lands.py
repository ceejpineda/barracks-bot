#[{"land_number":"213","guild_id":"1","type":"SPACE","coop":"1","house":"Large","silo":"1","size":"Large","trees":"24","windmill":"1","mine":"0","apiary":"0","winery":"4","kiln":"0","hutch":"0","woodworking":"0","b_grill":"0","s_grill":"0","g_grill":"0","textiler":"0","sauna_portal":"0","soil":"60"}, ...]
import discord
from discord.ext import commands
import requests
from .db import create_connection

class LandCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cnx = create_connection()

    @commands.command()
    async def show_lands(self, ctx, guild_name):
        # if guild_name is not C3 or C3PO then return
        if guild_name not in ["C3", "C3PO"]:
            await ctx.send("Not C3 Guild Sorry")
            return
        
        # c3 = 1, c3po = 2
        guild_id = 1 if guild_name.upper() == "C3" else 2
        
        query = f"SELECT lands.land_number, name FROM lands JOIN guild ON lands.guild_id = guild.id WHERE guild.id = {guild_id}"
        cursor = self.cnx.cursor(dictionary=True)
        cursor.execute(query)
        
        result = cursor.fetchall()
        
        # Format the result into three columns with separators
        formatted_result = ''
        for i in range(0, len(result), 3):
            row = result[i:i+3]
            formatted_result += ' | '.join(str(item["land_number"]).ljust(10) for item in row)
            formatted_result += '\n'
        
        # Send the result as a markdown message
        await ctx.send(f'```\n{formatted_result}\n```')
    
    # Command to show the lands with specific types like for example $farm apiary will show all lands with apiary the number of apiary 
    @commands.command()
    async def farm(self, ctx, land_type):
        query = f"SELECT land_number, {land_type} FROM lands WHERE {land_type} > 0"
        cursor = self.cnx.cursor(dictionary=True)
        cursor.execute(query)
        
        result = cursor.fetchall()
        
        # Format the result into three columns with separators
        formatted_result = ''
        for i in range(0, len(result), 3):
            row = result[i:i+3]
            formatted_result += ' | '.join(f'{item["land_number"]} (Count: {item[land_type]})'.ljust(15) for item in row)
            formatted_result += '\n'
        
        # Send the result as a markdown message
        await ctx.send(f'```\n{formatted_result}\n```')

async def setup(bot):
    await bot.add_cog(LandCommands(bot))