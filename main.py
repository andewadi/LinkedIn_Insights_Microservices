from fastapi import FastAPI
from routes import router 

app = FastAPI(title="LinkedIn Insights Microservice", version="1.0")
app.include_router(router)  
