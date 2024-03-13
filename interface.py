from flask import Flask, request, jsonify
import config
from Project.utils import Medical_Insurance
import numpy as np

app=Flask(__name__)
@app.route("/")
def get_home():
    return "Hello Welcome to HomePage."

@app.route("/predict_charges",methods= ["POST","GET"])
def get_insurance():
    if request.method=="POST":
        data=request.form
        print("User Input Data: ",data)
        age=eval(data["age"])
        gender=data["gender"]
        bmi=eval(data["bmi"])
        children=int(data["children"])
        smoker=data["smoker"]
        region=data["region"]

        med_obj=Medical_Insurance(age,gender,bmi,children,smoker,region)
        charges=med_obj.get_predicted_charges()
        return  jsonify({"Result":f"Predicted Medical Charges are: {charges[0]}"})
    
if __name__=="__main__":
    app.run()