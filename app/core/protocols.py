from typing import Protocol

class IMessageProcessor(Protocol):
    def process(self, message: str) -> str:
        ...
