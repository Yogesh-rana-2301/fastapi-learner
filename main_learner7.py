#debug 
#cmd+shift+p to debug



from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app=FastAPI()

class Blog (BaseModel):
    title : str
    body : str
    published: Optional[bool]

@app.post ("/blog")
async def create_blog(blog:Blog):      # (name_you_will_call: class name to be done)
    return {"data":f"this is the blog title {blog.title}"}


#to change the port  (run using python3 main_leaner7.py)
#if __name__=="__main__":
#   uvicorn.run(app,host="127.0.0.1",port=9000)
