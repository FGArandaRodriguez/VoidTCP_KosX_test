FROM python:3.10-slim

RUN apt-get update && apt-get install -y netcat-openbsd

WORKDIR /app

COPY app /app/app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "app.server_app.run_server"]
