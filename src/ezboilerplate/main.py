from fastapi import FastAPI

app = FastAPI(title="Un'applicazione veramente crasta")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/hello")
async def hello():
    return {"message": "Ciao niko"}
