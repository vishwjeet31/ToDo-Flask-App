from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)
db = client.test
collection = db['TO -do Page']

app = Flask(__name__)

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = request.json
    item_name = data.get('itemName')
    item_description = data.get('itemDescription')

    # Insert data into MongoDB
    collection.insert_one({
        'itemName': item_name,
        'itemDescription': item_description
    })

    return 'To-Do item submitted successfully to database', 200

@app.route('/view', methods=['GET'])
def view_data():
    data = list(collection.find({}, {'_id': 0}))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

