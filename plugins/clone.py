from pyrogram import Client, filters
import random
import asyncio
import time
import pytz
from datetime import datetime, timedelta
from pyrogram.errors import FloodWait
tz = pytz.timezone("Europe/Istanbul")
from config import DEPO

@Client.on_message(filters.command("film") & filters.private)
async def filmg(bot, message):
    try:
        msj = message.text.split(" ")
        if len(msj) < 4:
            await message.reply_text("Hatalı Kullanım")
            return
        kanal_id = str(msj[1])
        id = int(msj[2])
        son_id = int(msj[3])
        sayi = await message.reply_text(f"{kanal_id} {id} {son_id}")
        msg = await message.reply_text("`Filmleri Kopyalıyorum Bekle`")
        for mid in range(id,son_id):
            bugun = datetime.now(tz).strftime("%T")
            if int(bugun.split(":")[0]) >= 20 or int(bugun.split(":")[0]) < 8:
                uyu = 30
            else:
                uyu = random.randint(2,5)
            try:
                cop = await bot.get_messages(kanal_id, mid)
            except FloodWait as e:
                await asyncio.sleep(e.value)
                try:
                    cop = await bot.get_messages(kanal_id, mid)
                except Exception as e:
                    print(e)
            if not cop:
                continue
            else:
                try:
                    await bot.copy_message(
                        chat_id=DEPO, 
                        from_chat_id=kanal_id, 
                        message_id=mid)
                    await asyncio.sleep(uyu)
                except FloodWait as f:
                    await asyncio.sleep(f.value)
        await msg.edit("İŞLEM TAMAM!!!")
    except Exception as e:
        await message.reply_text(e)
