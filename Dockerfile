# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Directorio de trabajo
WORKDIR /app

# Copiamos los requisitos e instalamos
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código
COPY app/ .

# Comando para arrancar la app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]