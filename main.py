from flask import Flask,request,render_template,jsonify
import numpy as np
import pickle
import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder


#Create a new Flask instance
app = Flask(__name__,template_folder='templates')

#Load the model
model = pickle.load(open('model.pkl','rb'))
data=pd.read_csv('loan_prediction.csv')
#LabelEncoding is
label=LabelEncoder()
data['Gender']=label.fit_transform(data['Gender'])
data['Married']=label.fit_transform(data['Married'])
data['Dependents']=label.fit_transform(data['Dependents'])
data['Self_Employed']=label.fit_transform(data['Self_Employed'])
data['Loan_ID']=label.fit_transform(data['Loan_ID'])
data['Property_Area']=label.fit_transform(data['Property_Area'])



@app.route('/')
def home():
    return render_template('prediction.html')
@app.route('/Prediction',methods=['POST'])
def predict():

    if request.method == 'POST':
        loan_id = request.form['loan_id']
        genders = request.form['gender']
        married = request.form['married_status']
        dependents = request.form['dependents']
        education = request.form['education']
        self_employed = request.form['self_employed']
        applicantincome = float(request.form['Applicantincome'])
        coapplicantincome = float(request.form['Coapplicantincome'])
        loanamount = float(request.form['Loanamount'])
        loan_amount_term = float(request.form['Loan_amount_term'])
        credit_history = float(request.form['Credit_history'])
        property_area = request.form['property_area']

        # Perform prediction using the model
        result = model.Prediction(loan_id, genders, married, dependents, education, self_employed, applicantincome, coapplicantincome, loanamount, loan_amount_term, credit_history, property_area)

        if result == 'N':
            prediction = "Not Successful "
        else:
            prediction = "Successful"

        return render_template('prediction.html', prediction_text="The Person  {} eligible for loan".format(prediction))







if __name__== '__main__':
    app.run(debug=True)
