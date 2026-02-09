# Q2_SimpleChatbot.py
# Simple rule-based chatbot in Python

print("ChatBot: Hello! I am your simple chatbot. Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("ChatBot: Goodbye! Have a nice day.")
        break

    elif "hello" in user or "hi" in user:
        print("ChatBot: Hello! How can I help you?")

    elif "name" in user:
        print("ChatBot: My name is SimpleBot.")

    elif "how are you" in user:
        print("ChatBot: I'm doing great, thank you!")

    elif "python" in user:
        print("ChatBot: Python is an easy and powerful programming language.")

    elif "college" in user:
        print("ChatBot: Your college is really good for education and activities.")

    else:
        print("ChatBot: Sorry, I didn't understand. Try asking something else.")


