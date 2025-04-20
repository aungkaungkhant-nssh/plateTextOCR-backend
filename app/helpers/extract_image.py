from fastapi import  UploadFile
import cv2
import easyocr
from fastapi.responses import JSONResponse
import numpy as np
import asyncio
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor()

def run_ocr_sync(img):
    reader = easyocr.Reader(['en'], gpu=False)
    return reader.readtext(img)

async def extract_plate_number_from_image(file:UploadFile)-> str:
   
    contents = await file.read()
    
    npimg = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    if img is None:
        return JSONResponse(content={"error": "Image decoding failed"}, status_code=400)

    MAX_DIM = 1000
    h, w = img.shape[:2]
    if max(h, w) > MAX_DIM:
        scale = MAX_DIM / max(h, w)
        img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)

    # Run OCR in separate thread
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(executor, run_ocr_sync, img)

    # Filter high-confidence text
    threshold = 0.05
    texts = [text.strip() for _, text, conf in result if conf > threshold]

    if not texts:
        raise ValueError("No high-confidence text found")

    return " ".join(texts)