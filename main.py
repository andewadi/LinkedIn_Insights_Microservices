from fastapi import FastAPI
from routes import router  # Must match variable name in routes.py

app = FastAPI(title="LinkedIn Insights Microservice", version="1.0")
app.include_router(router)  # Include the router
