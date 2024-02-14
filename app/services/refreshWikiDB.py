from extensions.custom_confluence_loader import CustomConfluenceLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
import config
from utils import utility 
from models import HelpDBState


def getWikiDBInfo() -> HelpDBState:
    return utility.getHelpDBState(config.HELP_WIKI_DB_DIR)

def refreshWikiDB() -> HelpDBState:

    # Create OpenAI embeddings
    openai_embeddings = OpenAIEmbeddings()

    loader = CustomConfluenceLoader(
        url=config.HELP_WIKI_URL,
        username=config.HELP_WIKI_USER_NAME,
        api_key=config.HELP_WIKI_API_KEY
    )
    data = loader.load(space_key="CS", include_attachments=False, limit=50)  #starting with include attachments as false

    # Split the loaded data
    text_splitter = CharacterTextSplitter(separator='\n', 
                                    chunk_size=1000, 
                                    chunk_overlap=40)

    docs = text_splitter.split_documents(data)

    #destroy any previous version of database
    utility.delete_folder_if_exists(config.HELP_WIKI_DB_DIR)

    # Create a Chroma vector database from the documents
    vectordb = Chroma.from_documents(documents=docs, 
                                    embedding=openai_embeddings,
                                    persist_directory=config.HELP_WIKI_DB_DIR)

    vectordb.persist()
    return utility.getHelpDBState(config.HELP_WIKI_DB_DIR)

