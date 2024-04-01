import discord
from discord.ext import commands

class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.command()
    # async def hello(self, ctx):
    #     # Check if the author's name contains "C³"
    #     if "C³" not in str(ctx.guild.name):
    #         await ctx.send("You are not a C³ member, I don't like you!")
    #         return

    #     await ctx.send('Hello!')
        
    # @commands.command()
    # async def hasonh(self, ctx):
    #     embed = discord.Embed()
    #     embed.set_image(url='https://media1.tenor.com/m/Hb_sHyuAfqYAAAAC/cillian-murphy-the-boss.gif')
    #     await ctx.send(embed=embed)
        
    # @commands.command()
    # async def godzilla(self, ctx):
    #     embed = discord.Embed()
    #     embed.set_image(url='https://media1.tenor.com/m/Ge_-hMuViA0AAAAC/godzilla-minus-one-godzilla.gif')
    #     await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(GeneralCommands(bot))



# @client.event
# async def on_message(message):
#     print("Received a message")
#     if message.author == client.user:
#         return
    
#     print(f"Message from {message.author}: {message.content}")

#     # if message.content.startswith('$hello'):
#     #     print(f"Message from {message.guild.me.nick}: {message.content}")
#     #     try:
#     #         # Check if the author's name contains "C³"
#     #         if "C³" not in str(message.guild.name):
#     #             await message.channel.send("You are not a C³ member, I don't like you!")
#     #             return

#     #         await message.channel.send('Hello!')
#     #     except Exception as e:
#     #         print(f"Error sending message: {e}")
            
#     if message.content.startswith('$hasonh'):
#         print(f"Message from {message.author}: {message.content}")
#         try:
#             await message.channel.send('https://tenor.com/view/cillian-murphy-the-boss-im-coming-serious-peaky-blinders-gif-13736011')
#         except Exception as e:
#             print(f"Error sending message: {e}")
            
#     if message.content.startswith('$hotato'):
#         try:
#             #fetch from api url
#             response = requests.get('https://pixels-server.pixels.xyz/v1/marketplace/item/itm_hotato?pid=2995208a4a8b2e70342104c9')
#             data = response.json()
#             lowest_price = 9999999
#             for listing in data['listings']:
#                 if listing['price'] < lowest_price:
#                     lowest_price = listing['price']
            
#             price_message = f"The lowest price for hotato is {lowest_price}"
#             await message.channel.send(price_message)
#         except Exception as e:
#             print(f"Error fetching hotato price: {e}")
            
#     if message.content.startswith('$register'):
#         try:
#             parts = message.content.split(' ')
#             if len(parts) != 3: await message.channel.send('Incomplete command')
            
#             command, name, role = parts[0], parts[1], parts[2]
            
#             await message.channel.send('Registering...')
            
#             query = "INSERT INTO user (username, role) VALUES (%s, %s)"
#             cursor = cnx.cursor()
#             cursor.execute(query, (name, role))
            
#             cnx.commit()
            
#             await message.channel.send('Registered!')
        
#         except Exception as e:
#             print(f"Error sending message: {e}")
            
#     if message.content.startswith('$bal'):
#         try:
#             parts = message.content.split(' ')
#             if len(parts) != 2: await message.channel.send('Incomplete command')
            
#             command, name = parts[0], parts[1]
            
#             await message.channel.send('Fetching balance...')
            
#             query = "SELECT balance FROM user WHERE username = %s"
#             cursor = cnx.cursor()
#             cursor.execute(query, (name,))
            
#             result = cursor.fetchone()
            
#             await message.channel.send(f'Balance: {result[0]}')
#         except Exception as e:
#             await message.channel.send('Error fetching balance')
    
#     if message.content.startswith('$addbal'):
#         try:
#             parts = message.content.split(' ')
#             if len(parts) != 3: await message.channel.send('Incomplete command')
            
#             command, name, amount = parts[0], parts[1], parts[2]
            
#             await message.channel.send('Adding balance...')
            
#             query = "UPDATE user SET balance = balance + %s WHERE username = %s"
#             cursor = cnx.cursor()
#             cursor.execute(query, (amount, name))
            
#             cnx.commit()
            
#             await message.channel.send('Balance added!')
#         except Exception as e:
#             await message.channel.send('Error adding balance')

#     if message.content.startswith('$apiary'):
#         try:
#             query = "SELECT land_number, apiary FROM lands WHERE apiary > 0"
#             cursor = cnx.cursor()
#             cursor.execute(query)
            
#             rows = cursor.fetchall()
            
#             print(rows)

#             # Create a list of strings
#             land_strings = [f"Land: {row[0]} ({row[1]} Apiaries)" for row in rows]

#             # Join the strings with newline characters
#             message_str = '\n'.join(land_strings)

#             # Send the string as a message
#             await message.channel.send(message_str)
            
#         except Exception as e:
#             # await message.channel.send('Error fetching apiary')
#             print(f"Error fetching apiary: {e}")
            
