INITIALIZING DB
===============

+ run the eve rest server
`$ python run.py`

+ clean any data if it already exists
`$ curl -i -X DELETE http://127.0.0.1:5000/concepts`

+ feed the data via post request
`$ curl -i -X POST -d @db.json -H 'Application-Content: application/json' \
        http://127.0.0.1:5000/concepts`
