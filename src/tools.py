# src/tools.py

from typing import Dict, List, Optional
import datetime
from zoneinfo import ZoneInfo

# Only import what this file actually needs
from google.generativeai import GenerativeModel
from google.genai import types     # ← GenerationConfig lives here in newer versions

# Relative imports from same package
from .constants import EMERGENCY_CONDITIONS, FIRST_AID_GUIDELINES

def identify_condition(condition_name: str) -> Dict:
    condition_name_lower = condition_name.lower().strip()
    
    if condition_name_lower in EMERGENCY_CONDITIONS:
        info = EMERGENCY_CONDITIONS[condition_name_lower]
        return {
            "status": "success",
            "report": {
                "condition": condition_name_lower.title(),
                **info  # unpack the dict
            }
        }
    
    # partial match logic...
    for key, info in EMERGENCY_CONDITIONS.items():
        if condition_name_lower in key or key in condition_name_lower:
            return {
                "status": "success",
                "report": {
                    "condition": key.title(),
                    **info
                }
            }
    
    return {
        "status": "error",
        "error_message": f"Condition '{condition_name}' not recognized. Try: pregnancy, epilepsy, diabetes, stroke."
    }

def get_first_aid(condition: str, specific_emergency: Optional[str] = None) -> Dict:
    condition_lower = condition.lower().strip()
    
    if condition_lower not in FIRST_AID_GUIDELINES:
        return {
            "status": "error",
            "error_message": f"No first-aid data for '{condition}'"
        }
    
    guidelines = FIRST_AID_GUIDELINES[condition_lower]
    
    if specific_emergency:
        key = specific_emergency.lower().strip()
        if key in guidelines:
            return {
                "status": "success",
                "report": {
                    "condition": condition.title(),
                    "emergency": specific_emergency.title(),
                    "steps": guidelines[key]
                }
            }
        else:
            return {
                "status": "error",
                "error_message": f"No specific guidance for '{specific_emergency}' in {condition}"
            }
    
    # return all if no specific emergency requested
    return {
        "status": "success",
        "report": {
            "condition": condition.title(),
            "guidelines": guidelines
        }
    }

def estimate_response_time(distance_to_hospital_km: float, traffic_level: str = "normal") -> Dict:
    """Estimate emergency response time based on distance and traffic."""
    # Base speeds in km/h for different traffic conditions
    traffic_speeds = {
        "light": 60,    # 60 km/h
        "normal": 40,   # 40 km/h
        "heavy": 25,    # 25 km/h
        "severe": 15    # 15 km/h
    }
    
    if traffic_level not in traffic_speeds:
        traffic_level = "normal"
    
    speed = traffic_speeds[traffic_level]
    travel_time_minutes = (distance_to_hospital_km / speed) * 60
    
    # Add preparation and dispatch time (5-10 minutes)
    prep_time = 8
    total_time = travel_time_minutes + prep_time
    
    return {
        "status": "success",
        "report": {
            "distance_km": distance_to_hospital_km,
            "traffic_level": traffic_level,
            "travel_time_minutes": round(travel_time_minutes, 1),
            "preparation_time_minutes": prep_time,
            "estimated_total_time_minutes": round(total_time, 1),
            "urgency": "critical" if total_time > 30 else "urgent" if total_time > 15 else "normal"
        }
    }

def plan_emergency_response(condition: str, severity: str = "moderate") -> Dict:
    """Create an emergency response plan based on condition and severity."""
    condition_lower = condition.lower().strip()
    severity_lower = severity.lower().strip()
    
    # Get condition information
    condition_info = identify_condition(condition_lower)
    
    # Severity levels and their implications
    severity_levels = {
        "mild": {"priority": "low", "response_time": 30, "transport": "personal_vehicle"},
        "moderate": {"priority": "medium", "response_time": 15, "transport": "ambulance_recommended"},
        "severe": {"priority": "high", "response_time": 8, "transport": "ambulance_immediate"},
        "critical": {"priority": "life_threatening", "response_time": 5, "transport": "ambulance_emergency"}
    }
    
    if severity_lower not in severity_levels:
        severity_lower = "moderate"
    
    severity_info = severity_levels[severity_lower]
    
    # Get first aid guidelines
    first_aid = get_first_aid(condition_lower)
    
    response_plan = {
        "status": "success",
        "report": {
            "condition": condition_lower,
            "severity": severity_lower,
            "priority": severity_info["priority"],
            "target_response_time_minutes": severity_info["response_time"],
            "recommended_transport": severity_info["transport"],
            "condition_details": condition_info.get("report", {}),
            "first_aid_guidelines": first_aid.get("report", {}),
            "immediate_actions": [
                "Call emergency services if severe or critical",
                "Monitor vital signs",
                "Keep patient calm and comfortable",
                "Follow first aid guidelines"
            ]
        }
    }
    
    return response_plan

def answer_general_question(question: str) -> Dict:
    try:
        model = GenerativeModel("gemini-1.5-flash")   # or "gemini-1.5-flash-002" etc.
        
        prompt = f"""You are a first-aid and emergency advisor specializing in:
- Pregnancy complications
- Epileptic seizures
- Diabetic emergencies (hypo/hyper)
- Stroke recognition & response

Answer ONLY questions related to these topics.
Provide clear, step-by-step, evidence-based advice.
Always end with: "This is not a substitute for professional medical help. Call emergency services immediately if the situation is serious."

Question: {question}"""
        
        response = model.generate_content(prompt)
        
        return {
            "status": "success",
            "report": {
                "question": question,
                "answer": response.text.strip()
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Could not generate answer: {str(e)}"
        }