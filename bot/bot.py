from WPP_Whatsapp import Create
import logging
from bot.message_handler import MessageHandler
from bot.qr_handler import QRHandler

logger = logging.getLogger(name="WPP_Whatsapp")

class WhatsAppBot:
    def __init__(self, session_name, log_qr):
        self.qr_handler = QRHandler()
        self.creator = Create(session=session_name, catchQR=self.qr_handler.catch_qr, logQR=log_qr)
        self.client = self.creator.start()
        self.message_handler = MessageHandler(self.client)

    def run(self):
        # Cek state login
        if self.creator.state != 'CONNECTED':
            raise Exception(self.creator.state)
        
        # Tambah listener untuk pesan baru
        self.creator.client.onMessage(self.message_handler.handle_message)
        self.creator.loop.run_forever()
