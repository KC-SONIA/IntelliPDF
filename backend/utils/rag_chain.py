import os

from pathlib import Path

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI



env_path = Path(__file__).parent.parent / ".env"

load_dotenv(dotenv_path=env_path)



def get_llm():

    llm = ChatGoogleGenerativeAI(

        model="gemini-2.5-flash",

        google_api_key=os.getenv("GOOGLE_API_KEY")

    )

    return llm



def ask_question(vectorstore, question, chat_history):
    history = ""

    for chat in chat_history:

        history += (

            f"User: {chat['user']}\n"

            f"Assistant: {chat['assistant']}\n"

        )

    llm = get_llm()

    results = vectorstore.similarity_search(
        question,
        k=3
    )


    context = "\n\n".join(

        [doc.page_content for doc in results]

    )


    prompt = f"""

    You are a helpful AI assistant.

    Answer only from the provided context.

    If answer is not present,

    say:

    "I couldn't find this information in the uploaded PDF."


    Chat History:

    {history}

    Context:

    {context}

    Question:

    {question}

    Answer:
    """
    response = llm.invoke(prompt)

    return response.content