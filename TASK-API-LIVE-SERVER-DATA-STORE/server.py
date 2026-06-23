from flask import Flask, request, jsonify

app = Flask(__name__)

sensor_data = []

@app.route('/sensor', methods=['POST'])
def sensor():
    data = request.json
    sensor_data.append(data)

    return jsonify({
        "message": "Data Stored",
        "data": data
    })

@app.route('/data', methods=['GET'])
def data():
    return jsonify(sensor_data)

if __name__ == '__main__':
    app.run(debug=True)