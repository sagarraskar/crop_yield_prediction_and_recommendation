import pickle
import json
import numpy as np
import joblib
__locations = None
__data_columns_yield = None
__data_columns_recommend = None
__yield_model = None
__recommend_model = None


def get_estimated_yield(state, district, crop, season, rainfall):
    load_served_artifacts()
    global __data_columns_yield
    global __yield_model
    state_pkl = open('state_encoder.pkl', 'rb')
    le_state = pickle.load(state_pkl)
    state_pkl.close()
    state = le_state.fit_transform([state])
    
    crop_pkl = open('crop_encoder.pkl', 'rb')
    le_crop = pickle.load(crop_pkl)
    crop_pkl.close()
    crop = le_crop.fit_transform([crop])
    rainfall_scaler = joblib.load('yield_rainfall_scaler.gz')
    rainfall = rainfall_scaler.fit_transform(np.array([rainfall]).reshape(-1,1))
    try:
        loc_index = __data_columns_yield.index("season_" + season)
    except:
        loc_index = -1
    print(loc_index, "Season_" + season)
    x = np.zeros(len(__data_columns_yield))
    x[0] = state
    x[1] = crop
    x[2] = rainfall
    if loc_index >= 0:
        x[loc_index] = 1
    
    return round(__yield_model.predict([x])[0], 2)
    

def recommend_crop(State, District, N, P, K, temperature, humidity, ph, rainfall):
    load_served_artifacts()
    global __data_columns_recommend
    global __recommend_model
    x = np.zeros(len(__data_columns_recommend))
    N_scaler = joblib.load('recommendation_N_scaler.gz')
    N = N_scaler.fit_transform(np.array([N]).reshape(-1,1))
    
    P_scaler = joblib.load('recommendation_P_scaler.gz')
    P = P_scaler.fit_transform(np.array([P]).reshape(-1,1))
    
    K_scaler = joblib.load('recommendation_K_scaler.gz')
    K = K_scaler.fit_transform(np.array([K]).reshape(-1,1))
    
    temperature_scaler = joblib.load('recommendation_temperature_scaler.gz')
    temperature = temperature_scaler.fit_transform(np.array([temperature]).reshape(-1,1))
    
    ph_scaler = joblib.load('recommendation_ph_scaler.gz')
    ph = ph_scaler.fit_transform(np.array([ph]).reshape(-1,1))
    
    rainfall_scaler = joblib.load('recommendation_rainfall_scaler.gz')
    rainfall = rainfall_scaler.fit_transform(np.array([rainfall]).reshape(-1,1))
    x[0] = N
    x[1] = P
    x[2] = K
    x[3] = temperature
    x[4] = humidity
    x[5] = ph
    x[6] = rainfall
    
    return __recommend_model.predict([x])[0]


def load_served_artifacts():
    print("loading saved arifacts...start")
    global __data_columns_recommend
    global __data_columns_yield
    global __locations
    global __yield_model
    global __recommend_model
    with open("yield_columns.json", 'r') as f:
        __data_columns_yield = json.load(f)['data_columns']
    with open("recommendation_columns.json", 'r') as f:
        __data_columns_recommend = json.load(f)['data_columns']
    with open("crop_yield_prediction_dt_model.pickle", 'rb') as f:
        __yield_model = pickle.load(f)
    with open("crop_recommendation_rfc.pickle", 'rb') as f:
        __recommend_model = pickle.load(f)
    print("Loading saved artifacts...done")


if __name__ == "__main__":
    
    print(get_estimated_yield("Assam", "BAKSA", "Rice", "kharif", 1366.7))
    print(recommend_crop("state", "district", 90, 42, 43, 20.879744, 82.002744, 6.502985, 202.935536))