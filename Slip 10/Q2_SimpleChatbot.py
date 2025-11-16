# Q2_SimpleChatbot.py
# Simple rule-based chatbot in Python

print("ChatBot: Hello! I am a simple chatbot. Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("ChatBot: Goodbye! Have a nice day.")
        break

    elif "hello" in user or "hi" in user:
        print("ChatBot: Hello! How can I help you?")

    elif "name" in user:
        print("ChatBot: I am your Python chatbot.")

    elif "how are you" in user:
        print("ChatBot: I'm doing great! Thanks for asking.")

    elif "python" in user:
        print("ChatBot: Python is a powerful programming language widely used in AI and ML.")

    elif "ai" in user or "artificial intelligence" in user:
        print("ChatBot: AI means making machines think and behave like humans!")

    elif "help" in user:
        print("ChatBot: Tell me what you need help with. I will try my best!")

    else:
        print("ChatBot: Sorry, I didn't understand that. Can you say it differently?")


"""
ChatBot: Hello! I am a simple chatbot. Type 'bye' to exit.

You: hi
ChatBot: Hello! How can I help you?

You: what is AI?
ChatBot: AI means making machines think and behave like humans!

You: bye
ChatBot: Goodbye! Have a nice day.
"""

