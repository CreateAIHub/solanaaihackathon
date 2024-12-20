import requests
from .config import ApiConfig

class ApiClient:
    def __init__(self, config: ApiConfig):
        self.config = config
        self.headers = {
            "X-Api-Key": config.api_key,
            "Content-Type": "application/json"
        }
    
    def post(self, endpoint: str, payload: dict) -> dict:
        try:
            url = f"{self.config.base_url}/{endpoint}"
            #print(f"Sending POST request to URL: {url}")
            #print(f"Headers: {self.headers}")
            #print(f"Payload: {payload}")
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            try:
                return response.json()
            except ValueError:
                print("Error decoding JSON: Expecting value")
                raise ValueError("Invalid JSON response")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            raise