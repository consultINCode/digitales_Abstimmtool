from flask import Blueprint,request
from api import electionroundsapi
from api import choicesapi

election_Blueprint = Blueprint('election_Blueprint', __name__)


#GET: electionid: <number>
#RETURNS: { [{ "id":<number>, "picture":<base64String>, "description":<string>, "counter":<number> }] }
@election_Blueprint.route('/api/election/<electionid>', methods=['GET'])
def read_choices(electionid):
    return choicesapi.read_choices(electionid)

#POST: { "title":<string>, "max_choices_per_person":<number> } 
#RETURNS: statuscode: True = 200, False = 500
@election_Blueprint.route('/api/election/create', methods =['POST'])
def create_election_round():
    return electionroundsapi.create_election_round(request.json)

#GET  
#RETURNS: { "id":<number>, "title":<string>, "running":<string>, "max_choices_per_person":<number> }
@election_Blueprint.route('/api/election/getAll', methods =['GET'])
def get_election_rounds():
    return electionroundsapi.get_all_election_rounds()

#GET  
#RETURNS: { "id":<number>, "title":<string>, "running":<string>, "max_choices_per_person":<number> }
@election_Blueprint.route('/api/election/getAllOpenElections', methods =['GET'])
def get_all_open_elections():
    return electionroundsapi.get_all_open_elections()

#GET: electionroundid:<number>
#RETURNS: statuscode: True = 200, False = 500
@election_Blueprint.route('/api/election/close/<electionroundid>', methods =['GET'])
def close_open_election_round(electionroundid):
    return electionroundsapi.close_open_election_round(electionroundid)

#POST: { "choiceid":<number> , "electionroundid" : <number> }
#RETURNS: statuscode: True = 200, False = 500
@election_Blueprint.route('/api/election/addChoiceToElectionRound', methods =['POST'])
def add_choice_to_election_round():
    return electionroundsapi.add_choice_to_election_round(request.json)

#GET electionroundid=<number>
@election_Blueprint.route('/api/election/getResult/<electionroundid>', methods =['GET'])
def get_result_of_election_round(electionroundid):
    return electionroundsapi.get_result_of_election_round(electionroundid)
