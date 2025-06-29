from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI root!"}


@app.get("/health")
async def health_check():
    return "Ok"
