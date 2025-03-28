import socket
import threading
from app.handlers.connection_handler import handle_client
from app.config import settings
from app.core.logger import get_logger

log = get_logger("Server")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((settings.HOST, settings.PORT))
        server.listen()

        log.info(f"Servidor escuchando en {settings.HOST}:{settings.PORT}")

        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()

if __name__ == "__main__":
    start_server()
