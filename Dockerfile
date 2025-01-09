# Usar una imagen base de Python 3.9
FROM python:3.9

# Establecer variables de entorno
ENV PYTHONUNBUFFERED=1
ENV PORT=8501

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema si son necesarias
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     curl \
#     software-properties-common \
#     && rm -rf /var/lib/apt/lists/*

# Copiar los archivos de requerimientos
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Dar permisos de ejecución al script de configuración
RUN chmod +x setup.sh

# Ejecutar el script de configuración
RUN ./setup.sh

# Exponer el puerto que usará la aplicación
EXPOSE $PORT

# Comando para ejecutar la aplicación
CMD streamlit run app.py --server.port=$PORT