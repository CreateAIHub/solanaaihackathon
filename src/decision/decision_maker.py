from typing import Dict, Callable
import json
from ..api.client import ApiClient
from ..handlers.action_handler import ActionHandler, ActionType
import requests
class DecisionMaker:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client
        self.action_handlers: Dict[str, Callable] = {
            ActionType.KNOWLEDGE_BASE.value: ActionHandler.handle_knowledge_base,
            ActionType.SWAP.value: ActionHandler.handle_swap,
            ActionType.ASKING_MORE_DETAILS.value: ActionHandler.handle_asking_more_details,
            ActionType.SOLANA_API_BOT.value: self.handle_solana_api_bot  # Add this line
        }

    def query(self, question: str) -> dict:
        payload = {"query": question}
        return self.api_client.post("decision_maker/chat/", payload)

    def parse_response(self, response: dict) -> None:
        try:
            # Extract JSON string from markdown code blocks if present
            message_text = response.get("message", "{}")
            if message_text.startswith("```json\n"):
                message_text = message_text.split("```json\n")[1].split("```")[0].strip()
            
            message = json.loads(message_text)
            agent_action = message.get("agent_action", "")
            action_details = message.get("action_details", "")
            parameters = message.get("parameters", {})
            
            handler = self.action_handlers.get(agent_action)
            if handler:
                result=handler(action_details, parameters)
                return result
            else:
                print(f"Unknown action type: {agent_action}")
                print(f"Details: {action_details}")
                
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            print(f"Response: {response}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print(f"Response: {response}")

    def handle_solana_api_bot(self, details: str, parameters: dict) -> None:
        try:
            payload = {"query": parameters.get("message", "")}
            #print(f"Payload for Solana API Bot: {payload}")
            response = self.api_client.post("solana_api_bot/chat/", payload)
            #print("Response from Solana API Bot:", response)
            #if isinstance(response, str):
                #print("Solana API Bot Response (String):", response)
            #else:
            #    print("Solana API Bot Response (JSON):", response)

            return response
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
        except Exception as e:
            print(f"Failed to handle solana_api_bot action: {e}")