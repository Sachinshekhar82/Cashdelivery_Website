import sqlite3
import time
import random
from flask import Flask, request, jsonify
from flask_cors import CORS




app = Flask(__name__)
CORS(app)

DATABASE = 'cashdash.db'

# All the helper functions and route definitions are the same...
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return "CashDash Backend API is running."

@app.route("/order", methods=['POST'])
def create_order():
    data = request.get_json()
    user_id = "user_001"
    amount = data.get("amount")
    address = data.get("address")

    if not all([amount, address]):
        return jsonify({"error": "Missing amount or address"}), 400

    try:
        amount = float(amount)
        if amount <= 0: raise ValueError
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid amount provided"}), 400

    delivery_fee = 50.0
    service_fee = 25.0
    total_charge = amount + delivery_fee + service_fee
    otp = str(random.randint(100000, 999999))
    order_id = f"ord_{int(time.time())}"

    conn = get_db_connection()
    try:
        conn.execute(
            'INSERT INTO orders (order_id, user_id, amount, address, total_charge, otp, status) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (order_id, user_id, amount, address, total_charge, otp, 'pending_assignment')
        )
        conn.commit()
    except Exception as e:
        print(f"Database error: {e}")
        return jsonify({"error": "Failed to create order due to a database issue."}), 500
    finally:
        conn.close()

    print(f"[ORDER CREATED] ID: {order_id}, Amount: {amount}, OTP: {otp}")
    
    return jsonify({
        "message": "Order created successfully! We are finding a delivery partner.",
        "order_id": order_id,
        "otp_for_next_step": otp
    }), 201

# This is now only for running the server directly
if __name__ == '__main__':
    app.run(debug=True, port=5000)


