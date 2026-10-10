FROM python:3.9-slim

# Install Tkinter, Xvfb, VNC server, lightweight window manager (Fluxbox), and noVNC
RUN apt-get update && apt-get install -y \
    python3-tk \
    tk \
    tcl \
    xvfb \
    x11vnc \
    fluxbox \
    novnc \
    websockify \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Expose noVNC web port
EXPOSE 8080

# Launch Xvfb display, window manager, VNC server, noVNC web bridge, and Python app
CMD Xvfb :99 -screen 0 1024x768x24 & \
    sleep 1 && \
    export DISPLAY=:99 && \
    fluxbox & \
    x11vnc -display :99 -forever -nopw -shared -rfbport 5900 & \
    websockify --web /usr/share/novnc/ 8080 localhost:5900 & \
    python app.py