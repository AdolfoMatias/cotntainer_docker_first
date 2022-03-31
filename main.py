import os
from flask import Flask
from flask import request
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import datasets
import pickle #seriaelizador

diabetes = datasets.load_diabetes()
X =diabetes.data[:, np.newaxis,2]

regr = linear_model.LinearRegression()
regr.fit(X, diabetes.target)
pickle.dump(reg, open("diabetes.pkl", "wb"))


app = Flask(__name__)

@app.route("/isALive")
def index():
    return "true"

@app.route("/prediction/", method=["GET"])
def get_predicition():
    feature = float(request.args.get("f"))
    modelo=pickle.load(open("diabetes.pkl", "rb"))
    pred= model.predict([[feature]])
    return str(pred)

    if __name__ =="__main__":
        if os.environ["ENVIRONMENT"] =="produtcion":
            app.run(port=80, host"0.0.0.0")