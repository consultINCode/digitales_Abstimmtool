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
logging.info("test")
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

# Helpers
def model_as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

#  getAllPersons()
# Gibt alle Benutzer zurück die in der Anwendung hinterlegt sind.
def getAllPersons():
    persons = session.query(Person).all()
    session.commit()
    print(persons)
    response = [] 
    for person in persons:
        response.append(model_as_dict(person))

    json_response = json.dumps(response)
    print(json_response)
    return json_response
    


# getAllPersonsCheckedIn()
# Gibt alle als anwesend makierten Benutzer zurück.


def getAllPersonsCheckedIn():
    persons = session.query(Person).filter(Person.is_present == True).all()
    session.commit()
    print(persons)
    response = [] 
    for person in persons:
        response.append(model_as_dict(person))

    json_response = json.dumps(response)
    print(json_response)
    return json_response

### getAllPersonsCheckedOut()
# Gibt alle als abwesend makierten Benutzer zurück.
def getAllPersonsCheckedOut():
    persons = session.query(Person).filter(Person.is_present==False).all()
    session.commit()
    response = []
    for person in persons:
        response.append(model_as_dict(person))
    
    return json.dumps(response)

# ### approveMinimalVoters()
# Überprüft ob Mindesanzahl an Wähler für eine MV vorhanden sind
def approveMinimalVoters():
    # TODO(Clarify conditions 0.5)
    num_checkedin_persons = len(getAllPersonsCheckedIn())
    num_all_persons = len(getAllPersons())
    if num_all_persons / num_checkedin_persons >= 0.5:
        return True
    else:
        return False

# ### createPerson(Person)
# Bekommt als Parameter mehrer Werte um eine Person anzulegen.
def createPerson(data):
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
    

# ### deletePerson(Person)
# Entfernt einen Benutzer aus der Anwendung
def deletePerson(data):
    person = session.query(Person).filter_by(id=data["userid"]).first()
    session.delete(person)
    try:
         session.commit()
    except:
        return False
    return True
    
# ### generatePassword() - same as resetPassword()
# Generiert ein Passwort für einen Benutzer
# Idee: Link mit einem geheimniss an user, user clickt, wenn pw = "", neues generieren und zurückgeben
def generatePassword(data):
    person = session.query(Person).filter_by(id=data["userid"]).first()
    password = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789-') for i in range(15)])
    user.password = argon2.hash(password)
    session.commit()
    return '{ "new_password" : "{}"}'.format(password)
    

# ### checkInForElectionRound(ElectionRound)
# Anwesenheit für einen Wahlgang bestätigen
def checkInForElectionRound(data):
    person = session.query(Person).filter(Person.id == data['userid']).first()
    person.is_present = True
    session.add(person)
    try:
         session.commit()
    except:
        return False
    return True
    
# ### checkOutFromElectionRound(ElectionRound)
# Sich von einem Wahlgang abmelden
def checkOutFromElectionRound(data):
    person = session.query(Person).filter(Person.id == data['userid']).first()
    person.is_present = False
    try:
         session.commit()
    except:
        return False
    return True
    
