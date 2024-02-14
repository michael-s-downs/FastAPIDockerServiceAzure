# FastAPIDockerServiceAzure
This is a Python API Server using 
-- FastAPI to create & document the API endpoints
-- Uvicorn to Serve the APIs
-- Langchain to enable the Service Business Logic and callouts to various databases and backend LLMs
-- Docker for easy Deployment in an Azure environment and to house a small onboard ChromaDB vector-store

The Structure of the project is roughly conventional:

FastAPIDockerServiceAzure/
│
├── app/                        # Application specific modules
│   ├── __init__.py             # Makes app a Python package
│   ├── main.py                 # Entry point for the application
│   ├── models/                 # Data models used by API endpoints & services
│   │   ├── __init__.py         # Makes models a Python package
│   │   └── example_model.py    # Example model
│   │
│   ├── services/               # Business logic for APIs
│   │   ├── __init__.py         # Makes services a Python package
│   │   └── example_service.py  # API service handler
│   │
│   └── utils/                  # Utility functions
│   │   ├── __init__.py         # Makes utils a Python package
│   │   └── utility.py          # Utility class
│   │
│   └── config/                 # config files & class
│       ├── __init__.py         # Makes utils a Python package
│       ├── config.json         # Static config items
│       └── config.py           # config class for constructing constants by environment
│
├── extensions/                 # Custom classes to extend libraries
│   ├── __init__.py             # Makes extensions a Python package
│   └── custom_extension.py     # Custom class example
│
├── tests/                      # Unit tests
│   ├── __init__.py             # Makes tests a Python package
│   └── test_example.py         # Example test
│
├── requirements.txt            # Project dependencies
└── setup.py                    # Setup script for the package distribution  (MAYBE)
