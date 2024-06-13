class MessageHandler:
    def __init__(self, client):
        self.client = client

    def handle_message(self, message):
        if message and not message.get("isGroupMsg"):
            chat_id = message.get("from")
            message_id = message.get("id")
            body = message.get("body")
            if "السلام عليكم" in body:
                self.client.reply(chat_id, "وعليكم السلام", message_id)
            else:
                self.client.reply(chat_id, "Welcome", message_id)
