import os
import streamlit as st
import openai

# Use API key from environment variable
openai.api_key = os.getenv("AIzaSyDu44F5c_y7BHSdZwqM5Nls8vVe6vESujg")

if not openai.api_key:
    st.error("❌ OpenAI API key not found. Set the OPENAI_API_KEY environment variable.")
    st.stop()

st.set_page_config(page_title="AI Study Buddy", page_icon="📚", layout="centered")
st.title("📚 AI-Powered Study Buddy")
st.write("Ask questions, summarize notes, or generate quizzes/flashcards instantly!")

# Input area
user_input = st.text_area("Enter your question, topic, or notes:")

# Choose action
option = st.radio(
    "What do you want the AI to do?",
    ("Explain Simply", "Summarize Notes", "Generate Quiz", "Generate Flashcards")
)

# When user clicks "Get Help"
if st.button("Get Help"):
    if not user_input.strip():
        st.warning("Please enter some text first!")
    else:
        with st.spinner("AI is thinking..."):
            try:
                # Prepare prompt
                if option == "Explain Simply":
                    prompt = f"Explain this topic in simple terms for a student: {user_input}"
                elif option == "Summarize Notes":
                    prompt = f"Summarize these notes in a concise, easy-to-read format: {user_input}"
                elif option == "Generate Quiz":
                    prompt = f"Generate 5 multiple-choice questions with answers based on: {user_input}"
                elif option == "Generate Flashcards":
                    prompt = f"Generate 5 flashcards (question and answer) based on: {user_input}"

                # Use the latest OpenAI API (v1)
                response = openai.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=600
                )

                # Get AI response
                answer = response.choices[0].message.content
                st.success(answer)

            except openai.error.AuthenticationError:
                st.error("❌ Authentication failed. Check your OpenAI API key.")
            except openai.error.APIError as e:
                st.error(f"❌ OpenAI API error: {e}")
            except Exception as e:
                st.error(f"❌ An unexpected error occurred: {e}")