import unittest
from unittest.mock import MagicMock
from bot.message_handler import MessageHandler

class TestMessageHandler(unittest.TestCase):
    def test_handle_message(self):
        mock_client = MagicMock()
        handler = MessageHandler(mock_client)

        # Test untuk pesan dengan "السلام عليكم"
        message = {"from": "123", "id": "1", "body": "السلام عليكم", "isGroupMsg": False}
        handler.handle_message(message)
        mock_client.reply.assert_called_with("123", "وعليكم السلام", "1")

        # Test untuk pesan lainnya
        message = {"from": "123", "id": "2", "body": "Hello", "isGroupMsg": False}
        handler.handle_message(message)
        mock_client.reply.assert_called_with("123", "Welcome", "2")

if __name__ == "__main__":
    unittest.main()
