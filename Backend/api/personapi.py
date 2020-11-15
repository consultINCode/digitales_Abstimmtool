import json
import logging
import sys
import os
from passlib.hash import argon2
from random import choice

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
def model_as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

#  get_all_persons()
# Gibt alle Benutzer zurück die in der Anwendung hinterlegt sind.
def get_all_persons():
    persons = session.query(Person).all()
    
    print(persons)
    response = [] 
    for person in persons:
        response.append(model_as_dict(person))

    json_response = json.dumps(response)
    print(json_response)
    session.commit()
    return json_response
    


# get_all_persons_checked_in()
# Gibt alle als anwesend makierten Benutzer zurück.
def get_all_persons_checked_in():
    persons = session.query(Person).filter(Person.is_present == True).all()
    session.commit()
    print(persons)
    response = [] 
    for person in persons:
        response.append(model_as_dict(person))

    json_response = json.dumps(response)
    print(json_response)
    return json_response

### get_all_persons_checked_out()
# Gibt alle als abwesend makierten Benutzer zurück.
def get_all_persons_checked_out():
    persons = session.query(Person).filter(Person.is_present==False).all()
    session.commit()
    response = []
    for person in persons:
        response.append(model_as_dict(person))
    
    return json.dumps(response)

# ### approve_minimal_voters()
# Überprüft ob Mindesanzahl an Wähler für eine MV vorhanden sind
def approve_minimal_voters():
    # TODO(Clarify conditions 0.5)
    num_checkedin_persons = len(get_all_persons_checked_in())
    num_all_persons = len(get_all_persons())
    if num_all_persons / num_checkedin_persons >= 0.5:
        return True
    else:
        return False

# ### create_person(Person)
# Bekommt als Parameter mehrer Werte um eine Person anzulegen.
def create_person(data: dict):
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
        return False
    return True
    

# ### delete_person(Person)
# Entfernt einen Benutzer aus der Anwendung
def delete_person(data: dict) -> bool:
    person = session.query(Person).filter_by(id=data["userid"]).first()
    session.delete(person)
    try:
         session.commit()
    except:
        return False
    return True
    
# ### generate_password() - same as resetPassword()
# Generiert ein Passwort für einen Benutzer
# Idee: 
#   Link mit einem geheimniss an user, user clickt, 
#   wenn pw = "", neues generieren und zurückgeben
def generate_password(data: dict) -> str:
    person = session.query(Person).filter_by(id=data["userid"]).first()
    password = ''.join(
        [choice('abcdefghijklmnopqrstuvwxyz0123456789-') for i in range(15)])
    user.password = argon2.hash(password)
    session.commit()
    return '{ "new_password" : "{}"}'.format(password)
    

# ### check_in_for_election_round(ElectionRound)
# Anwesenheit für einen Wahlgang bestätigen
def check_in_for_election_round(data: dict) -> bool:
    person = session.query(Person).filter(Person.id == data['userid']).first()
    person.is_present = True
    session.add(person)
    try:
         session.commit()
    except:
        return False
    return True
    
# ### check_out_from_election_round(ElectionRound)
# Sich von einem Wahlgang abmelden
def check_out_from_election_round(data: dict) -> bool:
    person = session.query(Person).filter(Person.id == data['userid']).first()
    person.is_present = False
    try:
         session.commit()
    except:
        return False
    return True
    
