import os
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF

def get_data():
    crop_recommendation_train = pd.read_csv(os.path.join('processed', 'crop_recommendation_train.csv'), sep=',')
    crop_recommendation_test = pd.read_csv(os.path.join('processed', 'crop_recommendation_test.csv'), sep=',')
    return [crop_recommendation_train, crop_recommendation_test]

if __name__ == '__main__':
    [crop_recommendation_train, crop_recommendation_test] = get_data()
    
    x_train = crop_recommendation_train.drop(labels=['label'], axis=1)
    x_test = crop_recommendation_test.drop(labels=['label'], axis=1)
    
    y_train = crop_recommendation_train['label']
    y_test = crop_recommendation_test['label']
       
    
    # Random Forest Classifier model
    rfr_model = RandomForestClassifier(n_estimators=30, max_depth=10)
    rfr_model.fit(x_train, y_train)

    # save ml model
    with open('models/rfr_crop_recommendation_model.pkl', 'wb') as f:
        pickle.dump(rfr_model, f)