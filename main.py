from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from routes import pessoas

app = FastAPI(title="Backend Mentoria")

origins = ["*"]

# permitir métodos, origens, e headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pessoas.router)


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=6000
        # ssl_keyfile=r"C:\certificate\keypy.pem",
        # ssl_certfile=r"C:\certificate\certpy.pem"
    )