import discord
from discord.ext import commands
from discord import app_commands
import subprocess
import time

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

def send_minecraft_command(command):
    """Send command to minecraft server and return output"""
    subprocess.run(['screen', '-S', 'minecraft', '-X', 'stuff', f'{command}^M'])
    time.sleep(0.5)
    subprocess.run(['screen', '-S', 'minecraft', '-X', 'hardcopy', '/home/marcus/DiscordBots/hardcopy.txt'])
    time.sleep(0.5)
    
    try:
        with open('/home/marcus/DiscordBots/hardcopy.txt', 'r') as f:
            return f.read().strip().split('\n')[-2]
    except FileNotFoundError:
        return "No output captured"

whitelist_group = app_commands.Group(name='whitelist', description='Minecraft whitelist commands')

@whitelist_group.command()
async def add(interaction: discord.Interaction, playername: str):
    """Add player to whitelist"""
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("Admin permissions required!", ephemeral=True)
        return
    
    output = send_minecraft_command(f'/whitelist add {playername}')
    await interaction.response.send_message(f"Whitelist add result:\n```{output}```", ephemeral=True)

@whitelist_group.command()
async def remove(interaction: discord.Interaction, playername: str):
    """Remove player from whitelist"""
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("Admin permissions required!", ephemeral=True)
        return
    
    output = send_minecraft_command(f'/whitelist remove {playername}')
    await interaction.response.send_message(f"Whitelist remove result:\n```{output}```", ephemeral=True)

@whitelist_group.command()
async def list(interaction: discord.Interaction):
    """List whitelisted players"""
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("Admin permissions required!", ephemeral=True)
        return
    
    output = send_minecraft_command('/whitelist list')
    await interaction.response.send_message(f"Whitelist:\n```{output}```", ephemeral=True)

@bot.event
async def on_ready():
    bot.tree.add_command(whitelist_group)
    await bot.tree.sync()
    print(f'{bot.user} has connected to Discord!')

# bot.run('YOUR_BOT_TOKEN')
