from fastapi import FastAPI, File,UploadFile
from fastapi.responses import JSONResponse
import cv2
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

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

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
    


