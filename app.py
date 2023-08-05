from flask import Flask, render_template, request
import pickle


app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

try:
    model = pickle.load(open('model.pkl', 'rb'))
except Exception as e:
    print("Error loading the model:", e)

# @app.route('/index')
# def index():
#     return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input features from the form
    location = request.form['location']
    bedrooms = float(request.form['bedrooms'])
    bathrooms = float(request.form['bathrooms'])
    sqft = float(request.form['sqft'])
    saleyear = (request.form['saleyear'])
    datebuild = (request.form['datebuild'])
    parkfacil= request.form['parkfacil']
    street = request.form['street']
    room = (request.form['room'])
    House_age =(request.form['houseage'])
    # print("bedrooms---->",bedrooms,bathrooms,sqft,saleyear,datebuild,parkfacil,street,room,House_age)
    predicted_price = model.predict([[location,bedrooms, bathrooms, sqft,saleyear,datebuild,parkfacil,street,room,House_age,"0","0","0"]])[0]
    # print("predicted_price--->",predicted_price, "round-->",round(predicted_price,2))
    predicted_price = round(predicted_price,2)
    return render_template('index.html', prediction=predicted_price)

if __name__ == '__main__':
    # app.run(host='::', port=5000, debug=True)
    #app.run(port = 5000, host='127.0.0.1', threaded=True,debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)