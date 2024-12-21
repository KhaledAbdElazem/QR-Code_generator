import telebot
import qrcode
from io import BytesIO

# Replace this with your bot token
BOT_TOKEN = "7849933952:AAGxpDYakSzI5gibAkZxyEj5KDZkzlNclUo"

# Initialize the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Command handler for /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Send me a link, and I'll generate a QR code for you.")

# Handle messages with links
@bot.message_handler(func=lambda message: True)
def generate_qr(message):
    try:
        # Get the user's input (link)
        data = message.text

        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,  # Size of the QR Code
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # Error correction level
            box_size=10,  # Size of each box in the QR code grid
            border=4,  # Thickness of the border
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Create the QR code image
        qr_image = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image in memory
        buffer = BytesIO()
        qr_image.save(buffer, format="PNG")
        buffer.seek(0)

        # Send the QR code image back to the user
        bot.send_photo(message.chat.id, buffer, caption="Here is your QR code!")
    except Exception as e:
        bot.reply_to(message, f"An error occurred: {e}")

# Polling to keep the bot running
print("Bot is running...")
bot.polling()
