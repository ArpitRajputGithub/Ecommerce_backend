from fastapi import FastAPI
from app.routes import product_routes
from app.routes import order_routes

app = FastAPI()

app.include_router(product_routes.router)
app.include_router(order_routes.router)

@app.get("/")
def read_root():
    return {"message": "Ecommerce backend for HRone"}

@app.get("/health")
def health_check():
    return {"status": "ok"}