# Ecommerce FastAPI Backend

This project is a simple ecommerce backend built with FastAPI and MongoDB Atlas.

## Features
- Product APIs: Create and list products
- Order APIs: Create orders and get orders by user (with product details)
- Pagination and filtering support

## Folder Structure
```
app/
  main.py            # FastAPI app and route registration
  config/db.py       # MongoDB connection logic
  models/            # Pydantic models for request validation
  schemas/           # Serialization helpers
  routes/            # API endpoints
  services/          # Business logic and DB operations
run.py               # Entrypoint to run the app
requirements.txt     # Dependencies
```

## Setup
1. Add your MongoDB Atlas URI to a `.env` file as `MONGODB_URI`.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python run.py`

---
Deployable to Render/Railway. All endpoints are documented in the code.
