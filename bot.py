import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8965341019:AAHXhNnkwZrXv18pWYCGliL38vbDB9DpmJU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Eshan Trading Bot Started ✅")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commands:\n/start\n/help\n/price\n/signal"
    )

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = requests.get(
        "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    ).json()

    btc_price = data["bitcoin"]["usd"]

    await update.message.reply_text(
        f"₿ Bitcoin Price: ${btc_price}"
    )

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = requests.get(
        "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    ).json()

    price = data["bitcoin"]["usd"]

    if price > 65000:
        signal = "🟢 BUY Signal"
    elif price < 60000:
        signal = "🔴 SELL Signal"
    else:
        signal = "🟡 WAIT Signal"

    await update.message.reply_text(
        f"📊 BTC Signal\n\nPrice: ${price}\n\n{signal}"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("price", price))
app.add_handler(CommandHandler("signal", signal))

print("Bot is running...")

app.run_polling()
