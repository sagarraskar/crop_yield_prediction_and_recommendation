from flask import Flask, request, jsonify
import util
app = Flask(__name__)


@app.route('/predict',  methods=['POST'])
def get_location_names():
    State = float(request.form['State'])
    District = request.form['District']
    Crop = int(request.form['Crop'])
    Season = int(request.form['Season'])
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/recommend', methods=['POST'])
def predict_home_price():
    N = float(request.form['N'])
    P = float(request.form['P'])
    K = float(request.form['K'])
    pH = float(request.form['pH'])
    State = float(request.form['State'])
    District = request.form['District']
    response = jsonify({
        'estimated_yield': util.recommend_crop(State, District, N, P, K)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting python Flask Server For Crop Yield Prediction & Recommendation...")
    app.run()
