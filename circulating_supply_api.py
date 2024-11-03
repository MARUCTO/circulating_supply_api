from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_KEY = "YOUR_ETHERSCAN_API_KEY"
CONTRACT_ADDRESS = "0x7AfD0d633e0A2b1db97506d97CAdc880C894EcA9"
BURN_ADDRESS = "0x000000000000000000000000000000000000dead"

@app.route('/circulating_supply')
def circulating_supply():
    total_supply = get_total_supply()
    burned_amount = get_balance(BURN_ADDRESS)
    circulating_supply = total_supply - burned_amount
    return jsonify({"circulating_supply": circulating_supply})

def get_total_supply():
    url = f"https://api.etherscan.io/api?module=stats&action=tokensupply&contractaddress={CONTRACT_ADDRESS}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return int(data["result"])

def get_balance(address):
    url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress={CONTRACT_ADDRESS}&address={address}&tag=latest&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return int(data["result"])

if __name__ == '__main__':
    app.run()
