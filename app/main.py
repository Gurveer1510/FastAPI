from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from .routers import posts, users, auth, votes
from . import models
from .database import engine

# myctx = CryptContext(schemes="bcrypt", deprecated = "auto")
# models.Base.metadata.create_all(engine)


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)


@app.get("/")
def greet_user():
    return "Hello User!"
