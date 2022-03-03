from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/')
def home():
    return 'hi'

@app.route('/predict',  methods=['POST'])
def crop_yield_prediction():
    state = request.form['State']
    district = request.form['District']
    crop = request.form['Crop']
    season = request.form['Season']
    rainfall = float(request.form['rainfall'])
    response = jsonify({
        'estimated_yield': util.get_estimated_yield(state, district, crop, season, rainfall)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/recommend', methods=['POST'])
def crop_recommend():
    N = float(request.form['N'])
    P = float(request.form['P'])
    K = float(request.form['K'])
    ph = float(request.form['ph'])
    humidity = float(request.form['humidity'])
    temperature = float(request.form['temperature'])
    rainfall = float(request.form['rainfall'])
    State = float(request.form['State'])
    District = request.form['District']
    # pH, rainfall, temperature data remaining
    response = jsonify({
        'recommended_crop': util.recommend_crop(State, District, N, P, K, temperature, humidity, ph, rainfall)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting python Flask Server For Crop Yield Prediction & Recommendation...")
    app.run()
