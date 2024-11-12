import pandas as pd
from crop_recommendation_repo.mapping import CropDictionary 
from crop_recommendation_repo.crop_recommendation import model,scaler

def getCropRecommendation(lstFetchedData):
    df = pd.DataFrame(lstFetchedData, columns=['N','P','K','temperature','humidity','ph','rainfall'])
    scaled_data = scaler.transform(df)

    prediction = model.predict(scaled_data)
    predictedNames = [CropDictionary[item] for item in prediction]
    return predictedNames

def processDataAndGetCropRecommendation(form):
    n_nitrogen = float(form.get('n_nitrogen',0))
    p_phosphorus = float(form.get('p_phosphorus',0))
    k_potassium = float(form.get('k_potassium',0))
    temperature = float(form.get('temperature',0))
    humidity = float(form.get('humidity',0))
    ph = float(form.get('ph',0))
    rainfall = float(form.get('rainfall',0))
    
    data = [[n_nitrogen,p_phosphorus,k_potassium,temperature,humidity,ph,rainfall]]
    return getCropRecommendation(data)
    
    


