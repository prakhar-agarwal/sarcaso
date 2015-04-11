Polarity Service
================

A RESTful service for obtaining _common-sense knowldege_ using GET method

Example:

`$ curl -H 'Application-Content: application/json' http://127.0.0.1:5000/concepts/infuriated`

This will return a json object as:

```json
{
    "polarity": "-0.418", 
    "_updated": "Sat, 11 Apr 2015 06:47:28 GMT", 
    "name": "infuriated", 
    "sensitivity": "0.624", 
    "attention": "0.145", 
    "pleasantness": "-0.137", 
    "_links": {"self": {"href": "concepts/5528c39ed6194c7fe17869e2", "title": "concept"}, 
    "collection": {"href": "concepts", "title": "concepts"}, 
    "parent": {"href": "/", "title": "home"}}, 
    "aptitude": "-0.638", 
    "_created": "Sat, 11 Apr 2015 06:47:28 GMT", 
    "_id": "5528c39ed6194c7fe17869e2", 
    "_etag": "bf0d420db2f5eeaa2489d13461416ab60d50498b", 
    "semantics": ["enraged", "furious", "maddened", "angered", "indignantly"]
}
```


## OBTAINING DATA FILE

`$ python parse_sentic.py > data.json`

Convert all the `'` to `"`

This will also change all the `'s` to `"s`
so change that to `'s` again 

In vim

`:%s/'/"/g`

To check if the file is json compliant
and pretty indent it

`:%!python -m json.tool`


## INITIALIZING DB

Run the eve rest server

`$ python run.py`

Clean any data if it already exists

`$ curl -i -X DELETE http://127.0.0.1:5000/concepts`

Feed the data via post request

`$ curl -i -X POST -d @data.json -H 'Application-Content: application/json' http://127.0.0.1:5000/concepts`



## CITATIONS

+ E. Cambria, D. Olsher, and D. Rajagopal. SenticNet 3: A Common and Common-Sense Knowledge Base for Cognition-Driven Sentiment Analysis. In: AAAI, pp. 1515-1521, Quebec City (2014)
