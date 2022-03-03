import os
import settings
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import json
import pickle
def get_data():
    crop_production = pd.read_csv(os.path.join(settings.PROCESSED_DIR, settings.CROP_PRODUCTION_DATA), sep=',')
    crop_recommendation = pd.read_csv(os.path.join(settings.PROCESSED_DIR, settings.CROP_RECOMMENDATION_DATA), sep=',')
    return [crop_production, crop_recommendation]

if __name__ == '__main__':
    [crop_production, crop_recommendation] = get_data()

    
    ###############  Crop Recommendation ############################
    # normalize values in crop_recommendation
    crop_recommendation['N'] = preprocessing.MinMaxScaler().fit_transform(crop_recommendation['N'].values.reshape(-1, 1))
    crop_recommendation['P'] = preprocessing.MinMaxScaler().fit_transform(crop_recommendation['P'].values.reshape(-1, 1))
    crop_recommendation['K'] = preprocessing.MinMaxScaler().fit_transform(crop_recommendation['K'].values.reshape(-1, 1))
    crop_recommendation['temperature'] = preprocessing.MinMaxScaler().fit_transform(crop_recommendation['temperature'].values.reshape(-1,1))
    crop_recommendation['ph'] = preprocessing.MinMaxScaler().fit_transform(crop_recommendation['ph'].values.reshape(-1,1))
    crop_recommendation['rainfall'] = preprocessing.MinMaxScaler().fit_transform(crop_recommendation['rainfall'].values.reshape(-1,1))

    # split dataset 
    crop_recommendation_train, crop_recommendation_test = train_test_split(crop_recommendation, test_size=0.2, random_state=42)
    
    # save data
    crop_recommendation_train.to_csv(os.path.join(settings.PROCESSED_DIR, settings.CROP_RECOMMENDATION_TRAIN_DATA), sep=',', index=False)
    crop_recommendation_test.to_csv(os.path.join(settings.PROCESSED_DIR, settings.CROP_RECOMMENDATION_TEST_DATA), sep=',', index=False)

    ###################### Crop Yield Prediction #########################
    # Drop rows with null values
    crop_production.dropna(axis=0, inplace=True)
    crop_recommendation.dropna(axis=0, inplace=True)

    # get no. of rows of each crop
    crop_production_count = crop_production.groupby(['Crop']).size().reset_index(name='count')

    # get crop names having count less than 100
    removed_crops = crop_production_count[crop_production_count['count'] < 100]['Crop'].to_list()

    # get crop name from removed_crops file and add them to removed_crops list
    with open(os.path.join(settings.REPORT_DIR, "removed_crops.txt"), 'r') as f:
        for line in f:
            removed_crops.append(line.strip())

    # remove rows whose crops are in the list removed_crops
    crop_production = crop_production[~crop_production['Crop'].isin(removed_crops)]

    # create new column for production per unit area
    crop_production['Production'] = crop_production['Production'] / crop_production['Area']
    crop_production.drop(['Area'], axis=1, inplace=True)

    # normalize values
    crop_production['Rainfall'] = preprocessing.MinMaxScaler().fit_transform(crop_production['Rainfall'].values.reshape(-1, 1))
    
    # convert type of columns to 'category'
    crop_production['Crop'] = crop_production['Crop'].astype('category')
    crop_production['State'] = crop_production['State'].astype('category')
    crop_production['District'] = crop_production['District'].astype('category')
    crop_production['Season'] = crop_production['Season'].astype('category')

    # encoding of categorical values
    crop_production['State'] = preprocessing.LabelEncoder().fit_transform(crop_production['State'])
    output = open('state_encoder.pkl', 'wb')
    pickle.dump(preprocessing.LabelEncoder(), output)
    output.close()
    crop_production['Crop'] = preprocessing.LabelEncoder().fit_transform(crop_production['Crop'])
    output = open('crop_encoder.pkl', 'wb')
    pickle.dump(preprocessing.LabelEncoder(), output)
    output.close()
    crop_production = pd.get_dummies(crop_production, columns=['Season'])

    # drop columns which are not required
    crop_production.drop(['District', 'Year', 'Subdivision'], axis=1, inplace=True)

    
    # split dataset into training and test set
    crop_production_train, crop_production_test = train_test_split(crop_production, test_size=0.2, random_state=42)
    
    
    # save data
    crop_production_train.to_csv(os.path.join(settings.PROCESSED_DIR, settings.CROP_PRODUCTION_TRAIN_DATA), sep=',', index=False)
    crop_production_test.to_csv(os.path.join(settings.PROCESSED_DIR, settings.CROP_PRODUCTION_TEST_DATA), sep=',', index=False)