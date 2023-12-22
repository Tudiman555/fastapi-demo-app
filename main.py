from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return 'hi'

@app.get('/about')
def about(): 
    return { 'data' : 'about'}