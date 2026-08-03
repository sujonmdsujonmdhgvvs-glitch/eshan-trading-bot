from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8965341019:AAEKz8Iz-5veDnJT8-saBTFj3rHUh6KC19k"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Eshan Trading Bot Started ✅")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot is running...")

app.run_polling()
