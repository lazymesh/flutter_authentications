from fastapi import FastAPI
from routes import router

# Initialize FastAPI app
app = FastAPI(title="Auth API")
app.include_router(router, prefix="")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)