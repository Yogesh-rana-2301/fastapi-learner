from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app=FastAPI()

class Blog (BaseModel):
    title : str
    body : str
    published: Optional[bool]

@app.post ("/blog")
async def create_blog(blog:Blog):      # (name_you_will_call: class name to be done)
    return {"data":f"this is the blog title {blog.title}"}

