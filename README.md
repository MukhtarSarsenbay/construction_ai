# AI-Powered Construction Task Manager 🏗️🤖

A FastAPI-based microservice that generates construction project tasks using Google's Gemini Pro AI model and manages project execution.

## Features

- **AI Task Generation**: Automatically generates construction tasks using Gemini Pro
- **Project Management**: Store and track projects with SQLite database
- **REST API**: Create and monitor projects through API endpoints
- **Background Processing**: Simulates task completion automatically (bonus feature)
- **Unit Tests**: Basic test coverage for API endpoints (bonus feature)

## Technologies Used

- **Backend**: FastAPI
- **AI Model**: Google Gemini Pro
- **Database**: SQLite with SQLAlchemy ORM
- **Async Processing**: Python asyncio
- **Testing**: Pytest

## Getting Started

### Prerequisites

- Python 3.8+
- Google Gemini API key (free tier)
- [Get API Key](https://ai.google.dev/)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/MukhtarSarsenbay/construction_ai.git
cd construction-ai
```

2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create .env file:
```bash
echo "GEMINI_API_KEY=your_api_key_here" > .env
```
5. Running the Application
```bash
uvicorn app.main:app --reload
```
The API will be available at http://127.0.0.1:8000/

API Documentation
Endpoints
POST /api/v1/projects/

Create a new construction project

Request:
```bash
{
  "project_name": "Shopping Mall",
  "location": "Dubai"
}
```
Response:
```bash
{
  "id": 1,
  "project_name": "Shopping Mall",
  "location": "Dubai",
  "status": "processing",
  "created_at": "2024-02-20T12:34:56",
  "tasks": [
    {"name": "Site Survey", "status": "pending"},
    {"name": "Permit Application", "status": "pending"}
  ]
}
```

GET /api/v1/projects/{project_id}

Get project details

Response:
```bash
{
  "id": 1,
  "project_name": "Shopping Mall",
  "location": "Dubai",
  "status": "in_progress",
  "created_at": "2024-02-20T12:34:56",
  "tasks": [
    {"name": "Site Survey", "status": "completed"},
    {"name": "Permit Application", "status": "pending"}
  ]
}
```

Usage

    Create a new project:

```bash
curl -X POST "http://localhost:8000/api/v1/projects/" \
-H "Content-Type: application/json" \
-d "{\"project_name\": \"Hospital\", \"location\": \"London\"}"

    Check project status:
```
```bash

curl "http://localhost:8000/api/v1/projects/1"
```
    Access interactive docs:

```bash
http://localhost:8000/docs
```
Testing

Run unit tests:
```bash
pytest tests/ -v
```

Configuration

construction_ai/
├── app/
│   ├── __init__.py
│   ├── main.py         # FastAPI setup
│   ├── database.py     # Database configuration
│   ├── models.py       # SQLAlchemy models
│   ├── schemas.py      # Pydantic schemas
│   ├── services.py     # Gemini integration & background tasks
│   └── routes.py       # API endpoints
├── tests/
│   └── test_api.py     # Unit tests
├── requirements.txt    # Dependencies
└── README.md           # This documentation

License

MIT License

Notes

    The background process automatically completes tasks every 10 seconds

    First API call might take longer due to model initialization

    Ensure your API key has access to Gemini Pro models