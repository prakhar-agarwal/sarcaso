Polarity Service
================


OBTAINING DATA FILE
-------------------
`$ python parse_sentic.py > data.json`

Convert all the `'` to `"`

This will also change all the `'s` to `"s`
so change that to `'s` again 

In vim

`:%s/'/"/g`

To check if the file is json compliant
and pretty indent it

`:%!python -m json.tool`


INITIALIZING DB
---------------

Run the eve rest server

`$ python run.py`

Clean any data if it already exists

`$ curl -i -X DELETE http://127.0.0.1:5000/concepts`

Feed the data via post request

`$ curl -i -X POST -d @data.json -H 'Application-Content: application/json' http://127.0.0.1:5000/concepts`



CITATIONS
---------
+ E. Cambria, D. Olsher, and D. Rajagopal. SenticNet 3: A Common and Common-Sense Knowledge Base for Cognition-Driven Sentiment Analysis. In: AAAI, pp. 1515-1521, Quebec City (2014)
