from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient(
    "mongodb+srv://shantanu89:shan123@cluster0.ql9x8os.mongodb.net/?retryWrites=true&w=majority")
database = client['taskdb']
collection = database['taskcollection']


@app.route("/insert/mongo", methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name: number})
        return jsonify(str("succefully Inserted !!"))


@app.route("/update/mongo", methods=['POST'])
def update():
    if request.method == 'POST':
        name = request.json['name']
        collection.update_one({"name": name}, {"$set": {"number": 4444}})
        return jsonify(str("succefully Updated !!"))


if __name__ == '__main__':
    app.run()
