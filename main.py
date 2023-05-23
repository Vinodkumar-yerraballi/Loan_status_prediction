from flask import Flask,request,render_template



#Create a new Flask instance
app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def prediction():
    if request.method == 'POST':
        return render_template('prediction.html')
    






if __name__== '__main__':
    app.run(debug=True)
