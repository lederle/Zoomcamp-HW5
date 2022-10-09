import pickle

with open('model1.bin', 'rb') as model_in:
    model = pickle.load(model_in)

with open('dv.bin', 'rb') as dv_in:
    dv = pickle.load(dv_in)

client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}

data = dv.transform([client])
prediction = model.predict_proba(data)[0, 1]

print(prediction)
