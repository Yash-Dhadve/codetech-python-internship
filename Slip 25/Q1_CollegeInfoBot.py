# Q1_CollegeInfoBot.py
# Simple College Information Chatbot

print("College Info Bot: Hello! Ask me anything about the college. Type 'bye' to exit.\n")

college_name = "ABC Institute of Technology"
address = "123 College Road, City"
phone = "9876543210"
email = "info@abcit.edu"
courses = ["B.Sc CS", "BCA", "M.Sc CS", "MCA"]
hod = {"cs": "Dr. Sharma", "it": "Dr. Rao"}

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Bot: Thank you! Visit again.")
        break

    elif "name" in user:
        print("Bot: This is", college_name)

    elif "address" in user or "location" in user:
        print("Bot: Our college is located at:", address)

    elif "contact" in user or "phone" in user:
        print("Bot: Phone:", phone, "| Email:", email)

    elif "course" in user:
        print("Bot: Available courses are:", ", ".join(courses))

    elif "hod" in user or "department" in user:
        print("Bot: HOD (CS):", hod['cs'], "| HOD (IT):", hod['it'])

    else:
        print("Bot: Sorry, I don't know that. Try asking about courses, contact, or address.")
        

# ---------------- SAMPLE OUTPUT (not printed automatically) ----------------
SAMPLE_OUTPUT = """
You: name
Bot: This is ABC Institute of Technology

You: courses
Bot: Available courses are: B.Sc CS, BCA, M.Sc CS, MCA

You: bye
Bot: Thank you! Visit again.
"""
# ---------------------------------------------------------------------------
