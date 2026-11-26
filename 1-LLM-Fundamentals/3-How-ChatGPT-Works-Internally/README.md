# Simple Terminal AI Chatbot

A beginner-friendly, terminal-based AI chatbot built with Python and the OpenRouter API. It uses **Liquid LFM 3.1 1.7B (Free)** to generate AI responses directly in your terminal.

This project demonstrates how to integrate an existing Large Language Model (LLM) into a Python application using HTTP requests, without relying on complex frameworks or AI libraries.

## Features

- Interactive terminal-based conversation.
- AI-powered responses using an existing LLM.
- Free model access through OpenRouter.
- Secure API key management using environment variables.
- Simple Python implementation.
- Direct HTTP communication using the Requests library.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenRouter API | Connects the application to an AI model |
| Liquid LFM 3.1 1.7B | Generates AI responses |
| Requests | Sends HTTP requests |
| Python-dotenv | Loads environment variables |

## Project Structure

```text
3-How-ChatGPT-Works-Internally/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/niyomugaboetiene/LLM-full-course-with-projects
```

Navigate into the project directory:

```bash
cd 3-How-ChatGPT-Works-Internally
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
certifi==2026.10.23
charset-normalizer==3.5.2
idna==3.20
python-dotenv==1.2.4
requests==2.34.2
urllib3==2.8.0
```

### 3. Get your OpenRouter API key

1. Visit [OpenRouter](https://openrouter.ai/).
2. Create an account or sign in.
3. Open the [API Keys page](https://openrouter.ai/keys).
4. Create or copy your API key.

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
OPEN_ROUTER_API_KEY=your_actual_api_key
```

Replace `your_actual_api_key` with your OpenRouter API key.

**Important:** Never publish your API key or upload your `.env` file to GitHub.

### 5. Configure the AI model

The project uses:

```python
MODEL = "liquid/lfm-3-1.7b:free"
```

The model is accessed through the OpenRouter Chat Completions API.

### 6. Run the chatbot

Start the application:

```bash
python3 main.py
```

Type your message in the terminal and receive an AI-generated response.

## How It Works

The application follows a simple process:

1. Loads the OpenRouter API key from the `.env` file.
2. Gets a message from the user through terminal input.
3. Prepares the message in the format expected by the Chat Completions API.
4. Sends an HTTP POST request to OpenRouter.
5. Receives the model's response.
6. Displays the API response in the terminal.

## API Endpoint

```text
https://openrouter.ai/api/v1/chat/completions
```

## Learning Objectives

This project helps beginners understand:

- What an API is and how it works.
- How to send HTTP POST requests using Python.
- How API authentication works.
- How to use an existing Large Language Model.
- How chat messages are structured using roles and content.
- How Python applications communicate with AI models.

## Limitations

- Requires an internet connection.
- Requires a valid OpenRouter API key.
- Free model access is subject to provider availability and rate limits.
- The initial version sends a single user message per request; persistent conversation history can be added in a future version.

## Future Improvements

- Add continuous conversations using a loop.
- Maintain conversation history.
- Add an exit command.
- Display only the AI-generated answer.
- Add error handling for API failures.
- Support switching between different AI models.

## Author

**NIYOMUGABO Etiene**

Python & AI Enthusiast

GitHub: [My GitHub Profile](https://github.com/niyomugaboetiene)

## Acknowledgements

- [OpenRouter](https://openrouter.ai/) for providing access to AI models.
- [Liquid AI](https://www.liquid.ai/) for the LFM model family.

---

**Note:** This is an educational project created to explore Large Language Model API integration using Python.
