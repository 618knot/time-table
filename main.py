from datetime import datetime
from pydantic import BaseModel
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
app = FastAPI()

@app.get("/api/v1/get/csv/{filename:path}")
async def go(filename: str):
    current = Path()
    file_path = current / "csv" / filename
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    
    response = FileResponse(path = file_path, filename = f"{date}_{filename}")
    return response

class reqprop(BaseModel):
    content: str
    date: str


@app.post("/api/v1/get/csv/")
async def go(req: reqprop):
    current = Path()
    file_path = current / "csv" / req.content
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    
    response = FileResponse(path = file_path, filename = f"{date}_{req.content}")
    return response
