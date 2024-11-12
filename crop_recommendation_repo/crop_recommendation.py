import pickle

modelFilePath = 'crop_recommendation_repo/pickle/crop_recommendation_mlp_model.pickle'
model = pickle.load(open(modelFilePath, "rb"))

scalerFilePath = 'crop_recommendation_repo/pickle/crop_recommendation_scaler.pickle'
scaler = pickle.load(open(scalerFilePath, "rb"))