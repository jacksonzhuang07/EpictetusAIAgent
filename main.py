import os
import random
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

# Mount static files (css, js, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup Templates
templates = Jinja2Templates(directory="templates")

# Load Book Text (Keep existing logic)
try:
    with open("Eichiridion.txt", "r", encoding="utf-8") as f:
        BOOK_TEXT = f.read()
except FileNotFoundError:
    BOOK_TEXT = "Error: Eichiridion.txt not found."

# Mock Data for "No API Key" Mode
MOCK_QUOTES = [
    "Some things are in our control and others not. Up to us are opinion, pursuit, desire, aversion, and, in a word, whatever are our own actions.",
    "Men are disturbed, not by things, but by the principles and notions which they form concerning things.",
    "Don't demand that things happen as you wish, but wish that they happen as they do happen, and you will go on well.",
    "If you wish your children, and your wife, and your friends to live for ever, you are stupid; for you wish to be in control of things which you cannot, you wish for things that belong to others to be your own.",
]

class UserInput(BaseModel):
    problem: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/advice")
async def get_advice(user_input: UserInput):
    # In the future, this is where the OpenAI call will go.
    # For now, we return a random quote from the book/list.
    
    # Simulate "Analysis"
    quote = random.choice(MOCK_QUOTES)
    
    return {
        "classification": "EXTERNAL (Likely)",
        "chapter": "Ref. Enchiridion",
        "action": "Accept what you cannot control.",
        "advice": quote
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)