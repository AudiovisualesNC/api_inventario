from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from uvicorn.middleware.debug import PlainTextResponse
import os
import sys

####En desarrollo
# from routers import rooms
###En produccion
from .routers import rooms

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(rooms.router)

try:
    host = os.environ['MYSQL_HOST']
    user = os.environ['MYSQL_USER']
    password = os.environ['MYSQL_PASS']
    db_name = os.environ['MYSQL_DB']
except:
    sys.stderr.write(str(sys.exc_info()[0]))
    exit(1)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print(str(exc.errors()))
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
