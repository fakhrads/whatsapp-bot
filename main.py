import logging
from config import Config
from bot.bot import WhatsAppBot

# Setup logging
logger = logging.getLogger(name="WPP_Whatsapp")
logger.setLevel(Config.LOG_LEVEL)

if __name__ == "__main__":
    bot = WhatsAppBot(Config.SESSION_NAME, Config.LOG_QR)
    bot.run()


