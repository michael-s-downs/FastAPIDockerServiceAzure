# FastAPIDockerServiceAzure
This is a Python API Server using 
-- FastAPI to create & document the API endpoints
-- Uvicorn to Serve the APIs
-- Langchain to enable the Service Business Logic and callouts to various databases and backend LLMs
-- Docker for easy Deployment in an Azure environment and to house a small onboard ChromaDB vector-store

The Structure of the project is roughly conventional:

```FastAPIDockerServiceAzure/
├───.vscode
├───app
│   └───__pycache__
├───config
│   └───__pycache__
├───extensions
│   └───__pycache__
├───models
│   └───__pycache__
├───services
│   └───__pycache__
├───tests
└───utils
    └───__pycache__```
