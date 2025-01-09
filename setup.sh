#!/bin/bash

# Crear directorio .streamlit si no existe
mkdir -p ~/.streamlit/

# Crear archivo de configuración para Streamlit
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]\n\
primaryColor = '#d33682'\n\
backgroundColor = '#002b36'\n\
secondaryBackgroundColor = '#586e75'\n\
textColor = '#fff'\n\
" > ~/.streamlit/config.toml

# Instalar dependencias (puedes agregar más aquí si es necesario)
pip install -r requirements.txt

# Ejecución de Streamlit en el puerto especificado (default es 8501 si no se pasa PORT)
streamlit run app.py
