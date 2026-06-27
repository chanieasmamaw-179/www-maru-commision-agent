from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File
import shutil


app=FastAPI()



@app.post("/upload")

async def upload(

files:list[UploadFile]=File(...)

):


    for file in files:


        with open(

            "uploads/"+file.filename,

            "wb"

        ) as buffer:


            shutil.copyfileobj(

                file.file,

                buffer

            )


    return {"status":"ok"}