from flask import Flask,request,render_template,jsonify
from project_app.utils import IrisDataset

app=Flask(__name__)

@app.route('/')
def abc():
    # return jsonify({'message' : 'send'})
    return render_template('index.html')

########################################################################################


@app.route('/predict',methods =['POST'])
def get_species():
     data = request.form  # dictionary
     print("Data is : ",data)

     SepalLengthCm  =   eval(data['SepalLengthCm'])           
     SepalWidthCm   =   eval(data['SepalWidthCm'])            
     PetalLengthCm  =   eval(data['PetalLengthCm'])           
     PetalWidthCm   =   eval(data['PetalWidthCm'])       

    #  SepalLengthCm  =   data.get('SepalLengthCm')      
    #  SepalWidthCm   =   data.get('SepalWidthCm')       
    #  PetalLengthCm  =   data.get('PetalLengthCm')        
    #  PetalWidthCm   =   data.get('PetalWidthCm') 


     pred_spec = IrisDataset(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm) 
     predicted_spieces = pred_spec.get_predict_Species()

     return render_template ('result.html' , prediction = predicted_spieces[0] )
app.run(debug = True)
