MONGO_DBNAME = 'concepts'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

ITEM_METHODS = ['GET', 'PATCH', 'DELETE', 'PUT']

ACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20

concepts = {
    'item_title' : 'concept',

    'cache_control': 'max-age=10,must-revalidate',
    
    'cache_expires': 10,
    
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'name'
    },
    
    'schema': {
        'name': {
            'type': 'string',
            'required': True,
            'unique': True,
        },
        'semantics':{
            'type': 'list'
        },
        'pleasantness': {
            'type': 'string',
        },
        'attention': {
            'type': 'string',
        },
        'polarity': {
            'type': 'string',
        },
        'aptitude': {
            'type': 'string',
        },
        'sensitivity': {
            'type': 'string',
        },
    }
}

DOMAIN = {
    'concepts': concepts,
}
