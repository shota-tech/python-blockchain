# Python Blockchain

Blockchain implementation using Python.


## What I learned
- How to implement blockchain.
- What is Proof of Work.
- How to use Flask.


## Prerequisites
- python3
- pipenv


## How to start nodes
1. Install dependencies.
   ```sh
   pipenv install
   ```
2. Activate virtualenv.
   ```sh
   pipenv shell
   ```
3. Start node 1.
   ```sh
   python3 -m server 5000
   ```
4. Start node 2 on a different port in a different window.
   ```sh
   pipenv shell
   python3 -m server 5001
   ```


## Usage
```sh
# Create a new transaction.
curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "d4ee26eee15148ee92c6cd394edd974e",
 "recipient": "someone-other-address",
 "amount": 5
}' "http://localhost:5000/transactions/new"

# Mine a new block.
curl "http://localhost:5000/mine"

# Get the blockchain.
curl "http://localhost:5000/chain"

# Register node 2 on node 1.
curl -X POST -H "Content-Type: application/json" -d '{
   "nodes": ["http://localhost:5001"]
}' "http://localhost:5000/nodes/register"

# Mine some new blocks on node 2.
curl "http://localhost:5001/mine"
curl "http://localhost:5001/mine"
curl "http://localhost:5001/mine"

# Get the blockchain of node 2.
curl "http://localhost:5000/chain"

# Replace the blockchain of node 1 with that of node 2 by the Consensus Algorithm.
curl "http://localhost:5000/nodes/resolve"

# Get the blockchain of node 1. 
curl "http://localhost:5000/chain"
```


## References
- https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
- https://qiita.com/hidehiro98/items/841ece65d896aeaa8a2a
