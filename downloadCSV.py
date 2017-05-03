from flask import Flask,send_file
import elasticsearch
from elasticsearch import Elasticsearch
import sys
import csv
import time
app = Flask(__name__)

@app.route('/getCSV') # this is a job for GET, not POST
def getCSVfile():
    filename = createCSV()
    return send_file(filename,
                     mimetype='text/csv',
                     attachment_filename=filename,
                     as_attachment=True)

def createCSV():
    es = Elasticsearch()
    res = es.search(index="tweetstream", doc_type="tweet", body={"query": {"match": {"message": "india"}}}, size=1000, from_=0)
    print("%d tweets found\n" % res['hits']['total'])

    filename = "india" + str(time.time()) + ".csv";
    with open(filename, 'w') as csvfile:
        fieldnames = ['Author', 'Date', 'Tweet']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for doc in res['hits']['hits']:
            print("Author: %s\ndate: %s\nTweet: %s\n" % (doc['_source']['author'],doc['_source']['date'],doc['_source']['message']))
            writer.writerow({'Author': doc['_source']['author'], 'Date': doc['_source']['date'], 'Tweet':doc['_source']['message']})

    return filename


if __name__ == "__main__":
    app.run()