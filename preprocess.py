import os
import settings
import pandas as pd


def get_data():
    crop_production = pd.read_csv(os.path.join(settings.PROCESSED_DIR, settings.CROP_PRODUCTION_DATA), sep=',')
    crop_recommendation = pd.read_csv(os.path.join(settings.PROCESSED_DIR, settings.CROP_RECOMMENDATION_DATA), sep=',')
    return [crop_production, crop_recommendation]

if __name__ == '__main__':
    [crop_production, crop_recommendation] = get_data()

    # Data Analysis
# Graphs
    # statewise distribution
    # coorelation between feature
    # area vs production
    
    # Drop rows with null values
    crop_production.dropna(axis=0, inplace=True)
    crop_recommendation.dropna(axis=0, inplace=True)

    # Drop crops with less than 400 entries

    # Normalize values
    # crop_production = crop_production.apply(lambda x: (x - x.min()) / (x.max() - x.min()))
    # crop_recommendation = crop_recommendation.apply(lambda x: (x - x.min()) / (x.max() - x.min()))

    # encoding of categorical values

    # split dataset


    # Random Forest
    # SVM
    # Neural Network

