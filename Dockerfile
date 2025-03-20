FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Set environment variables (default values can be overridden at runtime)
ENV S3_BUCKET_NAME="" \
    AWS_ACCESS_KEY="" \
    AWS_SECRET_KEY=""

# Command to run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
