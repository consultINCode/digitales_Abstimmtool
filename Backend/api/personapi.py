# pylint: disable=maybe-no-member

import json
import logging
import sys
import os
from passlib.hash import argon2
from random import choice
import api.response_helper as Response

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from models import Person,session

# Init logging
logging.basicConfig(filename='example.log', level=logging.DEBUG)

# Some example log lines
'''
logging.info("test")
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
'''

# Helpers
def model_as_dict(person):
       return {
                "id" : person.id,
                "name" : person.name,
                "is_present" : person.is_present,
                "role" : person.role
            }

#  get_all_persons()
# Gibt alle Benutzer zurück die in der Anwendung hinterlegt sind.
def get_all_persons():
    try:
        persons = session.query(Person).all()
        session.commit()
    except:
        Response.database_error()
    response = [] 
    for person in persons:
        response.append(
            model_as_dict(person)
        )
    json_response = json.dumps(response)
    return Response.ok(json_response)
    


# get_all_persons_checked_in()
# Gibt alle als anwesend makierten Benutzer zurück.
def get_all_persons_checked_in():
    try:
        persons = session.query(Person).filter(Person.is_present == True).all()
        session.commit()
    except:
        return Response.database_error()
    
    response = [] 
    for person in persons:
        response.append(
            model_as_dict(person)
        )
    json_response = json.dumps(response)
    print(json_response)
    return Response.ok(json_response)

### get_all_persons_checked_out()
# Gibt alle als abwesend makierten Benutzer zurück.
def get_all_persons_checked_out():
    try:
        persons = session.query(Person).filter(Person.is_present==False).all()
        session.commit()
    except:
        return Response.database_error()
    response = []
    for person in persons:
        response.append(model_as_dict(person))
    json_respose = json.dumps(response)
    return Response.ok(json.dumps(response))

# ### approve_minimal_voters()
# Überprüft ob Mindesanzahl an Wähler für eine MV vorhanden sind
def approve_minimal_voters():
    # TODO(Clarify conditions 0.5)
    num_checkedin_persons = len(get_all_persons_checked_in())
    num_all_persons = len(get_all_persons())
    if num_all_persons / num_checkedin_persons >= 0.5:
        return Response.ok({"approved":True, "message":"Minimum number reached"})
    else:
        return Response.ok({"approved":False, "message":"Minimum number not reached"})

# ### create_person(Person)
# Bekommt als Parameter mehrer Werte um eine Person anzulegen.
def create_person(data: dict):
    if 'name' not in data or not data['name']:
        return Response.wrong_format({"message": "Name missing!"})
    p1 = Person()
    p1.name = data['name']
    # TODO: Encpyt Passwords
    p1.password = ""
    p1.is_present = False
    p1.role = "0"
    session.add(p1)
    try:
         session.commit()
    except:
        Response.database_error()
    response = model_as_dict(p1)
    return Response.ok(response)
    

# ### delete_person(Person)
# Entfernt einen Benutzer aus der Anwendung
def delete_person(userid: int):
    print(type(userid))
    if not userid:
        return Response.wrong_format({'updated': False, 'message':'userid missing'})
    
    try:
        person = session.query(Person).filter_by(id=userid).first()
    except:
        return Response.database_error()
    
    if not person:
        return Response.ressource_not_found({"message": "userid not found!"})
    session.delete(person)
    try:
        session.commit()
    except:
        Response.database_error()
    return Response.ok({"userid":userid, "message":"deleted"})
    
# ### generate_password() - same as resetPassword()
# Generiert ein Passwort für einen Benutzer
# Idee: 
#   Link mit einem geheimniss an user, user clickt, 
#   wenn pw = "", neues generieren und zurückgeben
def generate_password(data: dict):
    if not 'userid' in data:
        return Response.wrong_format({'updated': False, 'message':'userid missing'})
    
    person = session.query(Person).filter_by(id=data["userid"]).first()
    password = ''.join(
        [choice('abcdefghijklmnopqrstuvwxyz0123456789-') for i in range(15)])
    person.password = argon2.hash(password)
    session.commit()
    return '{ "new_password" : "{}"}'.format(password)
    

# ### check_in_for_election_round(ElectionRound)
# Anwesenheit für einen Wahlgang bestätigen
def check_in(userid: int):
    if not userid:
        return Response.wrong_format({'updated': False, 'message':'userid missing'})
    
    person = session.query(Person).filter(Person.id == userid).first()
    person.is_present = True
    session.add(person)
    try:
        session.commit()
    except:
        Response.database_error()
    return Response.ok({"userid":userid, "message":"checked in"})
    
# ### check_out_from_election_round(ElectionRound)
# Sich von einem Wahlgang abmelden
def check_out(userid: int):
    if not userid:
        return Response.wrong_format({'updated': False, 'message':'userid missing'})
    
    person = session.query(Person).filter(Person.id == userid).first()
    person.is_present = False
    try:
         session.commit()
    except:
        Response.database_error()
    return Response.ok({"userid":userid, "message":"checked out"})
    
