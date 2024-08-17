import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from llms import get_llm, get_new_conversation
from air_tools import get_air_connector
load_dotenv()


def vca_application():
    
    air = get_air_connector()
        
    chat_history = get_new_conversation()    
    
    llm = get_llm()
    
    while True:
        # Prompt the user for input
        user_input = input("> ")
        
        # Check if the user wants to exit the loop
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting the application.")
            break
        
        if user_input.lower() == 'reset':
            chat_history = get_new_conversation()
            print('\nNew conversation started...\n\n')
            continue
        
        chat_history.append(HumanMessage(content=user_input))
        
        response = llm.invoke(chat_history)

        print('\nAI: ' + response.content + '\n')
        
        chat_history.append(AIMessage(content=response.content))        

if __name__ == "__main__":
    vca_application()