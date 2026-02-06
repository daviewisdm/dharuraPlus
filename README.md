# DharuraPlus - Emergency Medical Assistant

An AI-powered emergency medical assistant that provides information and guidance for pregnancy complications, epilepsy, diabetes, and stroke emergencies.

## Features

- **Condition Identification**: Identify and provide information about emergency medical conditions
- **First Aid Guidance**: Get step-by-step first aid instructions for specific emergencies
- **Response Time Estimation**: Calculate emergency response times based on distance and traffic conditions
- **Emergency Response Planning**: Create comprehensive emergency response plans based on condition severity
- **General Medical Q&A**: Answer general questions about supported medical conditions

## Supported Conditions

- Pregnancy complications
- Epileptic seizures
- Diabetic emergencies (hypoglycemia/hyperglycemia)
- Stroke recognition and response

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd dharuraPlus
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix/MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Create a .env file with your Google API key
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_CLOUD_PROJECT=your_project_name
GOOGLE_CLOUD_LOCATION=your_location
GOOGLE_CLOUD_STORAGE_BUCKET=your_bucket_name
```

## Usage

### Running the Application

```bash
python app.py
```

This will:
- Create the emergency medical agent
- Save the agent to `agent.pkl` for later use
- Display success/error messages

### Using the Tools

You can also use the individual tools directly:

```python
from src.tools import (
    identify_condition,
    get_first_aid,
    estimate_response_time,
    plan_emergency_response,
    answer_general_question
)

# Identify a condition
result = identify_condition("pregnancy")
print(result)

# Get first aid guidance
first_aid = get_first_aid("pregnancy", "bleeding")
print(first_aid)

# Estimate response time
response_time = estimate_response_time(10.5, "heavy")
print(response_time)

# Plan emergency response
plan = plan_emergency_response("pregnancy", "severe")
print(plan)

# Answer general questions
answer = answer_general_question("What are the symptoms of pre-eclampsia?")
print(answer)
```

## Project Structure

```
dharuraPlus/
├── src/
│   ├── __init__.py
│   ├── agent.py          # Main agent implementation
│   ├── tools.py          # Emergency response tools
│   └── constants.py      # Medical condition data
├── app.py                # Main application entry point
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create this)
├── agent.pkl            # Serialized agent (created by app.py)
└── README.md            # This file
```

## API Reference

### Tools

#### `identify_condition(condition_name: str) -> Dict`
Identifies and returns information about a specific emergency condition.

**Parameters:**
- `condition_name`: Name of the medical condition

**Returns:** Dictionary with condition information or error message

#### `get_first_aid(condition: str, specific_emergency: Optional[str] = None) -> Dict`
Provides first aid guidelines for a specific condition.

**Parameters:**
- `condition`: Medical condition name
- `specific_emergency`: Optional specific emergency type

**Returns:** Dictionary with first aid steps or error message

#### `estimate_response_time(distance_to_hospital_km: float, traffic_level: str = "normal") -> Dict`
Estimates emergency response time based on distance and traffic.

**Parameters:**
- `distance_to_hospital_km`: Distance to nearest hospital in kilometers
- `traffic_level`: Traffic condition ("light", "normal", "heavy", "severe")

**Returns:** Dictionary with time estimates and urgency level

#### `plan_emergency_response(condition: str, severity: str = "moderate") -> Dict`
Creates an emergency response plan based on condition and severity.

**Parameters:**
- `condition`: Medical condition name
- `severity`: Severity level ("mild", "moderate", "severe", "critical")

**Returns:** Comprehensive emergency response plan

#### `answer_general_question(question: str) -> Dict`
Answers general medical questions using AI.

**Parameters:**
- `question`: Medical question

**Returns:** AI-generated answer with medical disclaimer

## Dependencies

- `google-generativeai`: Google Generative AI for question answering
- `python-dotenv`: Environment variable management
- `cloudpickle`: Object serialization
- `thefuzz`: Fuzzy string matching
- `rapidfuzz`: Fast string matching

## Disclaimer

**This application is for informational purposes only and is not a substitute for professional medical advice.**

- Always call emergency services (911 or local emergency number) for serious medical situations
- Consult healthcare professionals for medical concerns
- This tool provides guidance but cannot replace professional medical judgment

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]

## Support

For issues and questions, please create an issue in the repository or contact the development team.
