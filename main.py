from fastapi import FastAPI
from uploadToDeta import uploadToDeta
from getFromDeta import getFromDetabase
from putToSoundcloud import initiate

app = FastAPI()


@app.get("/")
async def root():

    return {"message": "Hello World"}

@app.get("/scrape")
async def scrape():
    return {"message":initiate()}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
