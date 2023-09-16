from typing import Union

from fastapi import FastAPI
from fastapi import Request
from fastapi.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware

import subprocess


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/latex/api/v1")
def read_root():
    return {"Hello": "World"}

@app.get("/latex/api/v1/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/latex/api/v1/texify")
async def postlatex(info : Request):
    data = await info.json()
    print(data)
    with open("example/web.tex", "w") as f:
        f.write("\documentclass[10pt,crop,varwidth]{standalone}\n")
        f.write("\\begin{document}\n")
        f.write(data["q"]+"\n")
        f.write("\end{document}\n")

    subprocess.run(["pdflatex", "-output-directory", "example", "example/web.tex"])

    return {
        "status" : "SUCCESS",
        "data" : data
    }
