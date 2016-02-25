# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
# MONGO_USERNAME = 'user'
# MONGO_PASSWORD = 'user'
MONGO_DBNAME = 'rdltest'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# 'people' schema definition
rdl_schema = {
    'FileName': {
        'type': 'string',
        'required': True,
    },
    'DateCreated': {
        'type': 'datetime'
    },
	'LastUpdated': {
        'type': 'datetime'
    },
	'Parameters': {
        'type': 'list'
    },
	'ReportObjects': {
        'type': 'list'
    },    
    'DataSets': {
        'type': 'dict'
    },
    'TotalHours': {
        'type': 'number',
    },
}


rdls = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'rdls',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    'additional_lookup': {
        'url': 'regex("[\w\W]+")',
        'field': 'FileName'
    },
    'allow_unknown': True,
    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET'],

    'schema': rdl_schema
}

DOMAIN = {
    'rdls': rdls
}