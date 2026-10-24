from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import shutil
import os

from utils.pdf_loader import load_pdf
from utils.splitter import split_documents
from utils.embeddings import get_embedding_model

from utils.vectorstore import (
    create_vectorstore,
    save_vectorstore,
    load_vectorstore
)

from utils.rag_chain import ask_question

app = FastAPI()


# CORS

app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)

# Create uploads folder if not exists

os.makedirs(

    "uploads",

    exist_ok=True

)


# Global Variables

vectorstore = None
chat_history = []
embeddings = get_embedding_model()


# Load Saved VectorStore

try:

    vectorstore = load_vectorstore(

        embeddings

    )

    print("Vectorstore loaded successfully")


except Exception as e:

    print("No saved vectorstore found")

    print(e)



# Home Route

@app.get("/")

def home():

    return {

        "message":

        "PDF RAG Chatbot Backend Running"

    }

# Upload Route

@app.post("/upload")

def upload_pdf(

    file: UploadFile = File(...)

):

    global vectorstore


    file_path = f"uploads/{file.filename}"


    with open(

        file_path,

        "wb"

    ) as buffer:


        shutil.copyfileobj(

            file.file,

            buffer

        )


    documents = load_pdf(file_path)
    chunks = split_documents(documents)
    vectorstore = create_vectorstore(chunks,embeddings)

    save_vectorstore(vectorstore)

    return {

        "success": True,

        "message":"PDF uploaded and vectorstore created"}



# Chat Request Model

class ChatRequest(BaseModel):

    question: str



# Chat Route

@app.post("/chat")
def chat(data: ChatRequest):
    global vectorstore

    global chat_history

    if vectorstore is None:

        raise HTTPException(status_code=400,detail="Please upload PDF first")

    answer = ask_question(vectorstore,data.question,chat_history)


    chat_history.append(

        {

            "user": data.question,
            "assistant": answer

        }

    )


    return {

        "success":True,

        "answer":answer

    }

@app.post("/clear-chat")
def clear_chat():
    global chat_history
    chat_history = []
    return {
        "message":"Chat history cleared"
    }