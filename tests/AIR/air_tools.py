from air_sdk import AirApi
import os

def get_air_connector():
    user = "obenyacov@nvidia.com"
    api_token = os.getenv("AIR_API_KEY")
    
    air = AirApi(username=user, password=api_token, api_url="https://air-inside.nvidia.com/api/")
    
    return air


def get_air_tools():
    pass
    
    