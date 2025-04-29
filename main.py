import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
VIP_CHANNEL_LINKS = os.getenv("VIP_CHANNEL_LINKS", "").split(",")
REFERRAL_LINK = os.getenv("REFERRAL_LINK")
VALID_TRADER_IDS = ["123456", "654321", "987654"]  # নিজের মত করে আপডেট করতে পারো

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎯 Welcome! Please send me your Trader ID:")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.strip()
    if user_input in VALID_TRADER_IDS:
        links_message = "✨ Congratulations! Here are your VIP Channel Links:\n\n"
        for link in VIP_CHANNEL_LINKS:
            links_message += f"🔗 {link}\n"
        await update.message.reply_text(links_message)
    else:
        await update.message.reply_text(f"❌ Invalid Trader ID.\n👉 Register first: {REFERRAL_LINK}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
