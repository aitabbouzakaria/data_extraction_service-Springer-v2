# githubprjt

A robust, scalable API service designed to extract data from third-party sources with comprehensive testing and monitoring.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
- [Running the Service](#running-the-service)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [License](#license)

---

## Overview

The Data Extraction Service provides asynchronous job processing for extracting data, with endpoints to manage jobs, monitor status, and retrieve results. It is built with FastAPI and comes with automated tests covering seeded, real, and edge case scenarios.

---

## Features

- Start, monitor, cancel, and remove extraction jobs
- List all jobs and fetch statistics
- Health check endpoint for monitoring
- Pagination support for large datasets
- API token-based authentication
- Robust error handling and validation
- Tested with Pytest for multiple scenarios

---

## Tech Stack

- **Backend:** Python 3.11+ with FastAPI
- **Database:** PostgreSQL
- **Task Queue:** Celery with Redis
- **Testing:** Pytest
- **Documentation:** Swagger UI / OpenAPI

---

## Setup

1. Clone the repository:

```bash
git clone <your-repo-url>
cd data-extraction-service
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

3. Copy the `.env.example` to `.env` and configure your environment variables.

---

## Running the Service

Start the API server with Uvicorn:

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI is available at:

```
http://127.0.0.1:8000/docs
```

Example endpoints:

- `POST /api/v1/scan/start` — Start a new extraction job  
- `GET /api/v1/scan/status/<job_id>` — Get job status  
- `GET /api/v1/scan/result/<job_id>` — Get job results  
- `POST /api/v1/scan/cancel/<job_id>` — Cancel a job  
- `DELETE /api/v1/scan/remove/<job_id>` — Remove a job  
- `GET /api/v1/jobs/jobs` — List all jobs  
- `GET /api/v1/jobs/statistics` — Get job statistics  
- `GET /api/v1/health` — Health check

---

## Testing

Run all tests:

```bash
pytest -v
```

Testing categories:

- **Seeded Data Tests:** deterministic, fast tests using pre-populated database  
- **Real Extraction Tests:** end-to-end extraction with actual third-party API  
- **Edge Case Tests:** invalid inputs, error handling, and boundary checks

---

## Project Structure

```
githubprjt/
├── app/
│   ├── routes/
│   │   ├── scan.py
│   │   ├── jobs.py
│   │   └── health.py
│   ├── main.py
│   └── ...
├── tests/
│   ├── seeded/
│   ├── real/
│   └── edge/
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## Environment Variables

- `DATABASE_URL` — PostgreSQL connection URL  
- `REDIS_URL` — Redis URL for Celery  
- `API_SECRET_KEY` — Secret key for authentication  
- `EXTERNAL_API_BASE_URL` — Base URL for external data source  
- `LOG_LEVEL` — Logging level (default: INFO)

---

## License

MIT License

