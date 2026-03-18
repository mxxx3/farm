import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Konfiguracja logowania (pomaga debugować błędy na Koyeb)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Pobieranie tokena z Twojej zmiennej środowiskowej na Koyeb
TOKEN = os.getenv('magic_farm')

# Domyślny link do WebAppa
BASE_WEBAPP_URL = 'https://t.me/MagicFarmGameBot/magicfarm'

# Opis gry (escaped dla MarkdownV2)
DESCRIPTION = (
    "*Game Description*\n"
    "*Magic Farm: Ad Watching Adventure*\n\n"
    "Earn by watching\\. Sounds simple\\? That’s because it is\\. But behind the simplicity lies a system rewarding consistency, patience, and engagement\\.\n\n"
    "🎯 *Tap and Earn*\n"
    "Every click brings you closer to real crypto rewards\\. Ads\\? Yes — but each one is a chance to grab TRX and Drops tokens\\.\n\n"
    "🪙 *Collect, Convert, Track*\n"
    "Watch your balance grow with every action\\. Drops or TRX — you decide how to use your earnings\\.\n\n"
    "🎁 *Surprises Around Every Corner*\n"
    "Rewards are randomized, so you never know what the next moment will bring\\. Perfect for those who like to watch… and earn\\.\n\n"
    "📱 *Simple, Fast, Enjoyable*\n"
    "Clean interface, no daily limits, clear rules — designed to let you focus on what matters most: your profit\\.\n\n"
    "_Start now and see how rewarding your free time can be\\._"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Obsługa komendy /start z przekazaniem parametru do WebAppa."""
    user = update.effective_user
    
    # Sprawdzanie czy użytkownik przyszedł z linkiem polecającym lub używamy jego ID
    start_param = context.args[0] if context.args else str(user.id)
    webapp_url = f"{BASE_WEBAPP_URL}?startapp={start_param}"

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🚀 Launch Magic Farm", url=webapp_url)]
    ])

    await update.message.reply_text(
        DESCRIPTION, 
        reply_markup=keyboard, 
        parse_mode='MarkdownV2'
    )

def main():
    """Uruchomienie bota."""
    if not TOKEN:
        print("BŁĄD: Zmienna środowiskowa 'magic_farm' nie została znaleziona!")
        return

    # Budowanie aplikacji
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Rejestracja komend
    application.add_handler(CommandHandler("start", start))

    print("Bot Magic Farm uruchomiony...")
    application.run_polling()

if __name__ == '__main__':
    main()