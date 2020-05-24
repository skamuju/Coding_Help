from flask import Flask, jsonify, request
from pymongo import MongoClient, operations
app = Flask(__name__)

@app.route("/home", methods=['GET'])
def home():
    return ('Home Page')

@app.route('/register', methods= ['POST'])
def register():
    data = request.get_json()
    client = MongoClient('mongodb+srv://skamuju:ovio2004@cluster0-wvgmv.mongodb.net/test?retryWrites=true&w=majority')
    db = client['YSL']
    collection = db['test']
    post =  {'username': data['username'], 'email': data['email'], }
    collection.insert_one(post)
    return jsonify({"success": True})

app.run(host="0.0.0.0")