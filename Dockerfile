FROM python:3.9-slim

# 1. Install system dependencies, Tkinter libraries, and Xvfb for virtual display
RUN apt-get update && apt-get install -y \
    python3-tk \
    tk \
    tcl \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# 2. Set working directory
WORKDIR /app

# 3. Copy requirements and install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of the application code
COPY . /app

# 5. Expose port if your app uses networking (optional)
EXPOSE 5000

# 6. Start Xvfb virtual display, export the display variable, and run the app
CMD Xvfb :99 -screen 0 1024x768x24 & export DISPLAY=:99 && python app.py