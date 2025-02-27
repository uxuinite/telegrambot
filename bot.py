from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
)
from datetime import datetime

# Function to handle user messages
async def auto_reply(update: Update, context: CallbackContext):
    user_message = update.message.text.lower()
    user_name = update.message.from_user.full_name  # Get sender's name

    responses = {
        "hello": f"Hello, {user_name}! How can I assist you today?",
        "hi": f"Hi there, {user_name}! How's your day going?",
        "how are you": f"I'm just a bot, but I'm doing great! How about you, {user_name}?",
        "what job": f"Job work starts at 9 AM, helping customers complete tasks, {user_name}.",
        "can you show me": f"Sure, {user_name}! What would you like to see?",
        "goodbye": f"Goodbye, {user_name}! Have a great day!",
        "bye": f"Bye, {user_name}! See you soon!",
    }

    if "what time" in user_message or "time is it" in user_message:
        current_time = datetime.now().strftime("%I:%M %p %d/%m/%Y")
        await update.message.reply_text(f"Hello, {user_name}! The time is {current_time}.")
        return

    for key, response in responses.items():
        if key in user_message:
            await update.message.reply_text(response)
            return

    await update.message.reply_text(f"I'm not sure how to respond to that, {user_name}. Can you clarify?")

# Start command
async def start(update: Update, context: CallbackContext):
    user_name = update.message.from_user.full_name  # Get sender's name
    await update.message.reply_text(f"Hello, {user_name}! I'm your chatbot. How can I assist you?")

# Help command
async def help_command(update: Update, context: CallbackContext):
    user_name = update.message.from_user.full_name  # Get sender's name
    await update.message.reply_text(f"You can say 'hello', 'how are you', ask about jobs, or ask for the time, {user_name}!")

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
