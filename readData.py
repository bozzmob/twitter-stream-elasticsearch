from elasticsearch import Elasticsearch
import sys
import csv
import time

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