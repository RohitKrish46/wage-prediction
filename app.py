from flask import Flask, render_template, request
import pickle


app = Flask(__name__)

with open('./models/model.pkl', 'rb') as file:
    model=pickle.load(file)

with open('./models/preprocessor.pkl', 'rb') as file:
    model=pickle.load(file)

@app.route('/')
def home():
    return render_template('test.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    return render_template('predict.html')

if __name__ == "__main__":
    app.run(debug=True)