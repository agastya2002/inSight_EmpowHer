import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from profanity_check import predict, predict_prob
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {"Home page"}

########################### Profanity Checker ###############################
@app.get("/prof/{message}")
def sent(message : str):
    binPred = predict([message])
    probPred = predict_prob([message])
      
    dct = {"bin":str(binPred[0]), "prob":str(probPred[0])}
    jsonData = jsonable_encoder(dct)
    return JSONResponse(jsonData)
    
if __name__ == "__main__":
  uvicorn.run("app:app", host="0.0.0.0", port=8080) 
