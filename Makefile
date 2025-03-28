# VARIABLES
COMPOSE = docker-compose -f docker/docker-compose.yml

# -------------------------
# Construcción
# -------------------------
build:
	$(COMPOSE) build

# -------------------------
# Arranque del servidor
# -------------------------
up:
	$(COMPOSE) up servidor -d

# -------------------------
# Ejecutar cliente interactivo
# -------------------------
client:
	$(COMPOSE) run cliente

# -------------------------
# Pruebas unitarias (locales)
# -------------------------
test:
	pytest tests/

# -------------------------
# Limpiar contenedores
# -------------------------
down:
	$(COMPOSE) down

# -------------------------
# Limpiar imágenes y volúmenes
# -------------------------
clean:
	$(COMPOSE) down --rmi all --volumes --remove-orphans

# -------------------------
# Ayuda
# -------------------------
help:
	@echo "__> Comandos disponibles:"
	@echo "  make build     => Construye la imagen docker"
	@echo "  make up        => Inicia el servidor TCP"
	@echo "  make client    => Ejecuta el cliente TCP"
	@echo "  make test      => Ejecuta pruebas unitarias con pytest"
	@echo "  make down      => Detiene los servicios"
	@echo "  make clean     => Limpia todo (contenedores, volúmenes, imágenes)"
