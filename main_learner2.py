from fastapi import FastAPI

app=FastAPI()


@app.get("/")   # GET request at root "/"
async def home():
    return {"msg": "Home page"}

@app.get("/about")   # GET request at "/about"
async def about():
    return {"msg": "About page"}

@app.get("/users/{user_id}")   # GET request at "/users/123"
async def get_user(user_id: int):
    return {"user_id": user_id}
