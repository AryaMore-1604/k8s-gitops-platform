from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Product Service", version="1.0.0")

products = [
    {"id": 1, "name": "Laptop", "price": 75000},
    {"id": 2, "name": "Keyboard", "price": 2500},
    {"id": 3, "name": "Mouse", "price": 1200},
]


@app.get("/")
def root():
    return {
        "service": "product-service",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/products")
def get_products():
    return products


Instrumentator().instrument(app).expose(app)
