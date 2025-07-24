from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict
import uvicorn

app = FastAPI()

origins = ["*"]  # Allow all origins for frontend communication

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory blockchain-like data
blockchain_data = {
    "chain_id": 999,
    "rpc_url": "https://GBTNetwork",
    "symbol": "GBT",
    "name": "GBTNetwork",
    "logo": "https://raw.githubusercontent.com/openai-user-assist/GBTNetworkAssets/main/logo.png",
    "balance": {"0xF7F965b65E735Fb1C22266BdcE7A23CF5026AF1E": "36000000000000000000000000000000"}
}

@app.get("/")
def root():
    return {"status": "GBTNetwork RPC Live", "network": blockchain_data["name"]}

@app.get("/balance/{address}")
def get_balance(address: str):
    return {
        "address": address,
        "balance": blockchain_data["balance"].get(address, "0")
    }

@app.get("/metadata")
def get_metadata():
    return {
        "chainId": blockchain_data["chain_id"],
        "rpc": blockchain_data["rpc_url"],
        "name": blockchain_data["name"],
        "currencySymbol": blockchain_data["symbol"],
        "logo": blockchain_data["logo"]
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8545)
