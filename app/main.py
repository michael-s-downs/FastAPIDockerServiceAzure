from fastapi import FastAPI
from models import Query, Answer, HelpDBState
from services import query_help_DB, refreshWikiDB

app = FastAPI()

####################################
#EXAMPLE AND HELPFUL ENDPOINTS HERE:
####################################

#In case someone hits the top-level root address instead of a declared API-defining PATH...
@app.get("/")
async def top_level():
    return {"message": "Welcome to the Outlet Query Tool Gen-AI-over-API Service.  You are at the top, where there is nothing to see.  Available APIs are documented at /docs"}

#A REST Get Item by Path Pattern Example...
@app.get("/hello/{name}")
async def hello_name(name):
    return {"message": f"Hello {name}, how are you?"}

###################################
#CORE FEATURE ENDPOINTS BEGIN HERE:
###################################

#POST a Gen-AI Query Model and get back an Answer Model
@app.post("/query", response_model=Answer)
async def create_query(query: Query):
    return query_help_DB.getAnswer(query)

#GET a HelpDBState model describing the current state of the Help DB
@app.get("/gethelpdbinfo", response_model=HelpDBState)
async def get_help_db_info():
    return 

#GET Endpoint-Trigger to refresh the Help DB; Returns a HelpDBState Model to verify isExistent with the current lastRefresh time 
@app.get("/refreshhelpdb", response_model=HelpDBState)
async def refresh_help_db():
    #do something...
    return {"MOCK Return State": f"this will be replaced with success/fail + current info about the Help DB"}

