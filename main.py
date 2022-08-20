from getPdf import getPdf
from toCsv import toCsv
from toJSON import toJSON
import os
import datetime
from pydantic import BaseModel
from pathlib import Path
from fastapi import FastAPI, HTTPException
import glob
app = FastAPI()

class reqprop(BaseModel):
    content: str
    date: str

@app.post("/api/v1/get/csv/")
async def timetable(req: reqprop):
    items = ["goC.csv", "backS.csv"] 

    if req.content in items:
        current = Path()
        file_path = current / "csv" / req.content

        now = str_to_date(datetime.datetime.now().strftime("%Y-%m-%d"))
        reqdate = str_to_date(req.date)

        if reqdate != now:
            raise HTTPException(status_code=400, detail="invalid date")

        #downloadフォルダが空
        if len(glob.glob("download/*")) == 0:
            getPdf()
        
        #目的csvがない
        if req.content not in glob.glob("csv/*"):
            toCsv()

        t = os.path.getmtime(file_path)
        updated_at = str_to_date(datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d"))

    
        if updated_at == reqdate:
            response = append(toJSON(req.content),updated_at, "saved csv")
            return response
        elif updated_at != reqdate:
            #スクレイピング、ファイル生成
            getPdf()
            toCsv()
            response = append(toJSON(req.content),updated_at, "new csv")
            return response

    else:
        raise HTTPException(status_code=400, detail="file not found")

def append(response: dict, updated_at, msg):
    pdf = glob.glob("download/*")
    response.setdefault("source", pdf[0])
    response.setdefault("updated at", updated_at)
    response.setdefault("status", msg)
    return response

def str_to_date(date: str):
    date = date.split("-")
    return datetime.date(int(date[0]), int(date[1]), int(date[2]))