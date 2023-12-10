from flask import Flask,render_template,request
import numpy as np
import pickle

with open("crop_recommend.pkl",'rb') as f:
    model = pickle.load(f)
#create an object instance
app = Flask(__name__)
@app.route('/vaishu')
def check():
    return "Codegnan is in NBKR"
@app.route('/') #by default methods = ['GET']
def new():
    return render_template("crop.html")
@app.route('/predict',methods=['POST'])
def recommend():
    Nitrogen = int(request.form['Nitrogen'])
    phosphorus = int(request.form['phosphorus'])
    potassium = int(request.form['potassium'])
    temperature = int(request.form['temperature'])
    humidity = int(request.form['humidity'])
    ph = int(request.form['ph'])
    rainfall= int(request.form['rainfall'])
    
    input_data = np.array([[Nitrogen,phosphorus,potassium,temperature,humidity,ph,rainfall]])
    recommend_crop= model.predict(input_data)[0]
    print(recommend_crop)
    
    
    if recommend_crop == 0:
        recommend_crop = "apple"
    elif recommend_crop == 1:
        recommend_crop = "banana"
    elif recommend_crop == 2:
        recommend_crop = "blackgram"
    elif recommend_crop == 3:
        recommend_crop = "chickpea"
    elif recommend_crop == 4:
        recommend_crop = "coconut"
    elif recommend_crop == 5:
        recommend_crop = "coffee"
    elif recommend_crop == 6:
        recommend_crop = "cotton"
    elif recommend_crop == 7:
        recommend_crop = "grapes"
    elif recommend_crop == 8:
        recommend_crop = "jute"
    elif recommend_crop == 9:
        recommend_crop = "kidneybeans"
    elif recommend_crop == 10:
        recommend_crop = "lentil"
    elif recommend_crop == 11:
        recommend_crop = "maize"
    elif recommend_crop == 12:
        recommend_crop = "mango"
    elif recommend_crop == 13:
        recommend_crop = "mothbeans"
    elif recommend_crop == 14:
        recommend_crop = "mungbean"
    elif recommend_crop== 15:
        recommend_crop = "muskmelon"
    elif recommend_crop== 16:
        recommend_crop ="orange"
    elif recommend_crop == 17:
       recommend_crop = "papaya"
    elif recommend_crop == 18:
        recommend_crop = "pigeonpeas"
    elif recommend_crop == 19:
        recommend_crop = "pomegranate"
    elif recommend_crop == 20:
        recommend_crop ="rice"
    elif recommend_crop == 21:
        recommend_crop = "watermelon"
    else:
       recommend_crop = "No Crop"
        
    
    return render_template('crop.html', recommend_crop = recommend_crop)

if __name__=="__main__":
    app.run()
