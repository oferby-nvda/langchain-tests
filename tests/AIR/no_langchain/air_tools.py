from air_sdk import AirApi
import os
from dotenv import load_dotenv
load_dotenv()

user = "obenyacov@nvidia.com"
api_token = os.getenv("AIR_API_KEY")
air = AirApi(username=user, password=api_token, api_url="https://air-inside.nvidia.com/api/")

def get_tools() -> dict:
    tools = {
        "get_simulation_list": get_simulation_list,
            
    }
    return tools
    
def get_tools_desc() -> list:
    tools_desc = list()
    tools_desc.append(get_simulation_list_desc())
    return tools_desc
    

def get_simulation_list(dummy) -> str:
    simulations = air.simulation.list()
    response = []
    for simulation in simulations:
        response.append(simulation.title)
    return str(response)

def get_simulation_list_desc():
    return {
        "type": "function",
        "function": {
            "name": "get_simulation_list",
            "description": "return a list of all the simulation names",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        },
    }
    
    
    
# {
#         "type": "function",
#         "function": {
#             "name": "get_simulation_list",
#             "description": "return a list of all the simulation names",
#             "parameters": {
#                 "type": "object",
#                 "properties": {
#                     "expression": {
#                         "type": "string",
#                         "description": "The mathematical expression to evaluate",
#                     }
#                 },
#                 "required": ["expression"],
#             },
#         },
# }    
        