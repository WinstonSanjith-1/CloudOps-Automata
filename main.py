from fastapi import FastAPI, Request, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import boto3
import os

app = FastAPI()


AWS_REGION = "ap-south-1"
S3_BUCKET_NAME = os.environ.get("AWS_S3_BUCKET")  
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY_ID") 
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")


missing_vars = [var for var, val in {
    "AWS_S3_BUCKET": S3_BUCKET_NAME,
    "AWS_ACCESS_KEY_ID": AWS_ACCESS_KEY,
    "AWS_SECRET_ACCESS_KEY": AWS_SECRET_KEY
}.items() if not val]

if missing_vars:
    print(f"⚠️ Warning: Missing required AWS environment variables: {', '.join(missing_vars)}")
    print("Ensure the environment variables are set before using AWS services.")
    s3_client = None  
else:
    
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION
    )
    print(f"✅ Connected to S3 bucket: {S3_BUCKET_NAME}")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/upload", response_class=HTMLResponse)
async def upload_page(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})


@app.post("/upload/")
async def upload_file(request: Request, file: UploadFile):
    if not s3_client:
        return templates.TemplateResponse("upload.html", {"request": request, "error": "AWS S3 is not configured properly!"})

    try:
        s3_client.upload_fileobj(file.file, S3_BUCKET_NAME, file.filename)
        return templates.TemplateResponse("upload.html", {"request": request, "message": f"File '{file.filename}' uploaded successfully"})
    except Exception as e:
        return templates.TemplateResponse("upload.html", {"request": request, "error": str(e)})


@app.get("/list-files", response_class=HTMLResponse)
async def list_files(request: Request):
    if not s3_client:
        return templates.TemplateResponse("list_files.html", {"request": request, "error": "AWS S3 is not configured properly!"})

    try:
        response = s3_client.list_objects_v2(Bucket=S3_BUCKET_NAME)
        files = [obj['Key'] for obj in response.get('Contents', [])] if 'Contents' in response else []
        return templates.TemplateResponse("list_files.html", {"request": request, "files": files})
    except Exception as e:
        return templates.TemplateResponse("list_files.html", {"request": request, "error": str(e)})
