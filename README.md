# FastAPIDockerServiceAzure
This is a Python API Server using 
-- FastAPI to create & document the API endpoints
-- Uvicorn to Serve the APIs
-- Langchain to enable the Service Business Logic and callouts to various databases and backend LLMs
-- Docker for easy Deployment in an Azure environment and to house a small onboard ChromaDB vector-store

The Structure of the project is roughly conventional:

FastAPIDockerServiceAzure/
│
├── app/
│   ├── __init__.py
│   └── main.py
├── models/
│   ├── __init__.py
│   ├── query.py
│   ├── answer.py
│   └── helpdbstate.py
├── services/
│   ├── __init__.py
│   └── query_help_DB.py
├── util/
│   ├── __init__.py
│   └── utility.py
├── extensions/
│   ├── __init__.py
│   └── custom_confluence_loader.py
├── config/
│   ├── __init__.py
│   └── config.py
└── tests/
    ├── __init__.py
    └── some_future_test.py
