import os
from datetime import datetime
from pydantic import BaseModel
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
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
            response = FileResponse(path = file_path, filename = f"{date}_{req.content}")
            return response
        elif generated_at != req.date:
            #スクレイピング、ファイル生成
            response = FileResponse(path = file_path, filename = f"{date}_{req.content}")
            return response
    else:
        return {"message": "error: no such file"}