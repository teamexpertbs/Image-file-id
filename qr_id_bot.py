import logging
import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from keep_alive import keep_alive

BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

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
    application.add_handler(MessageHandler(filters.PHOTO & ~filters.COMMAND, get_photo_file_id))
    logger.info("🚀 QR ID Bot शुरू हो गया है। Telegram में फोटो भेजें।")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
