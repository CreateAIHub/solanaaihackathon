from enum import Enum

class ActionType(Enum):
    KNOWLEDGE_BASE = "knowledge_base"
    SWAP = "swap"
    ASKING_MORE_DETAILS = "asking_more_details"
    SOMETHING_ELSE = "something_else"

class ActionHandler:
    @staticmethod
    def handle_knowledge_base(details: str, parameters: dict) -> None:
        print("Knowledge Base Action Triggered!")
        print(f"Details: {details}")
        print(f"Answer: {parameters.get('message', '')}")

    @staticmethod
    def handle_swap(details: str, parameters: dict) -> None:
        print("Swap Action Triggered!")
        print(f"Details: {details}")
        if parameters:
            print(f"Input Mint: {parameters.get('inputMint')}")
            print(f"Output Mint: {parameters.get('outputMint')}")
            print(f"Amount: {parameters.get('amount')}")
            print(f"Slippage: {parameters.get('slippageBps')} bps")
        else:
            print("No parameters available - token may not be found")

    @staticmethod
    def handle_asking_more_details(details: str, parameters: dict) -> None:
        print("More Details Needed!")
        print(f"Details: {details}")
        print(f"Question: {parameters.get('message', '')}")

    @staticmethod
    def handle_default(details: str) -> None:
        print("No specific handler for this action.")
        print(f"Details: {details}")