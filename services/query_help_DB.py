import chromadb
from models.query_model import Query
from models.answer_model import Answer
from models.source_document import SourceDocument  
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from config import config
from models.source_document import SourceDocument  

#CURRENTLY KEEPING AT A 'MOCK' UNTIL READY TO PLUG IN BUSINESS LOGIC (TESTING build, refreshWikiDB service first)
def getAnswer(query: Query) -> Answer:
    
    openai_embeddings = OpenAIEmbeddings()

    vectordb = Chroma(embedding_function=openai_embeddings, persist_directory=config.HELP_WIKI_DB_DIR)

    # Create a retriever from the Chroma vector database
    retriever = vectordb.as_retriever(search_kwargs={"k": 30})

    # Use a ChatOpenAI model
    llm = ChatOpenAI(model_name='gpt-4-turbo-preview')

    # Create a RetrievalQA from the model and retriever
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)

    # Run the prompt and return the response
    response = qa(query.user_question)

    source_documents = [SourceDocument(title=doc.metadata["title"], source=doc.metadata["source"]) for doc in response["source_documents"]]

    # Construct and return an Answer object
    answer = Answer(
        user_question=query.user_question,
        system_role=query.system_role,
        response=response["result"],
        source_documents=source_documents
    )
    
    return answer

#TO-DO SECTION:  INCORPORATE THIS BUSINESS LOGIC FROM ORIGINAL POC Script
        # vectordb = Chroma(embedding_function=openai_embeddings, persist_directory=DB_DIR)

        # # Create a retriever from the Chroma vector database
        # retriever = vectordb.as_retriever(search_kwargs={"k": 30})

        # # Use a ChatOpenAI model
        # llm = ChatOpenAI(model_name='gpt-4-turbo-preview')

        # # Create a RetrievalQA from the model and retriever
        # qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)

        # # Run the prompt and return the response
        # response = qa(user_question)
        # st.subheader("Answer:")
        # st.write(response["result"])
        # st.subheader("Top Sources Used:")
        # for source_doc in response["source_documents"]:
        #     title = source_doc.metadata["title"]
        #     sourceLink = source_doc.metadata["source"]
        #     stringified = "["+title+"]"+"("+sourceLink+")"
        #     st.write(stringified)