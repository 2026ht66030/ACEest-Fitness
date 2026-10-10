FROM python:3.9-slim

# Install system dependencies, Tkinter libraries, and Xvfb for virtual display
RUN apt-get update && apt-get install -y \
    tk \
    tcl \
    python3-tk \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# Wrap the execution with xvfb-run to provide a virtual display environment for Tkinter
CMD ["xvfb-run", "python", "app.py"]