import os
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage

def get_new_conversation():
    chat_history = []
    chat_history.append(SystemMessage(
        content = """
        You are a helpful assistant that helps the user build a network simulation using NVIDIA AIR.
        NVIDIA Air is a cloud-hosted data center simulation platform designed to create a virtual environment 
        that mimics real-world production settings. It allows users to build and run simulations of 
        complex data center networks, enabling them to validate configurations, features, and automation code effectively. 
        You should answer questions related to this topic only. 
        If you don't have enough information to complete the task, ask the user for more details. Be specific about what information you need. 
        
        """
        ))
    return chat_history


def get_llm():

    groq_api_key = os.getenv("GROQ_API_KEY")

    MODEL_NAME = "llama-3.1-70b-versatile"

    llm = ChatGroq(
        temperature=0,
        model_name=MODEL_NAME,
        groq_api_key=groq_api_key
    )
    
    return llm