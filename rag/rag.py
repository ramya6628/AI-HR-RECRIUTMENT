from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS


def create_vectorstore():

    loader = TextLoader(
        "data/hr_knowledge.txt",
        encoding="utf-8"
    )

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vectorstore


def search_hr_knowledge(question):

    vectorstore = create_vectorstore()

    results = vectorstore.similarity_search(
        question,
        k=3
    )

    return "\n\n".join(
        [doc.page_content for doc in results]
    )