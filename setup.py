import os

BASE_DIR = "tcp_app"

estructura = {
    "app": {
        "config": ["__init__.py", "settings.py"],
        "core": ["__init__.py", "logger.py", "protocols.py"],
        "services": ["__init__.py", "message_processor.py"],
        "handlers": ["__init__.py", "connection_handler.py"],
        "client_app": ["run_client.py"],
        "server_app": ["run_server.py"]
    },
    "tests": ["test_protocol.py"],
    "docker": ["Dockerfile", "docker-compose.yml"],
    "": [".dockerignore", "requirements.txt", "README.md"]
}

def crear_estructura():
    print(f"[🚀] Creando proyecto en '{BASE_DIR}'")
    os.makedirs(BASE_DIR, exist_ok=True)

    for carpeta, archivos in estructura.items():
        if isinstance(archivos, list):
            ruta_carpeta = os.path.join(BASE_DIR, carpeta) if carpeta else BASE_DIR
            os.makedirs(ruta_carpeta, exist_ok=True)
            for archivo in archivos:
                ruta_archivo = os.path.join(ruta_carpeta, archivo)
                with open(ruta_archivo, 'w') as f:
                    f.write("")  # placeholder vacío
                print(f"    📄 {ruta_archivo}")
        elif isinstance(archivos, dict):
            for subcarpeta, subarchivos in archivos.items():
                ruta_subcarpeta = os.path.join(BASE_DIR, carpeta, subcarpeta)
                os.makedirs(ruta_subcarpeta, exist_ok=True)
                for archivo in subarchivos:
                    ruta_archivo = os.path.join(ruta_subcarpeta, archivo)
                    with open(ruta_archivo, 'w') as f:
                        f.write("")  # placeholder vacío
                    print(f"    📄 {ruta_archivo}")

    print("[✅] Estructura creada correctamente.")

if __name__ == "__main__":
    crear_estructura()
