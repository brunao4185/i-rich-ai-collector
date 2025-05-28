from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)
CSV_FILE = 'trades.csv'

# Cria o arquivo com cabeçalho, se não existir
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'direction', 'macd', 'hist', 'ha_color', 'range_percent', 'volume', 'price'])

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("📩 Novo dado recebido:", data)
    with open(CSV_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            data.get('timestamp'),
            data.get('direction'),
            data.get('macd'),
            data.get('hist'),
            data.get('ha_color'),
            data.get('range_percent'),
            data.get('volume'),
            data.get('price')
        ])
    return jsonify({'status': 'ok'})

@app.route('/files', methods=['GET'])
def list_csv_files():
    files = [f for f in os.listdir('.') if f.endswith('.csv')]
    return jsonify(files)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
