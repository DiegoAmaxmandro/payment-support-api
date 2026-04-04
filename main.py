from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import logging

app = FastAPI()

API_KEY = "secret123"

logging.basicConfig(
    filename="api.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

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
        logging.warning("Invalid API key attempt")
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )
    
    if payment.amount <= 0:
        logging.warning(f"Invalid amount : {payment.amount}")
        raise HTTPException(
            status_code=400,
            detail="Amount must be greater than zero"
        )
    logging.info(
        f"Payment approved: {payment.amount} {payment.currency}"
    )
    
    return{
        "status" : "aproved",
        "amount" : payment.amount,
        "currency": payment.currency
    }
    
