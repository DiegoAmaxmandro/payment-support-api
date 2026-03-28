from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{
        "message" : "Developer Support API is running"
    }