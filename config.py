import os
import json

# load environmentally static configs from config.json: update or create values  in a config.json file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)
HELP_WIKI_USER_NAME = config["help_wiki_user_name"]
HELP_WIKI_API_KEY = config["help_wiki_api_key"]
HELP_WIKI_URL = config["help_wiki_url"]

#Some Global Variables for finding the database (or queries for refreshing it) that must be dynamically determined at run-time
CODE_ABS_PATH: str = os.path.dirname(os.path.abspath(__file__))
HELP_WIKI_DB_DIR: str = os.path.join(CODE_ABS_PATH, "AspirentWikiDB")