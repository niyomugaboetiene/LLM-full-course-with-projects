# Simple LLM Project – Building an AI Question & Answer Application

## About the Project

This project is a beginner-friendly Large Language Model (LLM) application built with Python and the GEMINI API.

The main goal is to understand how applications communicate with Large Language Models through HTTP requests without depending on frameworks such as LangChain or the official OpenAI SDK.

The application allows users to enter questions and receive AI-generated answers using Google's **Gemini 3.8 Flash** model.

This project is also part of my journey to understand Generative AI and learn how to build real-world LLM-powered applications from scratch.

## Project Objectives

Through this project, I aim to understand:

- What Large Language Models (LLMs) are.
- How applications communicate with AI models.
- How HTTP and HTTPS requests work.
- How to use REST APIs with Python.
- How to authenticate API requests using API keys.
- How JSON is used to send and receive data.
- How prompts are sent to an LLM.
- How to receive and extract AI-generated responses.
- How to handle API errors and understand HTTP status codes.
- How to securely manage API keys using environment variables.
- How to save AI conversations and responses.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Requests | Sending HTTP requests |
| Python-dotenv | Loading environment variables |
| Gemini 3.8 Flash | Language model used to generate responses |
| JSON | Sending and receiving structured data |

## How the Application Works

The application follows a simple request-and-response architecture:

1. The user enters a question in the Python application.
2. Python prepares an HTTP POST request.
3. The request contains authentication headers and a JSON body.
4. Gemini processes the question and generates a response.
5. OpenRouter returns the response as JSON.
6. Python extracts and displays the AI-generated answer.

## Application Architecture

```text
       USER
        |
        | Enters a question
        v
  PYTHON APPLICATION
        |
        | HTTPS POST Request
        | API Key + JSON Data
        v
    GEMINI API
        |
        | Routes the request
        v
  GEMINI 3.8 FLASH
        |
        | Generates an answer
        v
    GEMINI API
        |
        | JSON Response
        v
  PYTHON APPLICATION
        |
        v
   DISPLAY ANSWER
```

## Project Structure

```text
simple-llm/
│
├── .env
├── .gitignore
├── main.py
├── requirements.txt
│
└── answers.json
```

### File descriptions

- `main.py`: Contains the Python application and API communication logic.
- `.env`: Stores the OpenRouter API key securely.
- `.gitignore`: Prevents sensitive files and unnecessary files from being uploaded to GitHub.
- `requirements.txt`: Lists the Python dependencies required by the project.
- `answers.json`: Will be used to store questions and their corresponding AI-generated answers.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/niyomugaboetiene/LLM-full-course-with-projects
cd 1-What-are-LLMs
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

Activate it on Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install requests python-dotenv
```

### 4. Create an OpenRouter API key

Visit:

https://aistudio.google.com/api-keys

Create an API key and keep it private.

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_actual_api_key
```

Never upload your real API key to GitHub.

### 6. Configure the API endpoint

The application communicates with GEMINI AI through this endpoint:

```text
https://generativelanguage.googleapis.com/v1beta
```

The model identifier used in the request is:

```text
google/gemini-3.8-flash
```

### 7. Run the application

```bash
python main.py
```

## Important Concepts I Am Learning

This project focuses on understanding the fundamentals of LLM application development.

**1. API (Application Programming Interface)**

Understanding how different software applications communicate with each other.

**2. HTTP and HTTPS**

Understanding how Python sends requests to an external server and receives responses.

**3. Authentication**

Learning how API keys are used to authenticate requests.

**4. JSON**

Understanding how structured information is sent to and received from an API.

**5. Prompt Engineering**

Learning how to formulate instructions and questions that guide an LLM's responses.

**6. Tokens**

Understanding how language models process text using tokens rather than simply treating everything as individual words.

**7. Error Handling**

Learning how to identify and troubleshoot errors such as HTTP 400, 401, 429 and 500.

## Learning Roadmap

The project will be developed gradually:

- [x] Understand what LLMs are.
- [x] Explore communication with LLM APIs.
- [x] Make an initial API request using Python.
- [ ] Send questions to Gemini 3.8 Flash.
- [ ] Extract and display AI responses.
- [ ] Understand prompts and prompt engineering.
- [ ] Explore tokens and model parameters.
- [ ] Handle API errors.
- [ ] Save questions and answers in JSON.
- [ ] Improve the application.

## Project Status

**Currently in development.**

This is a learning project. Its purpose is to build a strong understanding of LLM application development by implementing each component step by step.

## Author

**NIYOMUGABO Etiene**

Learning Artificial Intelligence, Machine Learning, Deep Learning and Generative AI.