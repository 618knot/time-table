from datetime import datetime
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
app = FastAPI()

@app.get("/get_csv/v1/{filename:path}")
async def go(filename: str):
    current = Path()
    file_path = current / "csv" / filename
    now = datetime.now()

    response = FileResponse(path = file_path)
    return response