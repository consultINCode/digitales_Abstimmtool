import json
import logging
import sys
import os

from models import ElectionRound, session, Choice
from random import choice

# TODO(What is this and why is it here??)
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


#Helper
def model_as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

# Election Rounds

def create_election_round(data: dict) -> bool: 
    '''Creates an election round'''
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

def get_all_election_rounds() -> str:
    '''Returns all election rounds.'''
    elec_round_list = session.query(ElectionRound).all()
    session.commit()
    response = []
    for round in elec_round_list:
        response.append(model_as_dict(round))
    
    return json.dumps(response)

def get_all_open_elections() -> str:
    '''Returns all active elections'''
    elec_round_list = session.query(ElectionRound).filter(ElectionRound.running == "running").all()
    session.commit()
    response = []
    for round in elec_round_list:
        response.append(model_as_dict(round))
    
    return json.dumps(response)
 
def close_open_election_round(data: dict) -> bool:
    '''Closes an election round.'''
    electionround = session.query(ElectionRound).filter(ElectionRound.id == data['electionroundid']).first()
    if electionround.running != "finished":
        electionround.running = "finished"
    try:
         session.commit()
    except:
        return False
    return True
 
def add_choice_to_election_round(data: dict) -> bool:
    '''Adds an choice to an election round.'''
    choice = session.query(Choice).filter(Choice.id == data['choiceid']).first()
    electionround = session.query(ElectionRound).filter(ElectionRound.id == data['electionroundid']).first()
    choice.election_round = electionround
    try:
         session.commit()
    except:
        return False
    return True
 
def get_result_of_election_round(data: dict) -> str:
    '''Returns the result of an election round.'''
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
    


