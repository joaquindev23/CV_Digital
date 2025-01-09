#!/bin/bash

# Crear directorio .streamlit si no existe
mkdir -p ~/.streamlit/

# Crear archivo de configuración para Streamlit
cat > ~/.streamlit/config.toml << EOL
[server]
headless = true
enableCORS = false
port = $PORT

[theme]
primaryColor = "#d33682"
backgroundColor = "#002b36"
secondaryBackgroundColor = "#586e75"
textColor = "#fff"
EOL

# Instalar dependencias
pip install -r requirements.txt