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
eth_price = data["ethereum"]["usd"]
bnb_price = data["binancecoin"]["usd"]
sol_price = data["solana"]["usd"]

await update.message.reply_text(
    f"💰 Crypto Prices\n\n"
    f"₿ BTC: ${btc_price}\n"
    f"🔷 ETH: ${eth_price}\n"
    f"🟡 BNB: ${bnb_price}\n"
    f"🟣 SOL: ${sol_price}"

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
        f"📊 BTC Smart Signal\n\n💰 Price: ${price}\n\n{signal}\n\n⚠️ Market analysis based"
    )
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("price", price))
app.add_handler(CommandHandler("signal", signal))

print("Bot is running...")

app.run_polling()
