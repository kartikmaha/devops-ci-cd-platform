# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependency file first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Environment variables (can be overridden by Jenkins)
ENV ENVIRONMENT=dev
ENV APP_VERSION=1.0.0
ENV BUILD_NUMBER=manual
ENV GIT_COMMIT=local

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
