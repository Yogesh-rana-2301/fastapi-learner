# to run uvicorn main_learner:app --reload     (it will be file_name:the app)
# 
# 
from fastapi import FastAPI            #FastAPI not FASTAPI

app=FastAPI()            #instance of FASTAPI

@app.get('/')           # what does this mean 
                        # x@ → This is a decorator in Python.
                        #app.get("/") → This tells FastAPI:
                        #“Whenever someone sends an HTTP GET request to the path /, call the function below."
                        # / is the route / path 
                        # get is the opertation on the path 
                        # @app (path operation decorator)


async def main():       # path operation function
    return {"MY NAME": "SAMEER"}