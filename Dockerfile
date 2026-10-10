FROM python:3.9-slim

# Install system dependencies required for Tkinter / GUI applications
RUN apt-get update && apt-get install -y \
    tk \
    tcl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]