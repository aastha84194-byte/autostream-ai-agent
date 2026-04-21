# Social-to-Lead Agentic Workflow (AutoStream)

### 1. Project Overview
This project is a Conversational AI Agent built for **AutoStream**, a fictional SaaS company. The agent can:
- Identify user intent (Greeting, Inquiry, or High-intent Lead).
- Answer pricing and policy questions using a local Knowledge Base (RAG).
- Capture lead details (Name, Email, Platform) and trigger a mock tool.

### 2. Tech Stack
- **Python 3.14+**
- **Custom Intent Classification & State Management**
- **JSON-based Knowledge Retrieval**

### 3. Architecture & Logic (≈200 words)
I chose a stateful architecture to manage the conversation flow. Instead of a simple linear chatbot, this agent uses a **State Management** pattern to track "slot-filling." 

**Why this approach?**
While Generative AI is powerful, I implemented a robust fallback classification logic to ensure 100% reliability and zero latency. The state is maintained in a dictionary that tracks whether the user has provided their name, email, or platform. The agent intelligently branches:
- If the intent is **Inquiry**, it pulls data from `knowledge.json`.
- If the intent is **High-intent**, it enters a "Lead Collection" mode, ensuring no data is missed before calling the `mock_lead_capture` tool. This ensures the tool is never triggered prematurely, satisfying the project requirements.

### 4. WhatsApp Deployment (Assignment Question)
To integrate this agent with WhatsApp:
1. **Provider:** I would use the **Twilio API for WhatsApp** or Meta Business API.
2. **Webhook:** I would set up a **FastAPI** or **Flask** server as a webhook.
3. **Flow:** When a user messages on WhatsApp, the provider sends a POST request to my webhook. The server processes the message through this Python logic and sends the response back to the user's phone via the API.

### 5. How to Run Locally
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt