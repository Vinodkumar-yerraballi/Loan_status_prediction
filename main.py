from flask import Flask,request,render_template



#Create a new Flask instance
app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Prediction',methods=['GET','POST'])
def prediction():
    if request.method == 'POST':
        loan_id = request.POST.get('loan_id')
        genders = request.POST.get('genders')
        married = request.POST.get('married')
        dependents = request.POST.get('dependents')
        education = request.POST.get('education')
        self_employed = request.POST.get('self_employed')
        applicantincome = request.POST.get('applicantincome')
        coapplicantincome = request.POST.get('coapplicantincome')
        loanamount = request.POST.get('loanamount')
        loan_amount_term = request.POST.get('loan_amount_term')
        credit_history = request.POST.get('credit_history')
        property_area = request.POST.get('property_area')

        result=model.Prediction(loan_id,genders,married,dependents,education,self_employed,applicantincome,coapplicantincome,loanamount,loan_amount_term,credit_history,property_area)
        return render_template('prediction.html')
    






if __name__== '__main__':
    app.run(debug=True)
