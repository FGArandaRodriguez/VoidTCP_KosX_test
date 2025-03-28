import socket
import time

HOST = "localhost"
PORT = 5000
ENCODING = "utf-8"
BUFFER_SIZE = 1024

def test_uppercase_response():
    """
    Prueba que el servidor responda con el mensaje en mayúsculas.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        client.sendall("hola servidor".encode(ENCODING))

        response = client.recv(BUFFER_SIZE).decode(ENCODING)
        assert response == "HOLA SERVIDOR", f"Respuesta inesperada: {response}"

        client.sendall("DESCONEXION".encode(ENCODING))
        time.sleep(1)

def test_desconexion_cierra_conexion():
    """
    Prueba que el servidor cierre la conexión al recibir 'DESCONEXION'.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        client.sendall("DESCONEXION".encode(ENCODING))

        time.sleep(1)
        try:
            # Intentamos enviar otro mensaje
            client.sendall("aun aqui?".encode(ENCODING))
            response = client.recv(BUFFER_SIZE)
            assert not response, "El servidor no cerró la conexión como se esperaba."
        except (ConnectionResetError, BrokenPipeError):
            assert True
