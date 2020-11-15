import logging

import api.choicesapi
import api.personapi
import api.voteapi
import api.electionroundsapi
# TODO(Why is this called hasChoice and no <name>api.py?)
import api.hasChoice

from models import Person, ElectionRound, Choice, session
from flask import Flask, Response, request, render_template

app = Flask(__name__)

# Init logging
logging.basicConfig(filename='example.log', level=logging.DEBUG)


#GET
#RETURNS: { [{ "id":<number>, "name":<string>, "password":<string>, "is_present":<boolean>, "role":<number as string> }] }
@app.route('/api/persons/getAllPersons', methods =['GET'])
def get_all_persons():
    return api.personapi.get_all_persons()

#GET
#RETURNS: { [{ "id":<number>, "name":<string>, "password":<string>, "is_present":<boolean>, "role":<number as string> }] }
@app.route('/api/persons/getAllPersonsCheckedIn', methods =['GET'])
def get_all_persons_checked_in():
    return api.personapi.get_all_persons_checked_in()

#GET
#RETURNS: { [{ "id":<number>, "name":<string>, "password":<string>, "is_present":<boolean>, "role":<number as string> }] }
@app.route('/api/persons/getAllPersonsCheckedOut', methods =['GET'])
def get_all_persons_checked_out():
    return api.personapi.get_all_persons_checked_out()
     
#POST { "name":<string> }
#RETURNS: statuscode: True = 200, False = 500
@app.route('/api/persons/createPerson', methods =['POST'])
def create_person():
    data = request.json
    if api.personapi.create_person(data):
        return Response(status=200)
    return Response(status= 500)
     
#DELETE { "userid":<number> } 
#RETURNS: statuscode: True = 200, False = 500
@app.route('/api/persons/deletePerson', methods =['DELETE'])
def delete_person():
    data = request.json
    if api.personapi.delete_person(data):
        return Response(status=200)
    return Response(status= 500)


# TODO(Test)
@app.route('/api/persons/approveMinimalVoters', methods =['GET', 'POST'])
def approve_minimal_voters():
    if request.method == 'GET':
        if api.personapi.approve_minimal_voters():
            return True
        return False
    else:
        return Response(status=405)

#POST { "userid":<number> } 
#RETURNS: statuscode: True = 200, False = 500
@app.route('/api/persons/checkInForElectionRound', methods =['POST'])
def checkInForElectionRound():
    data = request.json
    if api.personapi.check_in_for_election_round(data):
        return Response(status=200)
    return Response(status= 500)

#POST { "userid":<number> } 
#RETURNS: statuscode: True = 200, False = 500
@app.route('/api/persons/checkOutFromElectionRound', methods =['POST'])
def check_out_from_election_round():
    data = request.json
    if api.personapi.check_out_from_election_round(data):
        return Response(status=200)
    return Response(status= 500)

#DELETE: { "id": <number> }
#RETURNS: { "id":<number>, "deleted":<boolean> }
@app.route('/api/choice/<id>', methods=['DELETE'])
def delete_choice(id):
    return api.choicesapi.delete_choice(id)

#POST: { "description": <string>, "electionId":<number>, "picture?":<base64string> };
#RETURNS: { "id":<number>, "updated":<boolean>, "message?":<error message> }
@app.route('/api/choice/', methods=['POST'])
def create_choice():
    return api.choicesapi.create_choice(request.json)

#URL: <number>; POST: { "choiceid": <number>, "picture":<base64string> };
#RETURNS: { "id":<number>, "description?":<string>, "message?":<error message> }
@app.route('/api/choice/<choiceid>/updatePicture', methods=['POST'])
def setPicture(choiceid):
    return api.choicesapi.setPicture(choiceid, request.json)

#URL: <number>
#RETURNS: { [{ "id":<number>, "picture":<base64String>, "description":<string>, "counter":<number> }] }
@app.route('/api/election/<electionid>', methods=['GET'])
def read_choices(electionid):
    return api.choicesapi.read_choices(electionid)

#URL: <number>; POST: { "votes": <number> }
#RETURNS: { "id":<number>, "votes":<number>, "message?":<error message> }
@app.route('/api/choice/vote/<choiceid>', methods=['POST'])
def update_votes_choices(choiceid):
    return api.choicesapi.update_votes(choiceid, request.json)

#POST: { "title":<string>, "max_choices":<number> } 
#RETURNS: statuscode: True = 200, False = 500
@app.route('/api/electionrounds/createElectionRound', methods =['POST'])
def create_election_round():
    if request.method == 'POST':
        data = request.json
        if api.electionroundsapi.create_election_round(data):
            return Response(status=200)
        return Response(status= 500)

