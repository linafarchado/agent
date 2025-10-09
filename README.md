# AI Portfolio Agent

An intelligent agent that presents my professional profile as a Machine Learning Engineer through natural conversation. Built with Streamlit and powered by DeepSeek-V3.

## Live Demo

https://linafarchado.streamlit.app/

## Overview

This agent autonomously handles questions about my professional background, projects, and technical skills. It perceives user intent, retrieves relevant information from a knowledge base, and generates responses in English or French using a large language model.

## Features

- Context-aware responses based on query intent
- Bilingual support (English/French)
- Fallback to structured data on API failures
- Session-based conversation memory

## Architecture

The agent operates through three main layers:

**Perception**: Keyword-based detection identifies query context (projects, experience, skills, education, contact)

**Reasoning**: Maps detected context to relevant data sections in the knowledge base (data.json)

**Action**: Generates natural language responses via DeepSeek-V3 LLM or displays formatted structured data as fallback

## Tech Stack

- **Framework**: Streamlit
- **LLM**: DeepSeek-V3 (HuggingFace Inference API)
- **Language**: Python
- **Data**: JSON-based knowledge base

## Project Structure

```
.
├── app.py              # Main agent application
├── data.json           # Knowledge base (profile data)
├── requirements.txt    # Python dependencies
└── README.md
```

## Local Setup

```bash
pip install -r requirements.txt
```

Create `.streamlit/secrets.toml`:
```toml
HF_TOKEN = "your_huggingface_token"
```

Get your token at https://huggingface.co/settings/tokens

Run the agent:
```bash
streamlit run app.py
```

## How It Works

1. User submits a question
2. Agent detects context via keyword analysis
3. Retrieves relevant data from JSON knowledge base
4. Formats data and constructs LLM prompt
5. DeepSeek-V3 generates natural language response
6. Returns answer (or fallback data if API unavailable)

## License

Personal portfolio project - Lina Farchado