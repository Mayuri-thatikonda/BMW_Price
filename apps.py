from flask import Flask, render_template, request
import requests
import pickle
import sklearn
import numpy as np
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('bmw.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index1.html')
standard_to = StandardScaler()


@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        year=(request.form['year'])
        transmission=(request.form['transmission'])
        if(transmission=='Automatic'):
            transmission=0
        else:
            transmission=1
        mileage=(request.form['mileage'])
        fuelType=(request.form['fuelType'])
        if(fuelType=='Diesel'):
            fuelType=0
        elif(fuelType=='Electric'):
            fuelType=1
        elif(fuelType=='Hybrid'):
            fuelType=2
        elif(fuelType=='Other'):
            fuelType=3
        else:
            fuelType=4
        
        tax=(request.form['tax'])
        mpg=(request.form['mpg'])
        engineSize=(request.form['engineSize'])
        model_car=(request.form['model_car'])
        if(model_car=='1'):
            model_car=1
        elif(model_car=='2'):
            model_car=2
        elif(model_car=='3'):
            model_car=3
        elif(model_car=='4'):
            model_car=4
        elif(model_car=='5'):
            model_car=5
        elif(model_car=='6'):
            model_car=6
        elif(model_car=='7'):
            model_car=7
        elif(model_car=='8'):
            model_car=8
        elif(model_car=='X1'):
            model_car=9
        elif(model_car=='X2'):
            model_car=10
        elif(model_car=='X3'):
            model_car=11
        elif(model_car=='X4'):
            model_car=12
        elif(model_car=='X5'):
            model_car=13
        elif(model_car=='X6'):
            model_car=14
        elif(model_car=='X7'):
            model_car=15
        elif(model_car=='i3'):
            model_car=16
        elif(model_car=='i8'):
            model_car=17
        elif(model_car=='M2'):
            model_car=18
        elif(model_car=='M3'):
            model_car=19
        elif(model_car=='M4'):
            model_car=20
        elif(model_car=='M5'):
            model_car=21
        elif(model_car=='M6'):
            model_car=22
        elif(model_car=='Z3'):
            model_car=23
        else:
            model_car=24

            
            

        
        	
        
        prediction=model.predict([[year,transmission,mileage,fuelType,tax,mpg,engineSize,model_car]])
        output=(prediction)
        return render_template('index.html',prediction_text="Your Car Pricee is {}".format(output))
    
    return render_template("index.html")

    

    
if __name__=="__main__":
    

    
    
     app.run(debug=True)


