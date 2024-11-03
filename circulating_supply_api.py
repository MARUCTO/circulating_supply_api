from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("ETHERSCAN_API_KEY")
CONTRACT_ADDRESS = "0x7AfD0d633e0A2b1db97506d97CAdc880C894EcA9"
BURN_ADDRESS = "0x000000000000000000000000000000000000dead"
DECIMALS = 9  # Update this if your token has a different number of decimals

def get_total_supply():
    url = f"https://api.etherscan.io/api?module=stats&action=tokensupply&contractaddress={CONTRACT_ADDRESS}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    total_supply = int(data["result"]) / (10 ** DECIMALS)
    return total_supply

def get_burned_amount():
    url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress={CONTRACT_ADDRESS}&address={BURN_ADDRESS}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    burned_amount = int(data["result"]) / (10 ** DECIMALS)
    return burned_amount

@app.route('/total_supply')
def total_supply():
    total_supply = get_total_supply()
    return jsonify({"total_supply": total_supply})

@app.route('/circulating_supply')
def circulating_supply():
    total_supply = get_total_supply()
    burned_amount = get_burned_amount()
    circulating_supply = total_supply - burned_amount
    return jsonify({"circulating_supply": circulating_supply})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
