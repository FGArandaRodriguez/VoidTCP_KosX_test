import socket
from app.config import settings
from app.core.logger import get_logger
from app.services.message_processor import SimpleProcessor

log = get_logger("ConnectionHandler")
processor = SimpleProcessor()

def handle_client(conn: socket.socket, addr: tuple) -> None:
    """
    Maneja la comunicación con un cliente.
    """
    log.info(f"Nueva conexión desde {addr}")
    try:
        while True:
            data = conn.recv(settings.BUFFER_SIZE)
            if not data:
                break

            message = data.decode(settings.ENCODING).strip()
            log.info(f"Mensaje de {addr}: {message}")

            if message.upper() == "DESCONEXION":
                log.info(f"{addr} pidió desconexión.")
                break

            response = processor.process(message)
            conn.sendall(response.encode(settings.ENCODING))

    except Exception as e:
        log.exception(f"Error con cliente {addr}: {e}")
    finally:
        conn.close()
        log.info(f"🔌 Conexión cerrada con {addr}")
