import os
import json

# 1. Knowledge Base Loader
def get_kb():
    # Folder check for knowledge.json
    base_path = os.path.dirname(__file__)
    # Agar venv ke andar hai toh 'venv/knowledge.json' kar dena
    file_path = os.path.join(base_path, 'knowledge.json') 
    with open(file_path, 'r') as f:
        return json.load(f)

# 2. Simple Intent Classifier (Bypassing LLM to fix 404 error)
def get_intent(user_input):
    ui = user_input.lower()
    if any(word in ui for word in ['hi', 'hello', 'hey', 'greetings']):
        return 'greeting'
    elif any(word in ui for word in ['price', 'pricing', 'plan', 'cost', 'features']):
        return 'pricing'
    elif any(word in ui for word in ['buy', 'sign up', 'purchase', 'get started', 'subscribe', 'want']):
        return 'lead'
    return 'other'

# 3. Simple Agent State
user_data = {"name": None, "email": None, "platform": None}

def run_agent():
    print("\n--- AutoStream AI Agent is LIVE (Offline Mode) ---")
    try:
        kb = get_kb()
    except FileNotFoundError:
        print("Error: knowledge.json nahi mili! Use venv folder se bahar nikaalein.")
        return

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['exit', 'quit']: break
        
        intent = get_intent(user_input)

        if intent == 'greeting':
            print("Agent: Hello! Welcome to AutoStream. How can I help you today?")

        elif intent == 'pricing':
            print(f"Agent: We have two plans: Pro ({kb['pricing']['Pro Plan']}) and Basic ({kb['pricing']['Basic Plan']}).")
        
        elif intent == 'lead' or user_data['name'] is not None:
            if not user_data['name']:
                print("Agent: I can help you with that! What is your name?")
                user_data['name'] = input("Your Name: ")
            
            if not user_data['email']:
                print(f"Agent: Thanks {user_data['name']}! What is your email?")
                user_data['email'] = input("Your Email: ")
                
            if not user_data['platform']:
                print("Agent: One last thing, which creator platform do you use (YouTube/Insta)?")
                user_data['platform'] = input("Your Platform: ")
                
            # Requirement 3.3: Mock Tool Trigger
            print(f"\n✅ [TOOL] Lead Captured Successfully: {user_data['name']}, {user_data['email']}, {user_data['platform']}")
            print("Agent: You're all set! Our team will contact you soon.")
            break 
            
        else:
            print("Agent: That sounds interesting! Can you tell me more or ask about our pricing?")

if __name__ == "__main__":
    run_agent()