import os
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn import svm
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

def get_data():
    crop_production_train = pd.read_csv(os.path.join('processed', 'crop_production_train.csv'), sep=',')
    crop_production_test = pd.read_csv(os.path.join('processed', 'crop_production_test.csv'), sep=',')
    return [crop_production_train, crop_production_test]

if __name__ == '__main__':
    [crop_production_train, crop_production_test] = get_data()
    
    x_train = crop_production_train.drop(labels=['Production'], axis=1)
    x_test = crop_production_test.drop(labels=['Production'], axis=1)
    
    y_train = crop_production_train['Production']
    y_test = crop_production_test['Production']
    
    
    # Random Forest Regressor model
    rfr_model = RandomForestRegressor(n_estimators=70, max_depth=12)
    rfr_model.fit(x_train, y_train)

    # save ml model
    with open('models/rfr_crop_yield_prediction_model.pkl', 'wb') as f:
        pickle.dump(rfr_model, f)
