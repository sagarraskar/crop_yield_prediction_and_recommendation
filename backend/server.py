from flask import Flask, request, jsonify
from flask_cors import CORS
import util
app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return 'hi'

@app.route('/predict',  methods=['POST'])
def crop_yield_prediction():
    # get data from the body of the request
    data = request.json
    print(data)
    state = data['state']
    district = data['district']
    crop = data['crop']
    season = data['season']
    rainfall = float(data['rainfall'])
    response = jsonify({
        'estimated_yield': util.get_estimated_yield(state, district, crop, season, rainfall)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/recommend', methods=['POST'])
def crop_recommend():
    data = request.json
    print(data)
    
    n = float(data['n'])
    p = float(data['p'])
    k = float(data['k'])
    ph = float(data['ph'])
    humidity = float(data['humidity'])
    temperature = float(data['temperature'])
    rainfall = float(data['rainfall'])
    State = data['state']
    District = data['district']

    response = jsonify({
        'recommended_crop': util.recommend_crop(State, District, n, p, k, temperature, humidity, ph, rainfall)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting python Flask Server For Crop Yield Prediction & Recommendation...")
    app.run()
