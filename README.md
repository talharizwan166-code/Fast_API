# Fast-API

A beginner-friendly FastAPI project showcasing basic API routes, JSON responses, and RESTful web development fundamentals in Python.

## Features

* Blog API endpoints (GET, POST)
* Query parameters for filtering
* Pydantic models for data validation
* Comments system

## Installation

1. Clone the repository:

```bash
git clone https://github.com/talharizwan166-code/Fast\_API.git
cd Fast-API
```

2. Create and activate virtual environment:

```bash
python -m venv venv
# Windows
venv\\Scripts\\activate
# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 9000
```

Visit: http://127.0.0.1:9000/docs for interactive API documentation

## Project Structure

```
Fast-API/
├── main.py              # Your main FastAPI application
├── blog/                # Blog module
│   ├── \_\_init\_\_.py
│   └── main.py
├── app/                 # Empty folder for future scaling
│   ├── routers/         # Future: API route handlers
│   ├── schemas/         # Future: Pydantic models
│   ├── models/          # Future: Database models
│   └── core/            # Future: Configuration
├── tests/               # Empty folder for future tests
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

## API Endpoints

* `GET /blog` - Get list of blogs
* `GET /blog/unpublished` - Get unpublished blogs
* `GET /blog/{id}` - Get blog by ID
* `GET /blog/{id}/comments` - Get blog comments
* `POST /blog` - Create new blog

## License

MIT License

