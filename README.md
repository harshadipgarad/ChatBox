## AI Chatbox Project

This is a simple, command-line based AI chatbot application built using Python. 
It connects with the OpenRouter API to fetch smart and contextual responses based on user queries.

---

## Project Architecture

```mermaid
graph TD
    A[👤 User Input] -->|Types message| B[💻 Python Script / VS Code Terminal]
    B -->|Extracts API Key| C[.env File]
    B -->|Sends HTTP POST Request| D[🌐 OpenRouter API Gateway]
    D -->|Forwards Prompt| E[🤖 AI Language Model]
    E -->|Generates Text Response| D
    D -->|Returns JSON Response| B
    B -->|Prints Output| F[💬 Bot Response to User]

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#eee,stroke:#333,stroke-width:1px
    style D fill:#fbf,stroke:#333,stroke-width:2px
    style E fill:#bfb,stroke:#333,stroke-width:2px
    style F fill:#fff,stroke:#333,stroke-width:2px```

✨ Features
Real-time Interaction: Users can chat with the AI model directly via the terminal interface.
OpenRouter Integration: Uses OpenRouter API to easily access advanced language models.
Secure Environment: Environment variables (.env) are used to securely store the API keys.
Input Validation: Handles empty messages and provides a clean exit command (exit).

🚀 How to Run

Install Dependencies
Bash
pip install -r requirements.txt

Configure API Key
Open your .env file and add your key:
Plaintext
OPENROUTER_API_KEY=your_actual_api_key_here

Run the Chatbot
Bash
python chatbox.py