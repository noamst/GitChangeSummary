import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

# Load Groq API key
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY environment variable is missing")

# Use LLaMA 3 for summarization
llm = ChatGroq(
    model="llama3-8b-8192",
    api_key=groq_api_key
)

# Prompt and chain
prompt = PromptTemplate(
    input_variables=["diff"],
    template="Summarize the following git diff in natural language:\n\n{diff}"
)

summarization_chain = RunnableSequence(prompt | llm | StrOutputParser())

def summarize_diff(diff_text: str) -> str:
    return summarization_chain.invoke({"diff": diff_text})
