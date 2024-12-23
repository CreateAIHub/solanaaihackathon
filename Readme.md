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
