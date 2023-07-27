import json
import pickle
import pandas as pd
import warnings

# Ignore specific warning
warnings.filterwarnings("ignore", message="InconsistentVersionWarning")

__location = None
__data_columns = None
__model = None


def load_saved_artifacts():
    global __location
    global __data_columns
    global __model

    if __data_columns is None:
        print("Loading saved artifacts...")
        with open(r"D:\Machine_Learning\Projects\Real_estate\server\artifacts\columns.json", "r") as f:
            __data_columns = json.load(f)['data_columns']
            __location = __data_columns[3:]

    if __model is None:
        with open(r"D:\Machine_Learning\Projects\Real_estate\server\artifacts\best_model.pkl", "rb") as f:
            __model = pickle.load(f)


def get_location_names():
    load_saved_artifacts()
    return __location


def predict_price(location, sqft, bath, bhk):
    load_saved_artifacts()
    data_dict = dict.fromkeys(__data_columns, 0)
    predict_df = pd.DataFrame([data_dict])
    predict_df.total_sqft = sqft
    predict_df.bath = bath
    predict_df.bhk = bhk

    try:
        predict_df.loc[0, location] = 1
    except:
        print("Location Not found")

    return round(__model.predict(predict_df)[0], 2)


# Load the artifacts when the module is imported
load_saved_artifacts()
