# CodeLens

AI-powered tool that helps developers understand unfamiliar codebases using RAG (Retrieval-Augmented Generation).

## Features (MVP)

- Upload a ZIP file containing source code
- Automatically index the repository
- Ask questions about the codebase
- Get answers with citations to specific files

## Tech Stack

- **Frontend:** Next.js, React, Tailwind CSS
- **Backend:** FastAPI, SQLAlchemy
- **Database:** PostgreSQL with pgvector
- **LLM:** OpenAI API

## Prerequisites

- Node.js 18+
- Python 3.9+
- Docker

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd CodeLens
```

### 2. Start the database

```bash
make db-up
```

### 3. Set up the backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your OpenAI API key
```

### 4. Set up the frontend

```bash
cd frontend
npm install
```

### 5. Run the development servers

In separate terminals:

```bash
# Terminal 1: Backend
make dev-backend

# Terminal 2: Frontend
make dev-frontend
```

## Project Structure

```
CodeLens/
├── frontend/          # Next.js application
├── backend/           # FastAPI application
├── docker/            # Docker configurations
└── docs/              # Documentation
```

## License

MIT
