from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# 1. Import the actual ADK components
from google.adk.agents import Agent 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Initialize your Agent (do this outside the function so it only loads once)
my_agent = Agent(
    name="React-Assistant",
    instructions="You are an AI helper for my React app."
)

@app.get("/api/chat")
async def chat_with_adk(user_message: str):
    # 3. Use the ADK to get a response
    response = await my_agent.run(user_message)
    
    # 4. Return it to React
    return {"status": "success", "reply": response.text}