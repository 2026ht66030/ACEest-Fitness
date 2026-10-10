FROM python:3.9-slim

# Install system dependencies, Tkinter, Xvfb, VNC, and web tools
RUN apt-get update && apt-get install -y \
    python3-tk \
    tk \
    tcl \
    xvfb \
    x11vnc \
    fluxbox \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

# Create a startup script or command to launch Xvfb, a window manager, the VNC server, and your app
# (For simplicity, we can run them sequentially or via a start script)
CMD Xvfb :99 -screen 0 1024x768x24 & \
    export DISPLAY=:99 && \
    fluxbox & \
    x11vnc -display :99 -forever -nopw -listen localhost -xkb & \
    python app.py