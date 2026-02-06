# app.py  (must be in the project root, next to src/ folder)

import cloudpickle
from src.agent import create_emergency_agent

if __name__ == "__main__":
    print("Starting agent creation...")
    try:
        agent = create_emergency_agent()
        print("Agent created successfully.")
        
        # Optional pickle save
        with open("agent.pkl", "wb") as f:
            cloudpickle.dump(agent, f)
        print("Agent saved to agent.pkl")
        
    except Exception as e:
        print("Error during agent creation:")
        print(e)
        import traceback
        traceback.print_exc()