from beeson import app
from pyrogram import filters

@app.on_message(filters.command("alive"))
async def alive(_, m):
    await m.reply("Lmfao!")
