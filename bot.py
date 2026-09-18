import os
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("Hello! My Telegram bot is running on Railway.")

if __name__ == "__main__":
    if not TOKEN:
        raise ValueError("BOT_TOKEN environment variable is missing!")
    
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is starting...")
    app.run_polling()