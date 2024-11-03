from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# Constants
CONTRACT_ADDRESS = "0x7AfD0d633e0A2b1db97506d97CAdc880C894EcA9"  # Replace with your contract address
BURN_ADDRESS = "0x000000000000000000000000000000000000dead"
API_KEY = "YOUR_ETHERSCAN_API_KEY"  # Replace with your actual Etherscan API key
DECIMALS = 9  # Adjust based on your token’s decimals

def get_total_supply():
    """Retrieve the total supply of the token and deduct burned amount."""
    url = f"https://api.etherscan.io/api?module=stats&action=tokensupply&contractaddress={CONTRACT_ADDRESS}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    total_supply = int(data["result"]) / (10 ** DECIMALS)
    burned_amount = get_burned_amount()
    return total_supply - burned_amount  # Deduct burned amount

def get_burned_amount():
    """Retrieve the amount of tokens burned to the burn address."""
    url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress={CONTRACT_ADDRESS}&address={BURN_ADDRESS}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    burned_amount = int(data["result"]) / (10 ** DECIMALS)
    return burned_amount

@app.route('/total_supply')
def total_supply():
    """Endpoint to get total supply minus burned amount."""
    supply = get_total_supply()
    return jsonify({"total_supply": supply})

@app.route('/circulating_supply')
def circulating_supply():
    """Endpoint to get circulating supply."""
    total_supply = get_total_supply()
    circulating_supply = total_supply  # Already net of burned amount
    return jsonify({"circulating_supply": circulating_supply})

if __name__ == '__main__':
    app.run(debug=True)

