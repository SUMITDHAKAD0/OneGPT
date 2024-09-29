from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import TextSplitter, CharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from src.logging import logger
import os
import sys

class Loader:
    def __init__(self):
        self.path = "https://www.espn.com"

    def pdfloader(self):
        if not self.path:
            raise ValueError("No file path provided.")
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
        try:
            logger.info(f"Loading {os.path.basename(self.path)} File")
            text_loader = TextLoader(self.path)
            text_content = text_loader.load()
            return text_content
        except Exception as e:
            logger.error(f"Error: File not found - {self.path}")
            print(e)
            sys.exit(1)

    def webloader(self):
        if not self.path:
            raise ValueError("No file path provided.")
        try:
            logger.info(f"Loading {os.path.basename(self.path)} File")
            web_loader = WebBaseLoader(self.path)
            web_content = web_loader.load()
            return web_content
        except Exception as e:
            logger.error(f"Error: File not found - {self.path}")
            print(e)
            sys.exit(1)



if __name__ == "__main__":
    data = Loader().pdfloader()
    print(data)

