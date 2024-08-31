import os
from dotenv import load_dotenv
from groq import Groq
import json
from air_tools import get_tools, get_tools_desc

load_dotenv()

class Agent:
    def __init__(self, tools = []) -> None:
        self.groq_api_key = os.getenv("GROQ_API_KEY")
        self.llm = Groq()
        # self.MODEL = 'llama3-groq-70b-8192-tool-use-preview'
        self.MODEL="llama-3.1-70b-versatile"
        self.tools_desc = get_tools_desc()
        self.tools = get_tools()
        
        
    def get_system_message(self) -> list:
        return [{
            "role": "system",
            "content": """
                You are a profitional technical assistant that helps the user build a network simulation using NVIDIA AIR.
                NVIDIA Air is a cloud-hosted data center simulation platform designed to create a virtual environment 
                that mimics real-world production settings. It allows users to build and run simulations of 
                complex data center networks, enabling them to validate configurations, features, and automation code effectively. 
                You should answer questions related to this topic only. Be consice in your answers.
                Do not offer to do anything that you do not have a tool for. 
                """
        }]
    
    def get_response(self, messages: list):
        response = self.llm.chat.completions.create(
            model=self.MODEL,
            messages=messages,
            tools=self.tools_desc,
            tool_choice="auto",
            max_tokens=8000
        )
        
        tool_call = self.is_tool_call(response)
        
        if tool_call:
            tool_response = self.run_tool(tool_call, messages)
            print(f"Tool: {tool_response}")
            messages.append(tool_response)

            response = self.llm.chat.completions.create(
                model=self.MODEL,
                messages=messages
            )
        
        return response.choices[0].message.content
        
    def is_tool_call(self, response):
        tool_calls = response.choices[0].message.tool_calls
        if tool_calls:
            return tool_calls[0]
        return None
            
        
    def run_tool(self, tool_call, messages: list):
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)
        print(f"calling tool {function_name}, args: {function_args}")
        
        messages.append({
            "role": "assistant",
            "tool_calls": [
                {
                    "id": tool_call.id,
                    "function": {
                        "name": function_name,
                        "arguments": tool_call.function.arguments
                    },
                    "type": tool_call.type,
                }
            ]
        })

        function_to_call = self.tools[function_name]
        function_response = function_to_call(function_args)
        return {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": function_name,
                "content": function_response,
            }
    

    
    