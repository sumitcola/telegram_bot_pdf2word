import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from pdf_to_word import convert_pdf_to_word

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi! Send me a PDF file and I will convert it to a Word document.')

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await context.bot.get_file(update.message.document.file_id)
    pdf_path = 'input.pdf'
    word_path = 'output.docx'

    await file.download_to_drive(pdf_path)
    convert_pdf_to_word(pdf_path, word_path)

    await update.message.reply_document(document=open(word_path, 'rb'))

    # Cleanup temp files
    os.remove(pdf_path)
    os.remove(word_path)

if __name__ == '__main__':
    app = ApplicationBuilder().token('8276086405:AAFQHTn6kWaarGk9e6l2Lp5dUGi9l9o7FT0').build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.Document.PDF, handle_document))

    print("Bot is running...")
    app.run_polling()
