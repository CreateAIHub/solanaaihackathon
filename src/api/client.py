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
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}