# Usa la imagen base de Python 3.12
FROM python:3.12-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . /app

# Instala dependencias del sistema necesarias para `imageio` y `matplotlib`
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Instala las dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Establecer la variable de entorno PORT para Cloud Run
ENV PORT 8080

# Expone el puerto que utiliza Streamlit (Cloud Run usa el puerto 8080 por defecto)
EXPOSE 8080

# Ejecuta Streamlit en el puerto especificado por Cloud Run
CMD ["streamlit", "run", "app.py", "--server.port=${PORT}", "--server.address=0.0.0.0"]
