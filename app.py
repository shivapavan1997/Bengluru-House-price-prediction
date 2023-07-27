from flask import Flask, request, render_template, url_for, redirect
from server.util import predict_price

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/submit', methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        total_sqft = int(request.form['total_sqft'])  # From homepage.html form id=total_sqft
        location = (request.form['location'])
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])
        prediction = predict_price(location, total_sqft, bath, bhk)

        # Render the homepage.html template with the prediction result
        return render_template('homepage.html', prediction=prediction)
    else:
        return render_template('homepage.html')


if __name__ == '__main__':
    app.run(debug=False)
