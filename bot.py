
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
)

# Function to handle user messages
async def auto_reply(update: Update, context: CallbackContext):
    user_message = update.message.text.lower()

    responses = {
        "hello": "Hello! How can I assist you today?",
        "hi": "Hi there! How's your day going?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what job": "Job work starts at 9 AM, helping customers complete tasks.",
        "can you show me": "Sure! What would you like to see?",
        "goodbye": "Goodbye! Have a great day!",
        "bye": "Bye! See you soon!",
    }

    for key, response in responses.items():
        if key in user_message:
            await update.message.reply_text(response)
            return

    await update.message.reply_text("I'm not sure how to respond to that. Can you clarify?")

# Start command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I'm your chatbot. How can I assist you?")

# Help command
async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("You can say 'hello', 'how are you', or ask about jobs!")

# Main function to run the bot
def main():
    TOKEN = "7585107530:AAE6a_3kU23yChoDEmmaPuMD5oJ9d96rcf0"
    
    # Use Application instead of Updater
    app = Application.builder().token(TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    # Start polling
    app.run_polling()

if __name__ == "__main__":
    main()
