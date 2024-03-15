from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware 
from typing import Dict
from database import *

app=FastAPI()

origins=['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/api/todo')
async def get_todo():
    response = await fetch_all_todo()
    return response

@app.get('/api/todo{title}',response_model=Todo)
async def get_todo_id(title):
    response = fetch_one_todo(title)
    if response:
        return response
    else:
        raise HTTPException(status_code=400, detail="Todo not found")
@app.post('/api/todo/post',response_model=Todo)
async def post_todo(todo:Todo):
    response=await create_todo(todo.dict())
    if response:
        return response
    else:
        raise HTTPException(status_code=400,detail="Something went wrong")
    
@app.put('/api/put/todo{title}',response_model=Todo)
async def update_todo(title:str,desc:str):
    response=await update_todo(title,desc)
    if response:
        return response
    else:
        raise HTTPException(status_code=400,detail="There is no Todo with this Title")
    
@app.delete('/api/delete/todo{title}')
async def get_todo_delete(title):
    response=await remove_todo(title)
    if response:
        return "Successfully deleted item"
    else:
        raise HTTPException(status_code=404,detail="no todo item with this title")