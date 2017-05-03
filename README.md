# Twitter Stream API, Elastic Search
Read data from Twitter Stream API and push it to Elastic Search. Read data from Elastic Search and generate a CSV.

##Usage

### Twitter Stream API
Get live tweets from Twitter's Stream API and pushes the data to Elastic search
Run
```python getStream.py keyword```
Example - ```python getStream.py india```

### Read Data and create CSV (Command line)
Read data that match the search keyword from elastic search and write it into a CSV file
Run
```python readData.py keyword```
Example - ```python readData.py india```

### Download CSV (REST API)
You can download a CSV file of data that contains your search keyword.

Run
```python downloadCSV.py```
URL - ```http://127.0.0.1:5000/getCSV?keyword=search-keyword```
Example - ```http://127.0.0.1:5000/getCSV?keyword=india```

## Example CSV
There are sample/example CSV's provided already for reference. Search keywords were - KKR, sports, india.