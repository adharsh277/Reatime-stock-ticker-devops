import random
import time
import threading
from flask import Flask
from flask_socketio import SocketIO
from kafka import KafkaProducer
import json

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Wait for Kafka to be ready
def wait_for_kafka():
    while True:
        try:
            producer = KafkaProducer(
                bootstrap_servers='kafka:9092',
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            print("✅ Kafka Connected!")
            return producer
        except Exception as e:
            print("❌ Kafka not available yet. Retrying in 3s...")
            time.sleep(3)

producer = wait_for_kafka()

# Simulate stock data
def generate_stock_prices():
    stocks = ['AAPL', 'GOOG', 'TSLA', 'MSFT']
    while True:
        stock_data = {
            'symbol': random.choice(stocks),
            'price': round(random.uniform(100, 1500), 2),
            'timestamp': time.time()
        }
        producer.send('stock-price', stock_data)
        socketio.emit('stock_update', stock_data)
        time.sleep(2)

@app.route('/')
def index():
    return "Stock Ticker Backend Running"

if __name__ == '__main__':
    threading.Thread(target=generate_stock_prices).start()
    socketio.run(app, host='0.0.0.0', port=5000)

