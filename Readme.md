# Project Overview

This project provides a **decision-making agent** for the Solana blockchain. It processes user queries to either:
- Access a knowledge base
- Perform a token swap
- Collect more details

## Installation

Install dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Running Locally

Start the FastAPI server with the following command:

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

## Deployment

Refer to the `render.yaml` file for a sample Render service configuration. It defines the build and start commands required for deployment. 

**Note**: Since we are using a free plan, the server enters sleep mode when idle. This causes a delay of approximately 30 seconds for the first request as the server wakes up.

## Project Structure

- **`main.py`**: Main application entry point.
- **`chat.py`**: Configures API routing.
- **`config.py`**: Handles API configuration.
- **`DecisionMaker`**: Contains the decision-making logic.
- **`action_handler.py`**: Includes handlers for different actions.

## Assistants Used

We leveraged two AI agents from [Assister.ai](https://build.assisterr.ai) in this project:

1. **[Decision Maker Agent](https://build.assisterr.ai/model/decision_maker)**: This is our primary decision-making agent. It processes user queries, determines intents, and orchestrates actions such as accessing the knowledge base, executing token swaps, and performing smart contract interactions.

2. **[Solana API Bot](https://build.assisterr.ai/model/solana_api_bot)**: This agent supports the generation of JSON RPC requests when required, facilitating seamless integration with Solana's blockchain.

These agents together form the backbone of our decision-making and execution pipeline, enabling efficient and intelligent query handling.

## Usage

To interact with the system, send a POST request to:

```
/api/v1/chat
```

The request body should include a JSON object containing a `query` string.

Example:

```json
{
  "query": "Swap 10 SOL for USDC"
}
```

### Workflow:
1. **DecisionMaker** evaluates the query.
2. Determines whether to:
   - Look up the knowledge base
   - Perform token swap logic
3. Token swaps utilize `coin_list.txt` to fetch mint addresses.

## Example Configuration

A sample Render service configuration is included in `render.yaml` for deployment purposes.
