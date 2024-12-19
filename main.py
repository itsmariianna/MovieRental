from fastapi import FastAPI
from routers import auth, movies, rentals
from dotenv import load_dotenv
import os

# Loading env variables
load_dotenv()
PORT = int(os.getenv("PORT", 8080))
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default_secret")


app = FastAPI()

@app.get("/")
def main_page():
    return {"message": "Welcome to the Movie Rental API!"}


# routers (auth, movies and rentals)
app.include_router(auth.router)
app.include_router(movies.router)
app.include_router(rentals.router)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=PORT)
