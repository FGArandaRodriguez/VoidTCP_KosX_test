import socket
from app.config import settings
from app.core.logger import get_logger

log = get_logger("Client")

def start_client():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(("servidor", settings.PORT))
            log.info("Conectado al servidor.")

            while True:
                msg = input("👉 Ingresa mensaje: ").strip()
                client.sendall(msg.encode(settings.ENCODING))

                if msg.upper() == "DESCONEXION":
                    log.info("Cerrando cliente.")
                    break

                response = client.recv(settings.BUFFER_SIZE).decode(settings.ENCODING)
                print(f"🧾 Respuesta: {response}")

    except Exception as e:
        log.exception(f"Error en cliente: {e}")

if __name__ == "__main__":
    start_client()
