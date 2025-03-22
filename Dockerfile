
FROM --platform=linux/amd64 python:3.10-alpine

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir --no-compile -r requirements.txt

COPY . /app

EXPOSE 8000

ENV AWS_S3_BUCKET="" \
    AWS_ACCESS_KEY_ID="" \
    AWS_SECRET_ACCESS_KEY="" \
    AWS_REGION="ap-south-1" \
    PYTHONUNBUFFERED=1 \
    UVICORN_WORKERS=1  

RUN chmod +x /app/main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
