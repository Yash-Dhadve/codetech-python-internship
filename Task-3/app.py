import streamlit as st
import json
import random
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------------------------------------
# Configuration & Setup
# ---------------------------------------------------------
# Set page configuration first (Best Practice: must be the first Streamlit command)
st.set_page_config(page_title="Professional Business Chatbot", layout="wide")

# Load spaCy model for text processing (tokenization, lemmatization)
# Note: Ensure 'en_core_web_sm' is installed in your environment
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    st.error("Model not found. Please run: python -m spacy download en_core_web_sm")

# ---------------------------------------------------------
# Data Loading & NLP Training
# ---------------------------------------------------------
# Load the 'intents' file which acts as the chatbot's knowledge base.
# It contains patterns (what user says) and responses (what bot says).
with open("intents.json", "r") as file:
    data = json.load(file)

intents = data["intents"]

# Prepare training data
# We flatten the JSON structure into two lists: one for patterns, one for tags.
all_patterns = []
tags = []

for intent in intents:
    for pattern in intent["patterns"]:
        all_patterns.append(pattern.lower())  # Normalize to lowercase for consistency
        tags.append(intent["tag"])

# Vectorization:
# Machines understand numbers, not words. TfidfVectorizer converts our text patterns
# into numerical vectors, weighing words by how unique they are (TF-IDF).
vectorizer = TfidfVectorizer()
pattern_vectors = vectorizer.fit_transform(all_patterns)


# ---------------------------------------------------------
# Core Chatbot Logic
# ---------------------------------------------------------
def get_response(user_input):
    """
    Determines the best response by comparing the user's input 
    against all known patterns using Cosine Similarity.
    """
    user_input = user_input.lower()

    # Convert user input into the same vector space as our patterns
    input_vector = vectorizer.transform([user_input])

    # Calculate Cosine Similarity:
    # This measures the "angle" between the user's vector and our pattern vectors.
    # A score closer to 1 means the text is very similar.
    similarity = cosine_similarity(input_vector, pattern_vectors)

    # Find the index of the pattern with the highest similarity score
    best_match_index = similarity.argmax()
    best_score = similarity[0][best_match_index]

    # Threshold Check:
    # If the confidence score is too low (< 0.2), the bot admits it doesn't understand
    # rather than guessing incorrectly.
    if best_score < 0.2:
        return "I’m sorry, I do not understand that yet."

    # Retrieve the tag associated with the best matching pattern
    matched_tag = tags[best_match_index]

    # specific response selection:
    # Find the intent matching the tag and pick a random response for variety.
    for intent in intents:
        if intent["tag"] == matched_tag:
            return random.choice(intent["responses"])


# ---------------------------------------------------------
# Streamlit UI Layout
# ---------------------------------------------------------
st.title("Professional Business Chatbot")
st.caption("AI-Powered Business Assistant")

# ---------------------------------------------------------
# Session State Management
# ---------------------------------------------------------
# Streamlit re-runs the entire script on every user interaction.
# We use st.session_state to persist data (chat history, input text) between re-runs.

if "messages" not in st.session_state:
    st.session_state.messages = []  # Stores tuple: (Sender, Message)

if "user_input" not in st.session_state:
    st.session_state.user_input = ""


# ---------------------------------------------------------
# Sidebar: Quick Action Buttons
# ---------------------------------------------------------
st.sidebar.title("Example Questions")

# Dynamic button generation based on intents
# Clicking a button updates the input field automatically.
for intent in intents:
    st.sidebar.markdown(f"### {intent['tag'].replace('_',' ').title()}")
    for pattern in intent["patterns"][:2]:  # Show first 2 patterns per intent
        if st.sidebar.button(pattern, key=f"btn_{pattern}"):
            st.session_state.user_input = pattern


# ---------------------------------------------------------
# Chat Interface (Bubble Design)
# ---------------------------------------------------------
# Iterate through history and display messages with custom HTML/CSS
# to differentiate between User (Right aligned) and Bot (Left aligned).
for sender, message in st.session_state.messages:
    if sender == "You":
        st.markdown(
            f"""
            <div style='text-align:right; background:#1f2937; padding:10px; 
                        border-radius:12px; margin:5px 0; color:white;'>
                <strong>You:</strong> {message}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style='text-align:left; background:#374151; padding:10px; 
                        border-radius:12px; margin:5px 0; color:white;'>
                <strong>Bot:</strong> {message}
            </div>
            """,
            unsafe_allow_html=True
        )


# ---------------------------------------------------------
# Input Area
# ---------------------------------------------------------
st.markdown("---")

# Layout: Wide input box, smaller Send/Reset buttons
col1, col2, col3 = st.columns([8, 1.5, 2])

with col1:
    # The text input is bound to session_state.user_input so sidebar buttons can update it
    user_input = st.text_input(
        "Message Input",
        value=st.session_state.user_input,
        placeholder="Type your message here...",
        label_visibility="collapsed"
    )

with col2:
    send_clicked = st.button("Send", use_container_width=True)

with col3:
    reset_clicked = st.button("Reset Chat", use_container_width=True)


# ---------------------------------------------------------
# Interaction Logic
# ---------------------------------------------------------
# Handle Reset: Clear history and reload
if reset_clicked:
    st.session_state.messages = []
    st.session_state.user_input = ""
    st.rerun()

# Handle Send: Process input, generate response, and update history
if send_clicked and user_input:
    response = get_response(user_input)

    # Append new interaction to history
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("Bot", response))

    # Clear the input field for the next message
    st.session_state.user_input = ""
    
    # Force a rerun to update the UI immediately with the new message bubbles
    st.rerun()