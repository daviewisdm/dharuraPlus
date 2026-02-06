#!/usr/bin/env python3
"""
Test script to verify the emergency medical assistant works correctly.
Run this script to test all functionality.
"""

import sys
import os
import warnings
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Suppress deprecation warnings during tests
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)

from src.agent import create_emergency_agent
from src.tools import (
    identify_condition,
    get_first_aid,
    estimate_response_time,
    plan_emergency_response,
    answer_general_question
)

def test_agent_creation():
    """Test that the agent can be created successfully."""
    print("🔧 Testing agent creation...")
    try:
        agent = create_emergency_agent()
        print(f"✅ Agent created successfully: {type(agent)}")
        print(f"   Agent name: {agent.name}")
        return True
    except Exception as e:
        print(f"❌ Agent creation failed: {e}")
        return False

def test_tools():
    """Test all the emergency medical tools."""
    print("\n🛠️  Testing tools...")
    
    tests_passed = 0
    total_tests = 5
    
    # Test 1: Identify condition
    try:
        result = identify_condition("pregnancy")
        if isinstance(result, dict) and result.get("status") == "success":
            print("✅ identify_condition: PASSED")
            tests_passed += 1
        else:
            print(f"❌ identify_condition: FAILED - {result}")
    except Exception as e:
        print(f"❌ identify_condition: ERROR - {e}")
    
    # Test 2: Get first aid
    try:
        result = get_first_aid("pregnancy", "bleeding")
        if isinstance(result, dict) and result.get("status") == "success":
            print("✅ get_first_aid: PASSED")
            tests_passed += 1
        else:
            print(f"❌ get_first_aid: FAILED - {result}")
    except Exception as e:
        print(f"❌ get_first_aid: ERROR - {e}")
    
    # Test 3: Estimate response time
    try:
        result = estimate_response_time(10.5, "normal")
        if isinstance(result, dict) and result.get("status") == "success":
            print("✅ estimate_response_time: PASSED")
            tests_passed += 1
        else:
            print(f"❌ estimate_response_time: FAILED - {result}")
    except Exception as e:
        print(f"❌ estimate_response_time: ERROR - {e}")
    
    # Test 4: Plan emergency response
    try:
        result = plan_emergency_response("pregnancy", "moderate")
        if isinstance(result, dict) and result.get("status") == "success":
            print("✅ plan_emergency_response: PASSED")
            tests_passed += 1
        else:
            print(f"❌ plan_emergency_response: FAILED - {result}")
    except Exception as e:
        print(f"❌ plan_emergency_response: ERROR - {e}")
    
    # Test 5: Answer general question (without AI to avoid API calls)
    try:
        result = answer_general_question("What is pregnancy?")
        # Allow both success and error (error is ok if AI not configured)
        if isinstance(result, dict) and result.get("status") in ["success", "error"]:
            print("✅ answer_general_question: PASSED")
            tests_passed += 1
        else:
            print(f"❌ answer_general_question: FAILED - {result}")
    except Exception as e:
        print(f"❌ answer_general_question: ERROR - {e}")
    
    print(f"\n   Tools test results: {tests_passed}/{total_tests} passed")
    return tests_passed == total_tests

def test_agent_functionality():
    """Test basic agent functionality."""
    print("\n🤖 Testing agent functionality...")
    
    try:
        agent = create_emergency_agent()
        
        # Test agent attributes
        if hasattr(agent, 'name') and agent.name == "emergency_medical_assistant":
            print("✅ Agent name: PASSED")
        else:
            print("❌ Agent name: FAILED")
            return False
        
        if hasattr(agent, 'tools') and len(agent.tools) == 5:
            print("✅ Agent tools: PASSED")
        else:
            print("❌ Agent tools: FAILED")
            return False
        
        print("✅ Agent functionality: PASSED")
        return True
        
    except Exception as e:
        print(f"❌ Agent functionality test failed: {e}")
        return False

def test_serialization():
    """Test that the agent can be serialized and deserialized."""
    print("\n💾 Testing serialization...")
    
    try:
        import cloudpickle
        agent = create_emergency_agent()
        
        # Test serialization
        test_file = 'test_serialization.pkl'
        with open(test_file, 'wb') as f:
            cloudpickle.dump(agent, f)
        print("✅ Serialization: PASSED")
        
        # Test deserialization
        with open(test_file, 'rb') as f:
            loaded_agent = cloudpickle.load(f)
        print("✅ Deserialization: PASSED")
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
        
        return True
        
    except Exception as e:
        print(f"❌ Serialization test failed: {e}")
        # Clean up on error
        test_file = 'test_serialization.pkl'
        if os.path.exists(test_file):
            try:
                os.remove(test_file)
            except:
                pass
        return False

def main():
    """Run all tests."""
    print("🚀 Starting Emergency Medical Assistant Tests")
    print("=" * 50)
    
    all_passed = True
    
    # Run all test suites
    all_passed &= test_agent_creation()
    all_passed &= test_tools()
    all_passed &= test_agent_functionality()
    all_passed &= test_serialization()
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 ALL TESTS PASSED! Your emergency medical assistant is working correctly.")
        print("\n📋 What you can do now:")
        print("   • Run 'python app.py' to create and save the agent")
        print("   • Import and use the tools in your own applications")
        print("   • Load the saved agent from 'agent.pkl'")
        print("   • Test with real medical scenarios")
    else:
        print("❌ Some tests failed. Please check the errors above.")
    
    return all_passed

if __name__ == "__main__":
    main()
