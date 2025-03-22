# Use a smaller base image with explicit platform
FROM --platform=linux/amd64 python:3.10-alpine

# Set working directory
WORKDIR /app

# Copy only required files first (better caching)
COPY requirements.txt /app/

# Install dependencies with optimizations
RUN pip install --no-cache-dir --no-compile -r requirements.txt

# Copy remaining application files
COPY . /app

# Expose port
EXPOSE 8000

# Set environment variables (default values can be overridden at runtime)
ENV AWS_S3_BUCKET="" \
    AWS_ACCESS_KEY_ID="" \
    AWS_SECRET_ACCESS_KEY="" \
    AWS_REGION="ap-south-1" \
    PYTHONUNBUFFERED=1 \
    UVICORN_WORKERS=1  

# Ensure script runs with correct permissions
RUN chmod +x /app/main.py

# Run FastAPI with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
