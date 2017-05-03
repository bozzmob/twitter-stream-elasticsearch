from flask import Flask,send_file,request
from elasticsearch import Elasticsearch
import csv
import time
app = Flask(__name__)

@app.route('/getCSV')
def getCSVfile():
    keyword = request.args.get('keyword')
    filename = createCSV(keyword)
    return send_file(filename,
                     mimetype='text/csv',
                     attachment_filename=filename,
                     as_attachment=True)

def createCSV(keyword):
    es = Elasticsearch()
    res = es.search(index="tweetstream", doc_type="tweet", body={"query": {"match": {"message": keyword}}}, size=1000, from_=0)
    print("%d tweets found\n" % res['hits']['total'])

    filename = keyword + str(time.time()) + ".csv";
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