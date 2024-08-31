from llms import Agent

def vca_application():
        
       
    agent = Agent()
    chat_history = agent.get_system_message()
    
    while True:
        # Prompt the user for input
        user_input = input("> ")
        
        # Check if the user wants to exit the loop
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting the application.")
            break
        
        if user_input.lower() == 'reset':
            chat_history = agent.get_system_message()
            print('\nNew conversation started...\n\n')
            continue

        chat_history.append(
            {
                "role": "user",
                "content": user_input,
            }
        )
        response = agent.get_response(chat_history)

        print('\nAI: ' + response + '\n')

if __name__ == "__main__":
    vca_application()