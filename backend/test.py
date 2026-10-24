from utils.pdf_loader import load_pdf

from utils.splitter import split_documents

from utils.embeddings import get_embedding_model

from utils.vectorstore import create_vectorstore

from utils.rag_chain import ask_question



documents = load_pdf("uploads/Unit-1.pdf")

chunks = split_documents(documents)

embeddings = get_embedding_model()


vectorstore = create_vectorstore(

    chunks,

    embeddings

)


answer = ask_question(

    vectorstore,

    "What is Machine Learning?"

)


print(answer)