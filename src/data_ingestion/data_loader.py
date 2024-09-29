from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import TextSplitter, CharacterTextSplitter
from src.logging import logger
import os
import sys

class Loader:
    def __init__(self):
        self.path = "data/gst1.pdf"

    def _validate_file_format(self, expected_format):
        if not os.path.isfile(self.path):
            raise ValueError(f"File not found: {self.path}")

        mime_type = magic.from_file(self.path, mime=True)
        if not expected_format.lower() in mime_type:
            raise ValueError(f"Invalid file format for {self.path}. Expected: {expected_format}")


    def pdfloader(self):
        if not self.path:
            raise ValueError("No file path provided.")
        self._validate_file_format('PDF')
  
        try:
            logger.info(f"Loading {os.path.basename(self.path)} File")
            pdf_loader = PyPDFLoader(self.path)
            pdf_content = pdf_loader.load()
            return pdf_content
        except Exception as e:
            logger.error(f"Error: File not found - {self.path}")
            print(e)
            sys.exit(1)
            

    def docloader(self):
        if not self.path:
            raise ValueError("No file path provided.")
        self._validate_file_format('docx')
        
        try:
            logger.info(f"Loading {os.path.basename(self.path)} File")
            doc_loader = Docx2txtLoader(self.path)
            doc_content = doc_loader.load()
            return doc_content
        except Exception as e:
            logger.error(f"Error: File not found - {self.path}")
            print(e)
            sys.exit(1)
        

    def textloader(self):
        if not self.path:
            raise ValueError("No file path provided.")
        self._validate_file_format('txt')

        try:
            logger.info(f"Loading {os.path.basename(self.path)} File")
            text_loader = TextLoader(self.path)
            text_content = text_loader.load()
            return text_content
        except Exception as e:
            logger.error(f"Error: File not found - {self.path}")
            print(e)
            sys.exit(1)
        

if __name__ == "__main__":
    data = Loader().pdfloader()
    print(data)

