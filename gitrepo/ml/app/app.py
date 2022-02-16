from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import pickle
import numpy as np
from torch import float32

titanic_app = Flask(__name__)
model = pickle.load(open('../model/finalized_model.pkl', 'rb'))

@titanic_app.route('/')
def index():
    return render_template('index.html')

@titanic_app.route('/predict', methods=['POST'])
def predict():
    inputlist = []
    
    #for x in request.form.values():
    #    inputlist.append(x)
    print("I am here1")
    #nt_features = [int(x) for x in request.form.values()]
    features = np.array([[float(request.form['age']), int(request.form['sex']), int(request.form['cabin'])]])

    #features = np.array(inputlist).reshape(1, -1)
    print(features)
    prediction = model.predict(features)
    print(prediction)
    return render_template('index.html', prediction_text='Prediction: {}'.format(prediction))

if __name__ == "__main__":
    titanic_app.run(debug=True)