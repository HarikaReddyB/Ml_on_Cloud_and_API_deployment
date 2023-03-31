import numpy as np
from flask import Flask, request,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='The Predictive analysis of Home price is $ {}'.format(output))

{
    "name": "Ml_on_Cloud_and_API_deployment",
    "version": "1.0.0",
    "description": "",
   "scripts": {
        "build": "echo \"No build specified\" && exit 1",
        "test": "echo \"No test specified\" && exit 1",
       "start": "node index.js"
     },
    "repository": {
        "type": "git",
        "url": "git+https://github.com/HarikaReddyB/Ml_on_Cloud_and_API_deployment.git"
    },
    "author": "",
    "license": "ISC",
    "bugs": {
        "url": "https://github.com/HarikaReddyB/Ml_on_Cloud_and_API_deployment/issues"
    },
    "homepage": "https://github.com/HarikaReddyB/Ml_on_Cloud_and_API_deployment#readme"
}

if __name__ == "__main__":
    app.run(debug=True)
