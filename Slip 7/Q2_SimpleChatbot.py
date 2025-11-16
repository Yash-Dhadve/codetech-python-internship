# Q2_SimpleChatbot.py
# Simple rule-based chatbot in Python

print("Hello! I am ChatBot. Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("ChatBot: Goodbye! Have a nice day.")
        break

    elif "hello" in user or "hi" in user:
        print("ChatBot: Hello! How can I help you?")

    elif "name" in user:
        print("ChatBot: I am a simple Python chatbot created for your practical.")

    elif "how are you" in user:
        print("ChatBot: I am good! Thank you for asking.")

    elif "your purpose" in user or "what can you do" in user:
        print("ChatBot: I can answer simple questions using rule-based responses.")

    elif "python" in user:
        print("ChatBot: Python is a powerful programming language used in AI, ML, and web development.")

    elif "ai" in user or "artificial intelligence" in user:
        print("ChatBot: AI is the ability of machines to mimic human intelligence.")

    else:
        print("ChatBot: Sorry, I don't understand that. Please try again.")



"""
Hello! I am ChatBot. Type 'bye' to exit.

You: hi
ChatBot: Hello! How can I help you?

You: what is python?
ChatBot: Python is a powerful programming language used in AI, ML, and web development.

You: bye
ChatBot: Goodbye! Have a nice day.
"""
