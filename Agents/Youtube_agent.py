from Prompt.prompt_router import PROMPTS
from llms.groq import llm

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api import TranscriptsDisabled

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableParallel,
    RunnableLambda,
    RunnablePassthrough
)

parser = StrOutputParser()


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def youtube_agent(video_id, question):

    api = YouTubeTranscriptApi()

    transcript_list = api.fetch(video_id, languages=["en"])

    transcript = " ".join(chunk.text for chunk in transcript_list)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    docs = splitter.create_documents([transcript])

    embedding = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-2"
    )

    vector_store = Chroma.from_documents(
        docs,
        embedding
    )

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k":4}
    )

    parallel = RunnableParallel({

        "context":retriever| RunnableLambda(format_docs),

        "question":RunnablePassthrough()

    })

    chain = (
        parallel| PROMPTS["youtube"]| llm| parser
    )

    return chain.invoke(question)