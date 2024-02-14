from models.query import Query
from models.answer import Answer
from models.source_document import SourceDocument   

#CURRENTLY KEEPING AT A 'MOCK' UNTIL READY TO PLUG IN BUSINESS LOGIC (TESTING build, refreshWikiDB service first)
def getAnswer(query: Query) -> Answer:
    
    # For demonstration, we'll create a dummy response and a list of source documents
    response = "This is a response based on the query: " + query.user_question
    system_role = "Default System Role"  # The idea is that someday we will need to allow or override multiple system roles...

    # Dummy list of SourceDocument instances
    # Replace this with actual data retrieval and creation logic
    source_documents = [
        SourceDocument(document_name="Doc 1", url="http://example.com/doc1"),
        SourceDocument(document_name="Doc 2", url="http://example.com/doc2"),
    ]

    # Construct and return an Answer object
    answer = Answer(
        user_question=query.user_question,
        system_role=system_role,
        response=response,
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