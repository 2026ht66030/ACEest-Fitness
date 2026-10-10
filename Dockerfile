FROM python:3.9-slim

# Install system dependencies, Tkinter libraries, and Xvfb for virtual display
RUN apt-get update && apt-get install -y \
    tk \
    tcl \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN dnf install -y python3-tkinter

COPY . .

EXPOSE 5000

# Use xvfb-run to provide a virtual display environment for Tkinter
CMD ["xvfb-run", "python", "app.py"]