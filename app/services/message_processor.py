from app.core.protocols import IMessageProcessor

class SimpleProcessor:
    def process(self, message: str) -> str:
        return message.upper()
