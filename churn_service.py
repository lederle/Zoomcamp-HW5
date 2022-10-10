import pickle
from flask import Flask, request, jsonify

app = Flask('churn')

@app.route('/predict', methods = ['POST'])
def predict():
    client = request.get_json()
    prediction = predict_client(client, dv, model)
    churn = prediction >= 0.5

    res = {
        'churn_probability': float(prediction),
        'churn': bool(churn)
    }

    return jsonify(res)

with open('model2.bin', 'rb') as model_in:
    model = pickle.load(model_in)

with open('dv.bin', 'rb') as dv_in:
    dv = pickle.load(dv_in)

client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}

def predict_client(client, dict_vect, model):
    data = dict_vect.transform([client])
    return model.predict_proba(data)[0, 1]
 
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 9696)
