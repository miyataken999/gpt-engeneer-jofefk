from fastapi import FastAPI
from models.knowledge import Knowledge
from parsers.excel_parser import ExcelParser
from parsers.image_parser import ImageParser

app = FastAPI()

@app.post("/upload_file")
async def upload_file(file: UploadFile = Depends()):
    knowledge = Knowledge()
    if file.content_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        parser = ExcelParser()
    elif file.content_type == "image/jpeg":
        parser = ImageParser()
    else:
        return {"error": "Unsupported file type"}
    knowledge.add(parser.parse(file))
    return {"message": "File uploaded successfully"}