import unittest
from bot.bot import WhatsAppBot

class TestWhatsAppBot(unittest.TestCase):
    def test_initialization(self):
        bot = WhatsAppBot("dummy_session", False)
        self.assertIsNotNone(bot)

if __name__ == "__main__":
    unittest.main()
