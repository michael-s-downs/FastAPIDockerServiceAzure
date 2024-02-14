from langchain_community.document_loaders import ConfluenceLoader
from langchain.docstore.document import Document
from langchain_community.vectorstores.utils import filter_complex_metadata
from bs4 import BeautifulSoup as Soup

#In order to apply a custom extractor to our ConfluenceLoader, we need to create/extend our own custom ConfluenceLoader...
class CustomConfluenceLoader(ConfluenceLoader):
    def process_page(self, page_id, space_key, content_format, include_attachments, *args, **kwargs):
        # Call the parent process_page method to retrieve the page content
        page_content = super().process_page(page_id, space_key, content_format, include_attachments, *args, **kwargs)

        oneDocList = [page_content]

        #filter any bad Document Metadata
        filteredPage_ContentList = filter_complex_metadata(oneDocList)        

        #take back the document from the list
        filteredDocument = filteredPage_ContentList[0]

        #get the metadata from the filtered Document
        filteredDocument_metadata = filteredDocument.metadata

        #make sure we only get the html from the Document object returned...
        html_content = filteredDocument.page_content

        # Apply custom extraction logic to the page content
        extracted_content = extract_content(html_content)

        # Finally, we need to turn it back into a Document object for further down-stream processing
        new_document = Document(page_content=extracted_content, metadata=filteredDocument_metadata)
        return new_document

#Define a custom extractor function to extract the text content from the webpage -- CURRENTLY USED
def extract_content(html):
    soup = Soup(html, "html.parser")
    content = soup.get_text()
    return content

#EXPERIMENTAL custom extractor function to extract text AND images from the webpage -- FUTURE USE
def extract_content_and_images(html):
    soup = Soup(html, "html.parser")
    text_content = soup.get_text()
    image_tags = soup.find_all('img')
    return text_content, image_tags