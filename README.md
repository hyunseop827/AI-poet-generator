# AI Poet Generator

[한국어 README](README.ko.md)

AI Poet Generator is a small Streamlit web app that creates Korean poems from a user-provided topic. It uses OpenAI through LangChain, giving users a simple interface for turning a short subject into a generated poem.

## Project Type

This project is an AI-powered creative writing tool. It is designed as a lightweight demo application for combining:

- Streamlit for the web interface
- LangChain for model integration
- OpenAI for text generation
- Python environment variables for API key configuration

## Features

- Enter a poem topic in Korean
- Generate a poem with an OpenAI chat model
- Basic API key validation before generation
- Local `.env` support through `python-dotenv`

## Requirements

- Python 3.11 or later
- OpenAI API key

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root. You can use `.env.example` as a reference:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## Run

Start the Streamlit app:

```bash
streamlit run main.py
```

Then open the local Streamlit URL shown in the terminal.

## Notes

The app is intentionally simple and focused on demonstrating a basic AI writing workflow. It can be extended with options such as poem style, tone, length, model selection, or generation history.
