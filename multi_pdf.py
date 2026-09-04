from langchain_openrouter import ChatOpenRouter
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os 
pdf=[
    "RAG/sample3.pdf",
    "RAG/sample4.pdf"
]
documents=[]
for i in pdf:
    loader=PyPDFLoader(i)
    document=loader.load()

    for doc in document:
        doc.metadata["source"] = i

        documents.extend(document)


splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunk = splitter.split_documents(documents)

embedding=HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

vector_store=FAISS.from_documents(
    chunk,
   embedding
)

retrievar = vector_store.as_retriever(
    search_kwargs={"k":5}
)

prompt = ChatPromptTemplate.from_template(
    """answer like a helpful assistant 
answer from only povided context.

context:{context}
question:{input}

"""
)

llm = ChatOpenRouter(
    model="gpt-oss-20b",
    openrouter_api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0
)

document_chain=create_stuff_documents_chain(
    
    llm,
    prompt
)

retrievar_chain=create_retrieval_chain(
    retrievar,
    document_chain
)


while True:
    user_input=input("you: ")

    if user_input.lower()=="exit":
        break

    response=retrievar_chain.invoke(
        {"input":user_input}

    )

    print("answer")
    print(response["answer"])
    print()
