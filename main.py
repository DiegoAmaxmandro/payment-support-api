from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

app = FastAPI()

API_KEY = "secret123"

class Payment(BaseModel):
    amount: float
    currency: str

@app.get("/")
def home():
    return{
        "message" : "Developer Support API is running"
    }
    
    
@app.post("/payment")
def create_payment(
    payment: Payment,
    x_api_key: str = Header()
):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )
    
    if payment.amount <= 0:
        raise HTTPException(
            status_code=400,
            detail="Amount must be greater than zero"
        )
    
    return{
        "status" : "aproved",
        "amount" : payment.amount,
        "currency": payment.currency
    }
    
