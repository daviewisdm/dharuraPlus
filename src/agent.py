# src/agent.py
import google.generativeai as genai
from typing import List, Any
import os
from dotenv import load_dotenv

load_dotenv()

from .tools import (  # Import your tools
    identify_condition,
    get_first_aid,
    estimate_response_time,
    plan_emergency_response,
    answer_general_question
)

class EmergencyAgent:
    def __init__(self):
        # Configure Google Generative AI
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction="""You are Emergency Medical Assistant, a chatbot for handling emergencies related to pregnancy, epilepsy, diabetes, and stroke.
            You can:
                1. Identify conditions and provide basic information.
                2. Give first aid instructions and plan emergency responses.
                3. Answer general questions about these conditions.
            Only answer questions related to pregnancy, epilepsy, diabetes, stroke, first aid, and emergency response.
            You can handle tasks sequentially if needed.
            Always remind users to seek professional medical help.""",
            generation_config={
                "temperature": 0.2,
                "max_output_tokens": 250,
            }
        )
        
        self.tools = {
            "identify_condition": identify_condition,
            "get_first_aid": get_first_aid,
            "estimate_response_time": estimate_response_time,
            "plan_emergency_response": plan_emergency_response,
            "answer_general_question": answer_general_question
        }
    
    def process_message(self, message: str) -> str:
        """Process a user message and return a response."""
        try:
            # Simple tool detection based on keywords
            message_lower = message.lower()
            
            if any(keyword in message_lower for keyword in ["identify", "what is", "condition", "symptoms"]):
                result = identify_condition(message)
                return f"Condition information: {result}"
            
            elif any(keyword in message_lower for keyword in ["first aid", "help", "treatment", "what to do"]):
                result = get_first_aid(message)
                return f"First aid guidance: {result}"
            
            elif any(keyword in message_lower for keyword in ["response time", "how long", "hospital", "distance"]):
                # Extract distance if mentioned
                import re
                distance_match = re.search(r'(\d+\.?\d*)\s*km', message_lower)
                if distance_match:
                    distance = float(distance_match.group(1))
                    result = estimate_response_time(distance)
                    return f"Response time estimate: {result}"
            
            elif any(keyword in message_lower for keyword in ["emergency plan", "response plan", "severity"]):
                result = plan_emergency_response(message)
                return f"Emergency response plan: {result}"
            
            # Default to general question
            result = answer_general_question(message)
            return f"General response: {result}"
            
        except Exception as e:
            return f"Error processing request: {str(e)}"

def create_emergency_agent():
    """Create and return an emergency medical agent instance."""
    return EmergencyAgent()
