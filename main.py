import os
import discord
import requests
import mysql.connector
from dotenv import load_dotenv
from fastapi import FastAPI

cnx = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="barracks_db_dev"
)


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

app = FastAPI()

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True 
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    print("Received a message")
    if message.author == client.user:
        return
    
    print(f"Message from {message.author}: {message.content}")

    if message.content.startswith('$hello'):
        print(f"Message from {message.author}: {message.content}")
        try:
            await message.channel.send('Hello!')
        except Exception as e:
            print(f"Error sending message: {e}")
            
    if message.content.startswith('$hotato'):
        try:
            #fetch from api url
            response = requests.get('https://pixels-server.pixels.xyz/v1/marketplace/item/itm_hotato?pid=2995208a4a8b2e70342104c9')
            data = response.json()
            lowest_price = 9999999
            for listing in data['listings']:
                if listing['price'] < lowest_price:
                    lowest_price = listing['price']
            
            price_message = f"The lowest price for hotato is {lowest_price}"
            await message.channel.send(price_message)
        except Exception as e:
            print(f"Error fetching hotato price: {e}")
            
    if message.content.startswith('$register'):
        try:
            parts = message.content.split(' ')
            if len(parts) != 3: await message.channel.send('Incomplete command')
            
            command, name, role = parts[0], parts[1], parts[2]
            
            await message.channel.send('Registering...')
            
            query = "INSERT INTO user (username, role) VALUES (%s, %s)"
            cursor = cnx.cursor()
            cursor.execute(query, (name, role))
            
            cnx.commit()
            
            await message.channel.send('Registered!')
        
        except Exception as e:
            print(f"Error sending message: {e}")
            
    if message.content.startswith('$bal'):
        try:
            parts = message.content.split(' ')
            if len(parts) != 2: await message.channel.send('Incomplete command')
            
            command, name = parts[0], parts[1]
            
            await message.channel.send('Fetching balance...')
            
            query = "SELECT balance FROM user WHERE username = %s"
            cursor = cnx.cursor()
            cursor.execute(query, (name,))
            
            result = cursor.fetchone()
            
            await message.channel.send(f'Balance: {result[0]}')
        except Exception as e:
            await message.channel.send('Error fetching balance')
    
    if message.content.startswith('$addbal'):
        try:
            parts = message.content.split(' ')
            if len(parts) != 3: await message.channel.send('Incomplete command')
            
            command, name, amount = parts[0], parts[1], parts[2]
            
            await message.channel.send('Adding balance...')
            
            query = "UPDATE user SET balance = balance + %s WHERE username = %s"
            cursor = cnx.cursor()
            cursor.execute(query, (amount, name))
            
            cnx.commit()
            
            await message.channel.send('Balance added!')
        except Exception as e:
            await message.channel.send('Error adding balance')
            

@app.get("/")
def read_root():
    return {"Hello": "World"}



client.run(TOKEN)
