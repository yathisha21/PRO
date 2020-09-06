# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('diabetes.pkl', 'rb'))
@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/diabetes", methods=['GET','POST'])
def diabetes():
    if request.method == 'POST':
        Pregnancies=int(request.form['Pregnancies'])
        Glucose= int(request.form['Glucose'])
        BloodPressure= int(request.form['BloodPressure'])
        SkinThickness= int(request.form['SkinThickness'])
        Insulin= int(request.form['Insulin'])
        BMI= float(request.form['BMI'])
        DiabetesPedigreeFunction= float(request.form['DiabetesPedigreeFunction'])
        Age=int(request.form['Age'])
        prediction=model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if prediction==1:
            return render_template('index.html', prediction_text="Oops! The predicted value is [1]. The person seems to have diabetes.")
        else:
            return render_template('index.html', prediction_text="Great! The predicted value is [0].The person does not have diabetes.")
    else:
        return render_template('index.html')
if __name__=="__main__":
    app.run(debug=True)
