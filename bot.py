import os
import discord
from dotenv import load_dotenv

load_dotenv()  # THIS loads your .env file

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user} (id={client.user.id})")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN env var is missing")

client.run(TOKEN)