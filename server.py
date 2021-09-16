import sys
from uuid import uuid4
from flask import Flask, jsonify, request

from blockchain import Blockchain


app = Flask(__name__)
node_identifier = str(uuid4()).replace('-', '')
blockchain = Blockchain()


@app.route('/nodes/register', methods=['POST'])
def register_node():
    values = request.get_json()

    nodes = values.get('nodes')
    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': '新しいノードが追加されました',
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201


@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()
    if replaced:
        response = {
            'message': 'チェーンが置き換えられました',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'チェーンが確認されました',
            'chain': blockchain.chain
        }

    return jsonify(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transactions():
    values = request.get_json()

    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    index = blockchain.new_transaction(
        values['sender'], values['recipient'], values['amount'])
    response = {'message': 'トランザクションはブロック {} に追加されました'.format(index)}
    return jsonify(response), 201


@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    blockchain.new_transaction(
        sender='0',
        recipient=node_identifier,
        amount=1,
    )

    block = blockchain.new_block(proof)

    response = {
        'message': '新しいブロックを採掘しました',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


if __name__ == '__main__':
    port = int(sys.argv[1])
    app.run(port=port)
