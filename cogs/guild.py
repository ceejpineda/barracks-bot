import discord
from discord.ext import commands
import requests
import emoji
import re

def remove_emojis(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

class GuildCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def show_members(self, ctx, guild_name):
        response = requests.get(f'https://pixels-server.pixels.xyz/v1/guild/{guild_name}').json()

        max_username_length = max(len(remove_emojis(user['player']['username'])) for user in response['guildMembers'] if user['role'] != 'Watcher')
        max_role_length = max(len(user['role']) for user in response['guildMembers'] if user['role'] != 'Watcher')
        max_shard_count_length = max(len(str(user['membershipsCount'])) for user in response['guildMembers'] if user['role'] != 'Watcher')

        table = f"{'Username'.ljust(max_username_length)} | {'Role'.ljust(max_role_length)} | {'Shard Count'.ljust(max_shard_count_length)}\n--- | --- | ---\n"  # Table headers

        for user in response['guildMembers']:
            if user['role'] != 'Watcher':
                username = remove_emojis(user['player']['username']).ljust(max_username_length)
                role = user['role'].ljust(max_role_length)
                shard_count = str(user['membershipsCount']).ljust(max_shard_count_length)
                table += f"{username} | {role} | {shard_count}\n"  # Add each user to the table

        # Split the table into lines
        lines = table.split('\n')

        # Send each chunk of lines as a separate message
        chunk = ""
        for line in lines:
            if len(chunk) + len(line) > 1990:
                await ctx.send(f"```{chunk}```")
                chunk = line
            else:
                chunk += line + '\n'

        # Send the last chunk if it's not empty
        if chunk:
            await ctx.send(f"```{chunk}```")

    @commands.command()
    async def search_member(self, ctx, guild_name, member_name):
        response = requests.get(f'https://pixels-server.pixels.xyz/v1/guild/{guild_name}').json()

        for user in response['guildMembers']:
            if member_name.lower() in remove_emojis(user['player']['username']).lower():
                username = remove_emojis(user['player']['username'])
                role = user['role']
                shard_count = user['membershipsCount']
                await ctx.send(f"```Username: {username}\nRole: {role}\nShard Count: {shard_count}```")
                return

        await ctx.send(f"```Member '{member_name}' not found in guild '{guild_name}'.```")
async def setup(bot):
    await bot.add_cog(GuildCommands(bot))