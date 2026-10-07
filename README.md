# 📚 AI Study Buddy

AI Study Buddy is a simple study assistant made using **Python, Streamlit, and OpenAI API**. It helps students understand topics, summarize notes, generate quizzes, and create flashcards.

## Features

* Explain topics in simple language
* Summarize notes
* Generate 5 MCQ questions
* Generate flashcards
* Simple and easy-to-use interface

## Technologies Used

* Python
* Streamlit
* OpenAI API

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-link>
cd AI-Study-Buddy
```

### 2. Install required libraries

```bash
pip install -r requirements.txt
```

### 3. Add your OpenAI API key

Set your API key as an environment variable:

```text
OPENAI_API_KEY=your_api_key
```

Do not add your API key directly to the code or upload it to GitHub.

### 4. Run the application

```bash
streamlit run app.py
```

## How It Works

First, the user enters a question, topic, or notes.

Then the user selects what they want the AI to do:

* Explain Simply
* Summarize Notes
* Generate Quiz
* Generate Flashcards

The selected option creates a prompt, which is sent to the OpenAI API. The generated answer is then displayed on the Streamlit page.

## Future Improvements

* Add chat history
* Add more quiz options
* Add quiz score
* Add voice input
* Add user login
* Save study notes and results

## Author

**Pranali Raundal**

Computer Engineering Student | Aspiring Software Developer
