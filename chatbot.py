import re


def chatbot_response(user_input):
    # converting the input to lowercase to make the chatbot case-insensitive
    user_input = user_input.lower()

    # pattern matching for predefined responses
    # adding some common misspellings as well
    if re.match(r"\b(hello|hi|hey|helo)\b", user_input):
        return "Hello! How can I assist you today?"
    elif re.match(r"\b(bye|goodbye|by)\b", user_input):
        return "Goodbye! Have a great day!"
    elif re.match(r"\b(how are you\?|how are you|how are u)\b", user_input):
        return "I'm a chatbot, so I'm always functioning at full capacity!"
    elif re.match(r"\b(what is your name\?|what is your name|what's your name)\b", user_input):
        return "I am a simple rule-based chatbot."
    elif re.match(r"what can you do\?", user_input):
        return "I can respond to basic greetings and questions. Try asking me something!"
    else:
        return "I'm sorry, I don't understand that. Can you try rephrasing?"

# user and chatbot interaction

def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if re.match(r"\b(bye|goodbye|by|tata)\b", user_input.lower()):
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)


chat()
