.PHONY: help install dev-backend dev-frontend db-up db-down db-reset

help:
	@echo "Available commands:"
	@echo "  make install      - Install all dependencies"
	@echo "  make dev-backend  - Start FastAPI development server"
	@echo "  make dev-frontend - Start Next.js development server"
	@echo "  make db-up        - Start PostgreSQL container"
	@echo "  make db-down      - Stop PostgreSQL container"
	@echo "  make db-reset     - Delete database and start fresh"

# Install dependencies
install:
	cd backend && pip install -r requirements.txt
	cd frontend && npm install

# Development servers
dev-backend:
	cd backend && uvicorn app.main:app --reload --port 8000

dev-frontend:
	cd frontend && npm run dev

# Database management
db-up:
	docker compose up -d postgres

db-down:
	docker compose down

db-reset:
	docker compose down -v
	docker compose up -d postgres
