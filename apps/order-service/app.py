from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Order Service", version="1.0.0")

orders = [
    {"id": 101, "customer": "Arya", "product": "Laptop", "status": "Delivered"},
    {"id": 102, "customer": "Rahul", "product": "Keyboard", "status": "Shipped"},
    {"id": 103, "customer": "Priya", "product": "Mouse", "status": "Processing"},
]

@app.get("/")
def root():
    return {
        "service": "order-service",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/orders")
def get_orders():
    return orders

Instrumentator().instrument(app).expose(app)
