from fastapi import FastAPI, File,UploadFile
from fastapi.responses import JSONResponse
import cv2
import numpy as np
import easyocr
from fastapi.middleware.cors import CORSMiddleware
import face_recognition
from app.routes import vehicle
from app.database import engine, Base

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)
app.include_router(vehicle.router)


reader = easyocr.Reader(['en'], gpu=False)
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/check-license")
async def check_license(file: UploadFile = File(...)):
    contents = await file.read()
    
    npimg = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    if img is None:
        return JSONResponse(content={"error": "Image decoding failed"}, status_code=400)

    result =   reader.readtext(img)

    if not result:
        return JSONResponse(content={"message": "No text detected"}, status_code=200)

    threshold = 0.05
    extracted_text = []
    for bbox, text, confidence in result:
        if confidence > threshold:
            print(text)
            extracted_text.append({
                "text": text,
            })
        else:
            print("Text confidence below threshold, not appended.")

    return JSONResponse(content={"results": extracted_text})

@app.post("/check-person")
async def check_person(file: UploadFile=File(...)):
    img =cv2.imread("./data/akk.png")
    rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img_encoding= face_recognition.face_encodings(rgb_img)[0]

    img2 =cv2.imread("./data/messi.jpeg")
    rgb_img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    img_encoding2= face_recognition.face_encodings(rgb_img2)[0]

    print(img_encoding)
    print("---------")
    print(img_encoding2)

    result =face_recognition.compare_faces([img_encoding],img_encoding2)
    print(result)
    


