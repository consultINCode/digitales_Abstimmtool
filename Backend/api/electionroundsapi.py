# pylint: disable=maybe-no-member

import json
import logging
import sys
import os

from models import ElectionRound, session, Choice
from random import choice
import api.response_helper as Response

# TODO(What is this and why is it here??)
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


#Helper
def model_as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

# Election Rounds

def create_election_round(data: dict): 
    '''Creates an election round'''
    if not 'title' in data or not data['title']:
        return Response.wrong_format({"message": "Title is missing"})
    if not 'max_choices' in data:
        return Response.wrong_format({"message": "max_choices is missing"})
    if not type(data['max_choices']) == int:
        return Response.wrong_format({'message' : 'max_choices: not a number'})
    
    elec_round = ElectionRound()
    elec_round.title = data['title']
    elec_round.running = 'not_started'
    elec_round.max_choices_per_person = data['max_choices']
    session.add(elec_round)
    try:
         session.commit()
    except:
        return Response.database_error()
    return Response.ok(model_as_dict(elec_round))

def get_all_election_rounds():
    '''Returns all election rounds.'''
    try:
        elec_round_list = session.query(ElectionRound).all()
        session.commit()
    except:
        return Response.database_error()
    response = []
    for round in elec_round_list:
        response.append(model_as_dict(round))
    
    return Response.ok(json.dumps(response))

def get_all_open_elections() :
    '''Returns all active elections'''
    try:
        elec_round_list = session.query(ElectionRound).filter(
            ElectionRound.running == "running").all()
        session.commit()
    except:
        Response.database_error()
    response = []
    for round in elec_round_list:
        response.append(model_as_dict(round))
    
    return Response.ok(json.dumps(response))
 
def close_open_election_round(electionroundid: int):
    '''Closes an election round.'''
    
    try:
        electionround = session.query(ElectionRound).filter(
            ElectionRound.id == electionroundid).first()
    except:
        return Response.database_error()
    if electionround.running != "finished":
        electionround.running = "finished"
    try:
        session.commit()
    except:
        return Response.database_error()
    return Response.ok(model_as_dict(electionround))
 
def add_choice_to_election_round(data: dict):
    '''Adds an choice to an election round.'''
    if not 'choiceid' in data:
        return Response.wrong_format({'message':'choiceid missing'})
    if not type(data['choiceid']) == int:
        return Response.wrong_format({'message' : 'choiceid: not a number'})
    
    if not 'electionroundid' in data:
        return Response.wrong_format({'message':'electionroundid missing'})
    if not type(data['electionroundid']) == int:
        return Response.wrong_format({'message' : 'electionroundid: not a number'})

    try:
        choice = session.query(Choice).filter(
            Choice.id == data['choiceid']).first()
        electionround = session.query(ElectionRound).filter(
            ElectionRound.id == data['electionroundid']).first()
        choice.election_round = electionround
        session.commit()
    except:
        return Response.database_error()
    return Response.ok({'message':'added choiceid {} to electionroundid {}'.format(data['choiceid'], data['electionroundid'])})
 
def get_result_of_election_round(electionroundid: int):
    '''Returns the result of an election round.'''
    try:
        electionround = session.query(ElectionRound).filter(
            ElectionRound.id == electionroundid).first()
        choices_list = session.query(Choice).filter(
            Choice.election_round_id == electionround.id).all()
    except:
        return Response.database_error()
    
    result_choices = []
    for choice in choices_list:
        tmp = {}
        tmp['id'] = choice.id
        tmp['description'] = choice.description
        tmp['picture'] = choice.picture
        tmp['counter'] = choice.counter
        result_choices.append(tmp)
    try:
        session.commit()
    except:
        return Response.database_error()
    result = {}
    result["electionroundid"] = electionroundid
    result['choices']=result_choices
    return Response.ok(json.dumps(result))
    


