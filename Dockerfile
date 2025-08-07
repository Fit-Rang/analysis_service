# Dockerfile
FROM python:3.11-slim

# Install build dependencies and libpq for PostgreSQL support
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Default command
CMD ["./run.sh"]

