import json
from flask import abort

def ok(message: dict):
    return message, 200

def ressource_not_found(message: dict):
    return message, 404

def wrong_format(message: dict):
    return message, 422

def server_error(message: dict):
    return message, 500
    
def database_error():
    return {"message":"database error"}, 500

def unauthorized():
    abort(401)