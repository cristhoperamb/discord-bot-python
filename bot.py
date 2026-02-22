import os
import asyncio
import discord
from aiohttp import web
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
PORT = int(os.getenv("PORT", "10000"))

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def health(request):
    return web.Response(text="ok")

async def start_web():
    app = web.Application()
    app.router.add_get("/", health)

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    print(f"Listening on 0.0.0.0:{PORT}")

@client.event
async def on_ready():
    print(f"Logged in as {client.user} (id={client.user.id})")

async def start_bot():
    if not TOKEN:
        raise RuntimeError("DISCORD_TOKEN env var is missing")
    await client.start(TOKEN)

async def main():
    await start_web()
    await start_bot()

if __name__ == "__main__":
    asyncio.run(main())
