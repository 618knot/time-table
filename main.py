from .toCsv import toCsv
from toJSON import toJSON
import os
from datetime import datetime
from pydantic import BaseModel
from pathlib import Path
from fastapi import FastAPI
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
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        t = os.path.getctime(file_path)
        generated_at = datetime.fromtimestamp(t)
        generated_at = generated_at.strftime("%Y-%m-%d")
    
        if generated_at == req.date:
            response = toJSON(req.content)
            response.setdefault("generated_at", generated_at)
            response.setdefault("status", "saved")
            return response
        elif generated_at != req.date:
            #スクレイピング、ファイル生成
            toCsv()
            response = toJSON(req.content)
            response.setdefault("generated_at", date)
            response.setdefault("status", "new")
            return response

    else:
        return {"message": "error: no such file"}