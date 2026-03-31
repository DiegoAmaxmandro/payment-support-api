from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Payment(BaseModel):
    amount: float
    currency: str

@app.get("/")
def home():
    return{
        "message" : "Developer Support API is running"
    }
    
    
@app.post("/payment")
def create_payment(payment: Payment):
    return{
        "status" : "approved",
        "amount" : payment.amount,
        "currency" : payment.currency
    }
    
