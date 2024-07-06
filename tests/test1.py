import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

chat = ChatGroq(
    temperature=0,
    model_name="mixtral-8x7b-32768",
    groq_api_key=groq_api_key
)

# Create a simple prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}")
])

# Create a chain
chain = prompt | chat

# Test the chain
response = chain.invoke({"input": "Explain the importance of low latency LLMs in 50 words."})

print(response.content)