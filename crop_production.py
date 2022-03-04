import os
import pickle
import pandas as pd
import settings
import json
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn import svm
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
import pickle
def get_data():
    crop_production_train = pd.read_csv(os.path.join(settings.PROCESSED_DIR, settings.CROP_PRODUCTION_TRAIN_DATA), sep=',')
    crop_production_test = pd.read_csv(os.path.join(settings.PROCESSED_DIR, settings.CROP_PRODUCTION_TEST_DATA), sep=',')
    return [crop_production_train, crop_production_test]

if __name__ == '__main__':
    [crop_production_train, crop_production_test] = get_data()
    
    x_train = crop_production_train.drop(labels=['Production'], axis=1)
    x_test = crop_production_test.drop(labels=['Production'], axis=1)
    
    y_train = crop_production_train['Production']
    y_test = crop_production_test['Production']
    
    # Linear Regression
    # lr_model = LinearRegression()
    # lr_model.fit(x_train, y_train)
    # lr_model.score(x_test, y_test)    
    
    # Decision Tree Regressor
    # Dt_model = DecisionTreeRegressor()
    # Dt_model.fit(x_train, y_train)
    # Dt_model.score(x_test, y_test)
    
    # Random Forest Regressor model
    rfr_model = RandomForestRegressor(n_estimators=70, max_depth=12)
    rfr_model.fit(x_train, y_train)
    rfr_model.feature_names = list(x_train.columns.values)
    # save model
    # pickle.dump(rfr_model, open(os.path.join(settings.BACKEND_DIR, settings.CROP_PRODUCTION_MODEL), 'wb'))
    
    # svr_model = svm.SVR()    
    # svr_model.fit(x_train, y_train)
    # svr_model.score(x_test, y_test)
    
    # Gaussian Process Regression
    
    # kernel = 1 * RBF(length_scale=1.0, length_scale_bounds=(1e-2, 1e2))
    # gaussian_process = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=9)
    # gaussian_process.fit(x_train, y_train)
    # gaussian_process.score(x_test, y_test)
    
    # storing crop production column names
    columns = {
        'data_columns' : [col for col in x_train.columns]
    }
    with open(os.path.join(settings.BACKEND_DIR, 'yield_columns.json'), 'w') as f:
        f.write(json.dumps(columns))
        

    with open(os.path.join(settings.BACKEND_DIR,'crop_yield_prediction_rfr_model.pickle'), 'wb') as f:
        pickle.dump(rfr_model, f)
