from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/circulating_supply', methods=['GET'])
def circulating_supply():
    total_supply = 10_000_000_000
    burned_amount = 301_298_369.4770529
    circulating_supply_value = total_supply - burned_amount
    return jsonify({"circulating_supply": circulating_supply_value})

@app.route('/total_supply', methods=['GET'])
def total_supply():
    total_supply_value = 10_000_000_000  # Replace this with your actual total supply if it changes dynamically
    return jsonify({"total_supply": total_supply_value})

if __name__ == '__main__':
    app.run()
