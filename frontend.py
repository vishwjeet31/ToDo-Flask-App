from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BACKEND_URL = 'http://13.233.129.131:8000'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    item_name = request.form['itemName']
    item_description = request.form['itemDescription']

    # Sending the POST request to backend
    form_data = {'itemName': item_name, 'itemDescription': item_description}
    requests.post(BACKEND_URL + '/submittodoitem', json=form_data)

    return 'To-Do item submitted successfully!'

@app.route('/view')
def view():
    response = requests.get(BACKEND_URL + '/view')
    data = response.json()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

