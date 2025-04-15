from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

from routes import router

# origins = [
#     "http://localhost:3000",
#     "http://localhost:8080",
#     "http://localhost:62233",
#     "http://127.0.0.1:62233",
# ]


# Initialize FastAPI app
app = FastAPI(title="Auth API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods='*',
    allow_headers='*'
)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)