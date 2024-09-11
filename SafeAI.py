# Dictionary of safety recommendations
safety_tips = {
    "travel": "When traveling, avoid isolated areas, use trusted transport, and share your location with family or friends.",
    "self-defense": "Carry a safety tool like pepper spray and learn basic self-defense moves to protect yourself.",
    "emergency": "In case of emergency, contact local authorities, use emergency apps, and stay in public spaces."
}

def get_safety_response(user_input):
    """Check if the input is asking for specific safety advice."""
    user_input = user_input.lower()
    if "travel safety" in user_input:
        return safety_tips['travel']
    elif "self-defense" in user_input:
        return safety_tips['self-defense']
    elif "emergency" in user_input:
        return safety_tips['emergency']
    else:
        return "I'm sorry, I don't have information on that topic yet because, I'm still beeing constructed."

def chat():
    print("Women's Safety AI Chatbot.(safeAI) Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() == 'quit':
            print("Chatbot: Stay safe! Goodbye!")
            break
        
        # Check for specific safety recommendations
        response = get_safety_response(user_input)
        print(f"SafeAI: {response}")

# Start chatting
chat()