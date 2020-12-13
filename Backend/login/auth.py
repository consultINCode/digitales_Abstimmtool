#TODO logginf
import logging
#TODO hashing
from passlib.hash import argon2
import api.response_helper as Response
from models import Person,session
from flask import session as fsession
import uuid
import datetime
#TODO Response.abort
from flask import abort, request
import configparser
from functools import wraps, update_wrapper
import api.response_helper as Response


config = configparser.ConfigParser()
config.read('config.ini')

def login(data):

    email = data.form['email']
    password = data.form['password']
    print(email)
    print(password)
    user = session.query(Person).filter(Person.mail == email).first()
    print(user.password)
    print(password)
    if (argon2.verify(password, user.password)):
        sessionid = uuid.uuid4()
        print (sessionid)
        session_end = datetime.datetime.now() + datetime.timedelta(seconds=config.getint('Session','session_duration'))
        fsession[str(sessionid)] = {"user.id" : user.id, "session_end" : session_end}
        return Response.ok({"sessionID":sessionid})
    return Response.database_error()


# Decoraters

def logged_in(f):
    @wraps(f)
    def decorated_function(*args, **kws):
            if not 'Authorization' in request.headers:
                Response.unauthorized()
            token  = request.headers['Authorization']
            try: 
                userid  = fsession.get(token)   
            except:
                Response.unauthorized()
            if (userid == None):
                Response.unauthorized()
            if(fsession[token]["session_end"] < datetime.datetime.now()):
                fsession.pop(token)
                Response.unauthorized()
            session_end = datetime.datetime.now() + datetime.timedelta(seconds=config.getint('Session','session_duration'))
            fsession[token]["session_end"] = session_end
            fsession.update()
            return f(*args, **kws)            
    return decorated_function

def is_present(f):
    @wraps(f)
    def is_present_decorator(*args, **kws):
            if not 'Authorization' in request.headers:
                Response.unauthorized()
            token  = request.headers['Authorization']
            try: 
                userid  = fsession.get(token)["user.id"]  
            except:
                Response.unauthorized()
            if (userid == None):
                Response.unauthorized()
            user = session.query(Person).filter(Person.id == userid).first()
            if not (user.is_present):
                Response.unauthorized()
            return f(*args, **kws)            
    return is_present_decorator

def has_role(role):
    def decorator(fn):
        def wrapped_function(*args, **kwargs):
            if not 'Authorization' in request.headers:
                Response.unauthorized()
            token  = request.headers['Authorization']
            try: 
                userid  = fsession.get(token)["user.id"]  
            except:
                Response.unauthorized()
            if (userid == None):
                Response.unauthorized()
            user = session.query(Person).filter(Person.id == userid).first()
            if( user.role != role):
                Response.unauthorized()
            return fn(*args, **kwargs)
        return update_wrapper(wrapped_function, fn)      
    return decorator
