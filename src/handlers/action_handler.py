from enum import Enum

class ActionType(Enum):
    KNOWLEDGE_BASE = "knowledge_base"
    SWAP = "swap"
    ASKING_MORE_DETAILS = "asking_more_details"
    SOLANA_API_BOT = "solana_api_bot"
    SOMETHING_ELSE = "something_else"

class ActionHandler:
    @staticmethod
    def handle_knowledge_base(details: str, parameters: dict) -> dict:
        #print("Knowledge Base Action Triggered!")
        #print(f"Details: {details}")
        #print(f"Answer: {parameters.get('message', '')}")
        return {
        "agent_action": "knowledge_base",
        "parameters": parameters
    }

    @staticmethod
    def handle_swap(details: str, parameters: dict) -> dict:
        #print("Swap Action Triggered!")
        #print(f"Details: {details}")
        #if parameters:
            #print(f"Input Mint: {parameters.get('inputMint')}")
        #    print(f"Output Mint: {parameters.get('outputMint')}")
        #    print(f"Amount: {parameters.get('amount')}")
        #    print(f"Slippage: {parameters.get('slippageBps')} bps")
        #else:
        #    print("No parameters available - token may not be found")

        return {
        "agent_action": "swap",
        "parameters": parameters
    }

    @staticmethod
    def handle_asking_more_details(details: str, parameters: dict) -> dict:
        #print("More Details Needed!")
        #print(f"Details: {details}")
        #print(f"Question: {parameters.get('message', '')}")
        return {
        "agent_action": "asking_more_details",
        "parameters": parameters
    }

    @staticmethod
    def handle_solana_api_bot(details: str, parameters: dict) -> dict:
        #print("Solana API Bot Action Triggered!")
        #print(f"Details: {details}")
        #print(f"Message: {parameters.get('message', '')}")
        return {
        "agent_action": "solana_api_bot",
        "parameters": parameters
    }

    @staticmethod
    def handle_default(details: str) -> None:
        print("No specific handler for this action.")
        print(f"Details: {details}")