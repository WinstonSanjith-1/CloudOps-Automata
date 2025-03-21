# Use a smaller base image
FROM python:3.10-alpine

# Set working directory
WORKDIR /app

# Copy only required files first (for better Docker caching)
COPY requirements.txt /app/

# Install dependencies with optimizations
RUN pip install --no-cache-dir --no-compile -r requirements.txt

# Copy remaining application files
COPY . /app

# Expose port
EXPOSE 8000

# Set environment variables (default values can be overridden at runtime)
ENV S3_BUCKET_NAME="" \
    AWS_ACCESS_KEY="" \
    AWS_SECRET_KEY="" \
    PYTHONUNBUFFERED=1 \
    UVICORN_WORKERS=1 

# Run FastAPI with a single worker to reduce memory usage
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
