# Large Language Models (LLMs) — From Beginner to Advanced

![LLM Learning Journey](https://img.shields.io/badge/AI-Large%20Language%20Models-blueviolet)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Learning](https://img.shields.io/badge/Status-Currently%20Learning-orange)
![License](https://img.shields.io/badge/License-MIT-green)

Welcome to my **Large Language Models (LLMs) Learning Repository**!

This repository documents my journey of learning Large Language Models from the fundamentals to advanced concepts through practical coding exercises, experiments, and real-world projects.

Rather than only studying theoretical concepts, I am building small applications and implementing important techniques to understand how LLMs work internally and how they can be used to solve real-world problems.

Every lesson has its corresponding coding tasks, explanations, experiments, and projects.

---

## Project Objectives

The main objectives of this repository are to:

- Understand what Large Language Models are and how they work.
- Learn the mathematics and concepts behind modern language models.
- Understand tokenization, embeddings, attention mechanisms, and Transformers.
- Implement important LLM components using Python and PyTorch.
- Build a small GPT-style language model from scratch.
- Work with pretrained models using Hugging Face.
- Learn how to fine-tune existing language models.
- Understand Retrieval-Augmented Generation (RAG).
- Build AI applications using LangChain and LangGraph.
- Explore AI agents, tool calling, and autonomous workflows.
- Deploy practical LLM-powered applications.

## Learning Roadmap

The repository is organized into learning phases. Each phase covers a specific area of LLM development.

| Phase | Topic | Main Focus |
|---|---|---|
| 01 | LLM Fundamentals | Understanding LLMs and Generative AI |
| 02 | NLP, Tokenization & Embeddings | Processing text and representing words numerically |
| 03 | Transformer Architecture | Understanding attention and Transformer components |
| 04 | Building GPT From Scratch | Implementing and training a Mini-GPT |
| 05 | Hugging Face & Pretrained Models | Working with existing language models |
| 06 | Fine-tuning LLMs | Customizing pretrained models |
| 07 | RAG & Vector Databases | Building document-based AI applications |
| 08 | LangChain & LangGraph | Developing structured LLM workflows |
| 09 | AI Agents | Tool calling, agent memory, and multi-agent systems |
| 10 | Production & Deployment | Optimizing and deploying LLM applications |

---

## Repository Structure

The repository is organized by learning phases and individual lessons.

```text

LLM-Full-Course-With-Projects/
│
├── 01-LLM-Fundamentals/
│   ├── 01-What-Are-Large-Language-Models/
│   ├── 02-Introduction-To-Generative-AI/
│   ├── 03-How-ChatGPT-Works-Internally/
│   ├── 04-Evolution-Of-NLP/
│   ├── 05-Foundation-Models/
│   ├── 06-Pretrained-Vs-Fine-Tuned-Models/
│   ├── 07-LLM-Parameters/
│   ├── 08-Training-Vs-Inference/
│   ├── 09-Context-Window/
│   └── 10-Next-Token-Prediction/
│
├── 02-NLP-Tokenization-And-Embeddings/
│   ├── 11-Introduction-To-NLP/
│   ├── 12-Text-Preprocessing/
│   ├── 13-Bag-Of-Words-And-TF-IDF/
│   ├── 14-Word-Embeddings/
│   ├── 15-Word2Vec/
│   ├── 16-GloVe-Embeddings/
│   ├── 17-LLM-Tokenization/
│   ├── 18-Byte-Pair-Encoding/
│   ├── 19-SentencePiece-Tokenizer/
│   └── 20-Build-Your-Own-Tokenizer/
│
├── 03-Transformer-Architecture/
│   ├── 21-Introduction-To-Transformers/
│   ├── 22-Attention-Is-All-You-Need/
│   ├── 23-Attention-Mechanism/
│   ├── 24-Self-Attention/
│   ├── 25-Query-Key-Value/
│   ├── 26-Scaled-Dot-Product-Attention/
│   ├── 27-Multi-Head-Attention/
│   ├── 28-Positional-Encoding/
│   ├── 29-Feed-Forward-Network/
│   ├── 30-Residual-Connections-And-Layer-Normalization/
│   ├── 31-Transformer-Encoder-Vs-Decoder/
│   ├── 32-Decoder-Only-Transformers/
│   ├── 33-GPT-Architecture/
│   └── 34-BERT-Vs-GPT-Vs-T5/
│
├── 04-Build-GPT-From-Scratch/
│   ├── 35-Build-GPT-From-Scratch/
│   ├── 36-Character-Level-Language-Model/
│   ├── 37-GPT-Training-Data-Preparation/
│   ├── 38-Token-Embedding-Layer/
│   ├── 39-Self-Attention-Using-PyTorch/
│   ├── 40-Multi-Head-Attention-Using-PyTorch/
│   ├── 41-Transformer-Block/
│   ├── 42-GPT-Architecture-Implementation/
│   ├── 43-Training-GPT-Using-PyTorch/
│   ├── 44-Next-Token-Prediction-Using-PyTorch/
│   ├── 45-GPT-Text-Generation/
│   └── 46-Temperature-TopK-TopP-Sampling/
│
├── 05-Hugging-Face-And-Pretrained-LLMs/
│   ├── 47-Hugging-Face-Transformers/
│   ├── 48-Hugging-Face-Tutorial/
│   ├── 49-Loading-Pretrained-LLMs/
│   ├── 50-Hugging-Face-Tokenizers/
│   ├── 51-Text-Generation-With-Hugging-Face/
│   ├── 52-Open-Source-LLMs/
│   ├── 53-Llama-Models/
│   ├── 54-Gemma-Models/
│   └── 55-Build-AI-Chatbot-With-Hugging-Face/
│
├── 06-LLM-Training-And-Fine-Tuning/
│   ├── 56-Pretraining-Vs-Fine-Tuning/
│   ├── 57-Supervised-Fine-Tuning/
│   ├── 58-Instruction-Tuning/
│   ├── 59-Fine-Tuning-Dataset-Preparation/
│   ├── 60-Fine-Tuning-With-Hugging-Face/
│   ├── 61-Parameter-Efficient-Fine-Tuning/
│   ├── 62-LoRA-Fine-Tuning/
│   ├── 63-QLoRA-Fine-Tuning/
│   ├── 64-LLM-Quantization/
│   ├── 65-Fine-Tuning-Llama/
│   └── 66-Evaluating-Fine-Tuned-LLMs/
│
├── 07-RAG-Embeddings-And-Vector-Databases/
│   ├── 67-Introduction-To-RAG/
│   ├── 68-RAG-Architecture/
│   ├── 69-Text-Embeddings-For-LLMs/
│   ├── 70-Vector-Databases/
│   ├── 71-Semantic-Search/
│   ├── 72-FAISS-Tutorial/
│   ├── 73-ChromaDB-Tutorial/
│   ├── 74-Document-Chunking-Strategies/
│   ├── 75-Build-PDF-RAG-Chatbot/
│   ├── 76-RAG-With-LangChain/
│   ├── 77-Advanced-RAG-Techniques/
│   └── 78-RAG-Evaluation-And-Reranking/
│
├── 08-LangChain-And-LangGraph/
│   ├── 79-Introduction-To-LangChain/
│   ├── 80-LangChain-Complete-Tutorial/
│   ├── 81-Chat-Models-And-Prompt-Templates/
│   ├── 82-LangChain-Chains/
│   ├── 83-Document-Loaders-And-Text-Splitters/
│   ├── 84-LangChain-Memory/
│   ├── 85-Build-Chatbot-With-LangChain/
│   ├── 86-Introduction-To-LangGraph/
│   ├── 87-LangGraph-Tutorial/
│   └── 88-Build-AI-Agent-With-LangGraph/
│
├── 09-AI-Agents-And-Advanced-LLM-Engineering/
│   ├── 89-Introduction-To-AI-Agents/
│   ├── 90-LLM-Function-Calling/
│   ├── 91-LLM-Tool-Calling/
│   ├── 92-ReAct-Agents/
│   ├── 93-AI-Agent-Memory/
│   ├── 94-Multi-Agent-Systems/
│   ├── 95-Model-Context-Protocol/
│   ├── 96-Build-AI-Agents-With-Python/
│   ├── 97-Build-Multi-Agent-Systems/
│   └── 98-AI-Agent-Evaluation-And-Guardrails/
│
├── 10-Production-And-Deployment/
│   ├── 99-Deploy-LLMs-With-FastAPI/
│   ├── 100-Running-Local-LLMs-With-Ollama/
│   ├── 101-vLLM/
│   ├── 102-LLM-Quantization-And-Optimization/
│   ├── 103-LLM-Inference-Optimization/
│   ├── 104-KV-Cache/
│   ├── 105-LLM-Streaming-With-FastAPI/
│   ├── 106-Docker-For-LLM-Applications/
│   ├── 107-LLM-Evaluation-And-Monitoring/
│   └── 108-Build-And-Deploy-Complete-LLM-Application/
│
├── requirements.txt
└── README.md

```

*Note: This is the planned organization. The actual folders will grow as I complete each lesson.*

---

## Technologies & Tools

The technologies I expect to use throughout this learning journey include:

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| NumPy | Numerical computations |
| Pandas | Data processing |
| PyTorch | Building and training neural networks |
| Hugging Face | Working with pretrained models |
| Transformers | Loading and using LLMs |
| Tokenizers | Text tokenization |
| SentencePiece | Subword tokenization |
| FAISS | Vector similarity search |
| ChromaDB | Vector database |
| LangChain | Building LLM applications |
| LangGraph | Building stateful AI workflows |
| FastAPI | Developing backend APIs |
| Ollama | Running supported LLMs locally |
| Docker | Application containerization |

Additional tools and technologies will be introduced as the learning journey progresses.

---

## How I Approach Each Lesson

Each lesson follows a practical learning approach:

1. **Theory:** Understand the concept and why it matters.
2. **Implementation:** Write Python code to implement the concept.
3. **Experimentation:** Change inputs, parameters, and configurations to observe different results.
4. **Analysis:** Understand the output and the behavior of the implementation.
5. **Mini Project:** Apply the knowledge to solve a small practical problem.

The goal is not simply to copy code but to understand what every important part does and why it is needed.

---

## Major Projects

Throughout this journey, I plan to develop several projects that combine the concepts learned in different phases.

| Project | Description |
|---|---|
| Custom Tokenizer | A tokenizer that converts text into token IDs |
| Mini-GPT | A small GPT-style language model built using PyTorch |
| AI Chatbot | A chatbot powered by a pretrained LLM |
| Fine-tuned Language Model | A model customized using a task-specific dataset |
| PDF RAG Chatbot | An AI assistant that answers questions from PDF documents |
| Rwanda Education AI Assistant | An educational assistant that uses relevant learning materials |
| AI Research Agent | An agent that researches and organizes information using tools |
| Production LLM Application | A complete application with an API and frontend |

These projects will evolve as I gain more knowledge and experience.

---
## My Long-Term Goal

My long-term goal is to develop the knowledge and practical skills needed to build useful AI-powered applications, particularly applications that can address real-world challenges in Rwanda and beyond.

I am especially interested in exploring:

- AI applications for education.
- Kinyarwanda language technology.
- Intelligent document processing.
- Agricultural AI assistants.
- AI-powered research and information systems.
- Practical LLM applications for everyday problems.

---

## Learning Progress

This repository is continuously updated as I complete new lessons and projects.

| Phase | Learning Area | Status |
|---|---|---|
| 01 | LLM Fundamentals | 🔄 In Progress |
| 02 | NLP, Tokenization & Embeddings | ⏳ Not Started |
| 03 | Transformer Architecture | ⏳ Not Started |
| 04 | Build GPT From Scratch | ⏳ Not Started |
| 05 | Hugging Face & Pretrained Models | ⏳ Not Started |
| 06 | Fine-tuning LLMs | ⏳ Not Started |
| 07 | RAG & Vector Databases | ⏳ Not Started |
| 08 | LangChain & LangGraph | ⏳ Not Started |
| 09 | AI Agents | ⏳ Not Started |
| 10 | Production & Deployment | ⏳ Not Started |

*Progress will be updated as I complete each learning phase.*

---

## Getting Started

### 1. Clone the repository

```bash
clone https://github.com/niyomugaboetiene/LLM-full-course-with-projects
```

### 2. Navigate into the project

```bash
cd LLM-full-course-with-projects
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the environment

Linux / macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

Some lessons may have their own dependencies or setup instructions. Always check the README inside the relevant lesson folder.

---

## Learning Resources

Some of the resources supporting this journey:

- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/en/chapter1/1)
- [Andrej Karpathy — Neural Networks and GPT](https://www.youtube.com/@AndrejKarpathy)
- [Stanford CS336 — Language Modeling from Scratch](https://www.youtube.com/playlist?list=PLoROMvodv4rP8nAmISxFINlGKSK4rbLKh)
- [3Blue1Brown](https://www.youtube.com/@3blue1brown)
- [DeepLearning.AI](https://www.deeplearning.ai/courses/)
- [Hugging Face Documentation](https://huggingface.co/docs)

---

## Contributions & Feedback

This repository primarily documents my personal learning journey, but suggestions, corrections, discussions, and improvements are welcome.

If you find an error or have a better way of implementing something, feel free to open an issue or submit a pull request.

---

## Author

**NIYOMUGABO Etiene**

UR Student | Python Developer | AI & Machine Learning Enthusiast

Exploring Artificial Intelligence, Machine Learning, Deep Learning, and Large Language Models.

- Website: [Personal Web](https://niyomugaboetiene.vercel.app)

---

## Support

If you find this repository useful for your own LLM learning journey, consider giving it a ⭐ star.

**Learning by building. Understanding by experimenting. Growing through AI.**