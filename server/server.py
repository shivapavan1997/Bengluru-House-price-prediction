from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'location': util.get_location_names()
    })
    response.headers.add('Access-Control_Allow-origin', '*')
    return response


@app.route('/predict_home_prices', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.predict_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control_Allow-origin', '*')
    return response


if __name__ == "__main__":
    print("starting python flask server for Home price prediction")
    app.run("0.0.0.0", port=5000)
