FROM python:3.9

ENV PYTHONUNBUFFERED=1
ENV PORT=8501

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Crear el archivo de configuración directamente
RUN mkdir -p ~/.streamlit/ && \
    echo '[server]\nheadless = true\nenableCORS = false\nport = '$PORT'\n\n[theme]\nprimaryColor = "#d33682"\nbackgroundColor = "#002b36"\nsecondaryBackgroundColor = "#586e75"\ntextColor = "#fff"' > ~/.streamlit/config.toml

EXPOSE $PORT

CMD streamlit run app.py --server.port=$PORT --server.address=0.0.0.0