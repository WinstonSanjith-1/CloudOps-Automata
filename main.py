from fastapi import FastAPI, Request, Form, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# AWS Configuration
AWS_REGION = "ap-south-1"
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

s3_client = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
    region_name=AWS_REGION
)
print(f"Connected to S3 bucket: {S3_BUCKET_NAME}")
# Templates setup
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/upload", response_class=HTMLResponse)
async def upload_page(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

@app.post("/upload/")
async def upload_file(request: Request, file: UploadFile):
    try:
        s3_client.upload_fileobj(file.file, S3_BUCKET_NAME, file.filename)
        return templates.TemplateResponse("upload.html", {"request": request, "message": f"File '{file.filename}' uploaded successfully"})
    except Exception as e:
        return templates.TemplateResponse("upload.html", {"request": request, "error": str(e)})

@app.get("/list-files", response_class=HTMLResponse)
async def list_files(request: Request):
    try:
        response = s3_client.list_objects_v2(Bucket=S3_BUCKET_NAME)
        files = [obj['Key'] for obj in response.get('Contents', [])]
        return templates.TemplateResponse("list_files.html", {"request": request, "files": files})
    except Exception as e:
        return templates.TemplateResponse("list_files.html", {"request": request, "error": str(e)})