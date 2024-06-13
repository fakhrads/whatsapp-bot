import unittest
from bot.qr_handler import QRHandler

class TestQRHandler(unittest.TestCase):
    def test_catch_qr(self):
        handler = QRHandler()
        handler.catch_qr("dummy_qr_code", "dummy_ascii_qr", 1, "dummy_url_code")
        # Periksa output manual atau tambahkan logika pengecekan

if __name__ == "__main__":
    unittest.main()
