#path parameter
#prefer to use swagger instead of redoc (just use /docs or /redoc)



from fastapi import FastAPI            

app=FastAPI()            

@app.get('/')          
async def index():      
    return {"data":"bloglist"}


@app.get('/blog/unpublished')
async def unpublished():
    
    #and also typecasted to int (if not int then error)
    #so any @app.get('/blog/unpublished') should give the error
    return {"data": "not yet published"}


@app.get('/blog/{id}')
async def blog(id: int):
    #fetch the blog with id==id
    #and also typecasted to int (if not int then error)
    #so any @app.get('/blog/unpublished') should give the error
    return {"data": id}



# two functions in one is wrong (have if else elif condition for that)
# async def blog(id: int):
    #fetch the blog with id==id
    #and also typecasted to int (if not int then error)
    #so any @app.get('/blog/unpublished') should give the error
#    return {"data": id*2}



#the following is not correct{
#@app.get('/blog/unpublished')
#async def unpublished():
    
    #and also typecasted to int (if not int then error)
    #so any @app.get('/blog/unpublished') should give the error
#    return {"data": "not yet published"}
#}

@app.get('/blog/{id}/comments')
async def blog(id: int):     #under the hood is pydantic 
    #fetch comments of blog with id 
    return {"data": {'1','2','3'}}




