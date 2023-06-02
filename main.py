# save this as app.py
from flask import Flask, escape, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('knn.pkl', 'rb'))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method ==  'POST':
        
        gender = request.form['gender']
        married = request.form['married']
        dependents = request.form['dependents']
        education = request.form['education']
        employed = request.form['employed']
        credit = float(request.form['credit'])
        area = request.form['area']
        ApplicantIncome = float(request.form['ApplicantIncome'])
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        LoanAmount = float(request.form['LoanAmount'])
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])

        # gender
        if (gender == "Male"):
            gender=1
        else:
            gender=0
        
        # married
        if(married=="Yes"):
            married = 1
        else:
            married=0

        # dependents
        if(dependents=='1'):
            dependents = 1
            dependents = 0
            dependents = 0
        elif(dependents == '2'):
            dependents = 0
            dependents = 1
            dependents = 0
        elif(dependents=="3+"):
            dependents = 0
            dependents = 0
            dependents = 1
        else:
            dependents = 0
            dependents = 0
            dependents = 0  

        # education
        if (education=="Not Graduate"):
            education=1
        else:
            education=0

        # employed
        if (employed == "Yes"):
            employed=1
        else:
            employed=0

        # property area

        if(area=="Semiurban"):
            area=1
            area=0
        elif(area=="Urban"):
            area=0
            area=1
        else:
            area=0
            area=0


        ApplicantIncomelog = np.log(ApplicantIncome)
        totalincomelog = np.log(ApplicantIncome+CoapplicantIncome)
        LoanAmountlog = np.log(LoanAmount)
        Loan_Amount_Termlog = np.log(Loan_Amount_Term)

        prediction = model.predict([[credit, ApplicantIncomelog,LoanAmountlog, Loan_Amount_Termlog, totalincomelog, gender, married, dependents, education, employed,area ]])

        # print(prediction)

        if(prediction==1):
            prediction="Yes"
        else:
            prediction="No"


        return render_template("prediction.html", prediction_text="loan status is {}".format(prediction))




    else:
        return render_template("prediction.html")



if __name__ == "__main__":
    app.run(debug=True)
