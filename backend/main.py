import json
import os

from flask import Flask

#to deploy:
#gcloud run deploy --source .

#from pymongo import MongoClient

app = Flask(__name__)

#mongoClient = MongoClient('mongodb://127.0.0.1:27017')
#db = mongoClient.get_database('fremp_test_app1_db')
#col = db.get_collection('fremp_test_app1_col')

# $ mongo
# $ use fremp_test_app1_db
# $ db.fremp_test_app1_col.insertOne({'data': 'Hello World from MongoDB'})

@app.route('/api/get/')
def getdata():
    data = 'from bacsssdddddkend'
    return {'data': data}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
