# Unified Agent Platform

A **backend-first FastAPI project** that exposes a **single unified API** to create AI agents across **multiple platforms** using a clean **adapter pattern**.

This project is designed to demonstrate **real-world backend engineering**: API design, abstraction, third-party integrations, deployment, and trade-off decisions.

---

## 🚀 Live Deployment

The service is **deployed on Render**.

* **Base URL:** `https://unified-agent-platform-1.onrender.com`

Swagger is the primary interface for testing the API.

---

## ✨ What This Project Does

Using a single endpoint (`POST /agents`), this backend can:

* Create a **voice-based agent** using **Vapi**
* Create a **text-based LLM assistant** using **OpenAI Assistants API**

Both platforms share the **same request schema**, while platform-specific logic is handled internally.

---

## 🧠 Why This Project Exists

Most beginner projects:

* Hard-code one API
* Mix business logic with routes
* Break when APIs differ

This project focuses on:

* Clean abstraction of third-party APIs
* Consistent request/response contracts
* Backend architecture over UI polish

---

## 🏗️ Architecture Overview

```
Client (Swagger / API Consumer)
        │
        ▼
POST /agents
        │
   AgentService
        │
 ┌──────┴────────┐
 ▼               ▼
VapiAdapter   OpenAIAdapter
 ▼               ▼
Vapi API     OpenAI Assistants API
```

### Key Design Decisions

* **Adapter Pattern** to isolate external APIs
* **Unified request schema** across platforms
* **Normalized responses** for consistency
* **Fail-fast validation** using Pydantic

---

## 🧩 Supported Platforms

| Platform          | Type        | Status       |
| ----------------- | ----------- | ------------ |
| Vapi              | Voice agent | ✅ Integrated |
| OpenAI Assistants | LLM agent   | ✅ Integrated |

---

## 📌 API Contract

### Request: `POST /agents`

```json
{
  "platform": "vapi | openai",
  "agent_name": "SupportBot",
  "model": "gpt-4o-mini",
  "instructions": "You are a helpful assistant"
}
```

---

### Response (Normalized)

```json
{
  "platform": "openai",
  "agent_id": "asst_...",
  "name": "SupportBot",
  "type": "llm",
  "model": "gpt-4o-mini",
  "created_at": "2026-01-04T14:15:36Z"
}
```

For Vapi, `type` will be `voice`.

---

## 🧪 Run Locally

### 1. Clone repository

```bash
git clone <repo-url>
cd unified-agent-platform
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` file

```env
VAPI_API_KEY=your_vapi_key
OPENAI_API_KEY=your_openai_key
```

### 5. Run the server

```bash
python -m uvicorn app.main:app --reload
```

Open Swagger at:

```
http://127.0.0.1:8000/docs
```

---

## ☁️ Deployment (Render)

* Runtime: Python
* Start command:

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 10000
```

* Secrets managed via **Render Environment Variables**

---

## ⚠️ Design Trade-offs

* No database (focus is API abstraction, not persistence)
* No heavy frontend (Swagger is sufficient for backend demos)
* Retell was intentionally excluded due to multi-step enterprise-only workflow

---

## 📈 How This Can Scale

* Add more agent platforms via new adapters
* Add authentication & rate limiting
* Add persistence layer
* Convert into internal platform service

---

## 🧑‍💻 What This Project Demonstrates

* Backend system design
* Adapter pattern usage
* Third-party API integration
* Error handling & debugging
* Real cloud deployment

---

## 📄 License

MIT
