from flask import Flask
from flask import jsonify
from flask import request
import numpy as np
import pandas as pd


#Fetching The Data

X = np.load('image.npz')['arr_0']

y = pd.read_csv("labels.csv")['labels']

print(pd.Series(y).value_counts())

classes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

nclasses = len(classes)


X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=9, train_size=3500, test_size=500)



@app.route("/predict-alphabet", methods=[:POST])

def predict_data() :
    image = request.files.get("alphabet")

prediction = get_prediciton(image)

return jsonify({

   "prediction": prediction     

}), 200
