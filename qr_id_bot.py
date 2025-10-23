import logging
import os
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters, ContextTypes
from keep_alive import keep_alive

BOT_TOKEN ="8410757797:AAFkltxNJ_kaXcofkVCl-8tVdeYP2qK_evk"

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# 🌟 /start कमांड का वेलकम मैसेज
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text(
        f"👋 नमस्ते {user.first_name}!\n\n"
        "मैं *Smarty Sunny* द्वारा बनाया गया एक बॉट हूँ 🤖\n\n"
        "मेरा काम है — QR Code की *File ID* निकालना 🔑\n\n"
        "बस मुझे कोई *QR Code या नॉर्मल फोटो* भेजो, मैं उसका File ID दे दूँगा ✅",
        parse_mode='Markdown'
    )

# 📸 QR Code की File ID निकालने वाला फ़ंक्शन
async def get_photo_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.photo:
        largest_photo = update.message.photo[-1]
        file_id = largest_photo.file_id
        logger.info(f"🔑 QR CODE FILE ID: {file_id}")
        await update.message.reply_text(
            f"✅ QR Code File ID सफलतापूर्वक प्राप्त हुई।\n\n**{file_id}**",
            parse_mode='Markdown'
        )
        await update.message.reply_text("अब आप इस ID को अपने मुख्य बॉट में इस्तेमाल कर सकते हैं।")
    else:
        await update.message.reply_text("❌ यह फोटो नहीं है। कृपया केवल QR कोड इमेज भेजें।")

def main():
    keep_alive()
    application = Application.builder().token(BOT_TOKEN).build()

    # /start कमांड हैंडलर
    application.add_handler(CommandHandler("start", start))

    # फोटो मैसेज हैंडलर
    application.add_handler(MessageHandler(filters.PHOTO & ~filters.COMMAND, get_photo_file_id))

    logger.info("🚀 QR ID Bot (by Smarty Sunny) शुरू हो गया है। Telegram में फोटो भेजें।")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
