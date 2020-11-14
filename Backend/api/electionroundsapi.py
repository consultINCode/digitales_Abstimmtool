import json
import logging
import sys
import os
from passlib.hash import argon2
from random import choice

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from models import ElectionRound,session, Choice

#Helper
def model_as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

# Election Rounds


#Erstellt eine Wahlrunde
def createElectionRound(data): 
    elec_round = ElectionRound()
    elec_round.title = data['title']
    elec_round.running = 'not_started'
    elec_round.max_choices_per_person = data['max_choices']
    session.add(elec_round)
    try:
         session.commit()
    except:
        return False
    return True


#gibt alle Wahlrunden zurück
def getAllElectionRounds():
    elec_round_list = session.query(ElectionRound).all()
    session.commit()
    response = []
    for round in elec_round_list:
        response.append(model_as_dict(round))
    
    return json.dumps(response)



#git alle Wahlrunden zurück die aktive sind
def getAllOpenElections():
    elec_round_list = session.query(ElectionRound).filter(ElectionRound.running == "running").all()
    session.commit()
    response = []
    for round in elec_round_list:
        response.append(model_as_dict(round))
    
    return json.dumps(response)
 
# Schließt eine Wahlrunde 

def closeOpenElectionRound(data):
    electionround = session.query(ElectionRound).filter(ElectionRound.id == data['electionroundid']).first()
    if electionround.running != "finished":
        electionround.running = "finished"
    try:
         session.commit()
    except:
        return False
    return True
 
#Fügt Wahlmöglichkeiten der Wahlrunde hinzu.  
def addChoiceToELectionRound(data):
    choice = session.query(Choice).filter(Choice.id == data['choiceid']).first()
    electionround = session.query(ElectionRound).filter(ElectionRound.id == data['electionroundid']).first()
    choice.election_round = electionround
    try:
         session.commit()
    except:
        return False
    return True

'''
### CheckIfElectionRoundIsOpen()
Prüft ob die Wahlrunde noch offen ist
Brauchen wir nicht, weil getAllOpenElections den gleichen sinn erfüllt
'''
 
# Gibt das Ergebnis der Wahlrunde zurück
def getResultofElectionRound(data):
    electionround = session.query(ElectionRound).filter(ElectionRound.id == data['electionroundid']).first()
    choices_list = session.query(Choice).filter(Choice.election_round_id == electionround.id).all()
    
    response = []
    for choice in choices_list:
        
        tmp = {}
        tmp['id'] = choice.id
        tmp['description'] = choice.description
        tmp['picture'] = choice.picture
        tmp['counter'] = choice.counter
        tmp['election_round_id'] = choice.election_round_id
        response.append(tmp)
    session.commit()
    return json.dumps(response)
    


