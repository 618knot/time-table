from getPdf import getPdf
from toCsv import toCsv
from toJSON import toJSON
import os
from datetime import datetime
from pydantic import BaseModel
from pathlib import Path
from fastapi import FastAPI
import glob
app = FastAPI()

class reqprop(BaseModel):
    content: str
    date: str

@app.post("/api/v1/get/csv/")
async def go(req: reqprop):
    items = ["goC.csv", "backS.csv"] 

    if req.content in items:
        current = Path()
        file_path = current / "csv" / req.content

        #downloadフォルダが空
        if len(glob.glob("download/*")) == 0:
            getPdf()
        
        #目的csvがない
        if req.content not in glob.glob("csv/*"):
            toCsv()

        t = os.path.getctime(file_path)
        generated_at = datetime.fromtimestamp(t)
        generated_at = generated_at.strftime("%Y-%m-%d")
    
        if generated_at == req.date:
            response = append(toJSON(req.content),generated_at, "saved csv")
            return response
        elif generated_at != req.date:
            #スクレイピング、ファイル生成
            getPdf()
            toCsv()
            response = append(toJSON(req.content),generated_at, "new csv")
            return response

    else:
        return {"message": "error: no such file"}

def append(response: dict, generated_at, msg):
    pdf = glob.glob("download/*")
    response.setdefault("source", pdf[0])
    response.setdefault("generated at", generated_at)
    response.setdefault("status", msg)
    return response