# Installed flask,scikit-learn, pandas, pickle-mixin by writing (pip install lib_name) in terminal

import pandas as pd
import numpy as np
from flask import Flask, render_template, request
import pickle



app=Flask(__name__, template_folder='views')
data= pd.read_csv("Cleaned_Data.csv")

df = pickle.load(open('banglore_home_prices_model.pickle','rb'))
@app.route('/')
def index():

    locations = sorted(data['location'].unique())
    return render_template('index.html', locations = locations)

@app.route('/predict',methods = ['POST'])
def predict():
    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqft = request.form.get('total_sqft')

    print(location, bhk, bath, sqft)
    input = pd.DataFrame([[location,bhk,bath,sqft]],columns=['location','total_sqft','bath','bhk'])
    prediction = df.predict(input)[0] * 1e5



    return str(np.round(prediction,2))
if __name__ == "__main__" :
    app.run(debug=True,port=5001)




