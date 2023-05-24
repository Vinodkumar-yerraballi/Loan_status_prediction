url = 'http://localhost:5000/results'
r = request.post(url,json={'ApplicantIncome':2000, 'CoaplicantIncome':1000, 'LoanAmount':400,
                             'Loan_Amount_Term':240,'Credit_History':1,'Self_Employed':1, 
                             'Property_Area':1, 'Married':1, 'Education':1, 'Gender':1 })

print(r.json())