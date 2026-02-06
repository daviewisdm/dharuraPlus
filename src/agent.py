# src/agent.py

from google.adk.agents import Agent
from google.genai import types

from .tools import (
    identify_condition,
    get_first_aid,
    estimate_response_time,
    plan_emergency_response,
    answer_general_question
)

# Define the agent as a top-level variable (this is what ADK looks for)
root_agent = Agent(
    name="emergency_medical_assistant",
    model="gemini-2.5-flash",  # or gemini-1.5-flash-exp / whatever you're using
    description=(
        "Agent supporting emergency response for pregnancy, epilepsy, diabetes, and stroke. "
        "Provides information on conditions, first aid, response planning, and general advice."
    ),
    instruction="""You are Emergency Medical Assistant, a chatbot for handling emergencies related to pregnancy, epilepsy, diabetes, and stroke.
        You can:
            1. Identify conditions and provide basic information.
            2. Give first aid instructions and plan emergency responses.
            3. Answer general questions about these conditions.
        Only answer questions related to pregnancy, epilepsy, diabetes, stroke, first aid, and emergency response.
        You can handle tasks sequentially if needed.
        Always remind users to seek professional medical help.
    """,
    tools=[
        identify_condition,
        get_first_aid,
        estimate_response_time,
        plan_emergency_response,
        answer_general_question
    ],
    generate_content_config=types.GenerateContentConfig(
        temperature=0.2,
        max_output_tokens=250
    )
)

def create_emergency_agent():
    """Create and return an emergency medical agent instance."""
    return root_agent