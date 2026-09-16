import os, yt_dlp
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
TOKEN=os.getenv("BOT_TOKEN")
async def start(u,c): await u.message.reply_text("Manda o link do Insta/TikTok")
async def baixar(u,c):
 url=u.message.text; s=await u.message.reply_text("Baixando... ⏳")
 try:
  o={'format':'best','outtmpl':'vid.%(ext)s','quiet':True}
  with yt_dlp.YoutubeDL(o) as y: y.extract_info(url,download=True); f=[x for x in os.listdir(".") if x.startswith("vid.")][0]
  await u.message.reply_video(video=open(f,'rb')); os.remove(f); await s.delete()
 except Exception as e: await s.edit_text(f"Erro: {e}")
app=ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start",start))
app.add_handler(MessageHandler(filters.TEXT,baixar))
app.run_polling()