#GET  
#RETURNS: { "id":<number>, "title":<string>, "running":<string>, "max_choices_per_person":<number> }
@app.route('/api/electionrounds/getAllElectionRounds', methods =['GET'])
def get_election_rounds():
    if request.method == 'GET':
        return api.electionroundsapi.get_all_election_rounds()

#GET  
#RETURNS: { "id":<number>, "title":<string>, "running":<string>, "max_choices_per_person":<number> }
@app.route('/api/electionrounds/getAllOpenElections', methods =['GET'])
def get_all_open_elections():
    if request.method == 'GET':
        return api.electionroundsapi.get_all_open_elections()

#POST: { "electionroundid":<number> }  
#RETURNS: statuscode: True = 200, False = 500
@app.route('/api/electionrounds/closeOpenElectionRound', methods =['POST'])
def close_open_election_round():
    if request.method == 'POST':
        data = request.json
        if api.electionroundsapi.close_open_election_round(data):
            return Response(status=200)
        return Response(status= 500)

#POST: { "choiceid":<number> }  
#RETURNS: statuscode: True = 200, False = 500
@app.route('/api/electionrounds/addChoiceToElectionRound', methods =['POST'])
def add_choice_to_election_round():
    if request.method == 'POST':
        data = request.json
        if api.electionroundsapi.add_choice_to_election_round(data):
            return Response(status=200)
        return Response(status= 500)

#GET
# TODO(Change to get)
@app.route('/api/electionrounds/getResultOfElectionRound', methods =['POST'])
def get_result_of_election_round():
    if request.method == 'POST':
        data = request.json
        return api.electionroundsapi.get_result_of_election_round(data)

#POST: { "receiverid":<number>, "senderid":<number> }  
#RETURNS: statuscode: True = 200, False = 500
@app.route('/api/choiceproxy/createChoiceProxy', methods =['POST'])
def create_choice_proxy():
    if request.method == 'POST':
        data = request.json
        if api.hasChoice.create_choice_proxy(data):
            return Response(status=200)
        return Response(status= 500)

#DELETE: <number>  
#RETURNS: statuscode: True = 200, False = 500
@app.route('/api/choiceproxy/<senderid>', methods=['DELETE'])
def delete_choice_proxy(senderid):
    if api.hasChoice.delete_choice_proxy(senderid):
        return Response(status=200)
    return Response(status= 500)

#POST: { "receiverid":<number>, "senderid":<number> }  
#RETURNS: statuscode: True = 200, False = 500
@app.route('/api/choiceproxy/updateChoiceProxy', methods =['POST'])
def update_choice_proxy():
    if request.method == 'POST':
        data = request.json
        if api.hasChoice.update_choice_proxy(data):
            return Response(status=200)
        return Response(status= 500)

#GET: elec_round_id=<number>
#RETURNS: { "id":<number>, "name":<string> }
@app.route('/api/vote/getAllPersonsWhoVoted', methods =['GET'])
def get_all_persons_who_voted():
    elec_round_id = request.args.get('elec_round_id')
    if elec_round_id is None:
        resp = Response(status=400)
        resp.set_data("elec_round_id required.")
        return resp
    return api.voteapi.get_all_persons_who_voted(elec_round_id)

#GET: elec_round_id=<number>
#RETURNS: { "id":<number>, "name":<string> }
@app.route('/api/vote/getAllPersonsWhoHaveNotVoted', methods =['GET'])
def get_all_persons_who_have_not_voted():
    elec_round_id = request.args.get('elec_round_id')

    if elec_round_id is None:
        resp = Response(status=400)
        resp.set_data("elec_round_id required.")
        return resp

    return api.voteapi.get_all_persons_who_have_not_voted(elec_round_id)

#GET: { "elec_round_id":<number>, "person_id":<number> }
#RETURNS: { "Result?":<string>, "Error?":<string> }
@app.route('/api/vote/setVote', methods =['POST'])
def set_vote():
    data = request.json
    if data is None:
        resp = Response(status=400)
        resp.set_data("elec_round_id and person_id required.")
        return resp

    elec_round_id = data['elec_round_id']
    person_id = data['person_id']

    if (elec_round_id is None) or (person_id is None):
        resp = Response(status=400)
        resp.set_data("elec_round_id and person_id required.")
        return resp
        
    return api.voteapi.set_vote(elec_round_id, person_id)


if __name__ == "__main__":
    app.run()

