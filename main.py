from fastapi import FastAPI, File,UploadFile
from fastapi.responses import JSONResponse
import cv2
import numpy as np
import easyocr

app = FastAPI()
reader = easyocr.Reader(['en'], gpu=False)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    
    npimg = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    if img is None:
        return JSONResponse(content={"error": "Image decoding failed"}, status_code=400)

    result = reader.readtext(img)

    if not result:
        return JSONResponse(content={"message": "No text detected"}, status_code=200)

    threshold = 0.05
    extracted_text = []
    for bbox, text, confidence in result:
        print(f"Detected text: {text}, Confidence: {confidence}")
        if confidence > threshold:
            extracted_text.append({
                "text": text,
            })
        else:
            print("Text confidence below threshold, not appended.")

    return JSONResponse(content={"results": extracted_text})
