from fastapi import  UploadFile
import cv2
import easyocr
from fastapi.responses import JSONResponse
import numpy as np

async def extract_plate_number_from_image(file:UploadFile)-> str:
    reader = easyocr.Reader(['en'], gpu=False)
    contents = await file.read()
    
    npimg = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    if img is None:
        return JSONResponse(content={"error": "Image decoding failed"}, status_code=400)

    result = reader.readtext(img)

    if not result:
        return JSONResponse(content={"message": "No text detected"}, status_code=200)

    threshold = 0.05
    texts = []

    for _, text, confidence in result:
        if confidence > threshold:
            texts.append(text.strip())

    if not texts:
        return JSONResponse(content={"message": "No high-confidence text found"}, status_code=200)

   
    plate_number = " ".join(texts)
    return plate_number;