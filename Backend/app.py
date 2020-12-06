import logging

import api.choicesapi
import api.personapi
import api.voteapi
import api.electionroundsapi
import api.csvapi
# TODO(Why is this called choiceproxyapi and no <name>api.py?)
import api.choiceproxyapi


from models import Person, ElectionRound, Choice, session
from flask import Flask, request, render_template

''' 
TODO List:
- Validierung in API file auslagern
- Statuscode ins API file
- return json richtig parsen fuer checkin und checkout
- readallChoices get elec info AND choices
'''

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
@app.route('/api/persons/create', methods =['POST'])
def create_person():
    return api.personapi.create_person(request.json)
     
#DELETE userid:<number>
#RETURNS: statuscode: True = 200, False = 500
@app.route('/api/persons/<userid>', methods =['DELETE'])
def delete_person(userid):
    return api.personapi.delete_person(userid)


# TODO(Test)
@app.route('/api/persons/approveMinimalVoters', methods =['GET'])
def approve_minimal_voters():
    return api.personapi.approve_minimal_voters()

#GET userid:<number>
#RETURNS: statuscode: True = 200, False = 500
@app.route('/api/persons/checkIn/<userid>', methods =['GET'])
def checkInForElectionRound(userid):
    return api.personapi.check_in(userid)

#GET userid:<number>
#RETURNS: statuscode: True = 200, False = 500
@app.route('/api/persons/checkOut/<userid>', methods =['GET'])
def check_out_from_election_round(userid):
    return api.personapi.check_out(userid)

#DELETE: { "id": <number> }
#RETURNS: { "id":<number>, "deleted":<boolean> }
@app.route('/api/choice/<id>', methods=['DELETE'])
def delete_choice(id):
    return api.choicesapi.delete_choice(id)

#POST: { "description": <string>, "electionid":<number>, "picture?":<base64string> };
#RETURNS: { "id":<number>, "updated":<boolean>, "message?":<error message> }
@app.route('/api/choice/create', methods=['POST'])
def create_choice():
    return api.choicesapi.create_choice(request.json)

#URL: <number>; POST: { "choiceid": <number>, "picture":<base64string> };
#RETURNS: { "id":<number>, "description?":<string>, "message?":<error message> }
@app.route('/api/choice/updatePicture/<choiceid>', methods=['POST'])
def updatePicture(choiceid):
    return api.choicesapi.updatePicture(choiceid, request.json)

#URL: <number>; POST: { "votes": <number> }
#RETURNS: { "id":<number>, "sucess":<Boolean>, "message?":<error message> }
@app.route('/api/choice/vote/<choiceid>', methods=['POST'])
def update_votes(choiceid):
    return api.choicesapi.update_votes(choiceid, request.json)

#GET: electionid: <number>
#RETURNS: { [{ "id":<number>, "picture":<base64String>, "description":<string>, "counter":<number> }] }
@app.route('/api/election/<electionid>', methods=['GET'])
def read_choices(electionid):
    return api.choicesapi.read_choices(electionid)

#POST: { "title":<string>, "max_choices":<number> } 
#RETURNS: statuscode: True = 200, False = 500
@app.route('/api/election/create', methods =['POST'])
def create_election_round():
    return api.electionroundsapi.create_election_round(request.json)

#GET  
#RETURNS: { "id":<number>, "title":<string>, "running":<string>, "max_choices_per_person":<number> }
@app.route('/api/election/getAll', methods =['GET'])
def get_election_rounds():
    return api.electionroundsapi.get_all_election_rounds()

#GET  
#RETURNS: { "id":<number>, "title":<string>, "running":<string>, "max_choices_per_person":<number> }
@app.route('/api/election/getAllOpenElections', methods =['GET'])
def get_all_open_elections():
    return api.electionroundsapi.get_all_open_elections()

#GET: electionroundid:<number>
#RETURNS: statuscode: True = 200, False = 500
@app.route('/api/election/close/<electionroundid>', methods =['GET'])
def close_open_election_round(electionroundid):
    return api.electionroundsapi.close_open_election_round(electionroundid)

#POST: { "choiceid":<number> , "electionroundid" : <number> }
#RETURNS: statuscode: True = 200, False = 500
@app.route('/api/election/addChoiceToElectionRound', methods =['POST'])
def add_choice_to_election_round():
    return api.electionroundsapi.add_choice_to_election_round(request.json)

#GET electionroundid=<number>
@app.route('/api/election/getResult/<electionroundid>', methods =['GET'])
def get_result_of_election_round(electionroundid):
    return api.electionroundsapi.get_result_of_election_round(electionroundid)

#POST: { "receiverid":<number>, "senderid":<number> }  
#RETURNS: statuscode: True = 200, False = 500
@app.route('/api/choiceproxy/create', methods =['POST'])
def create_choice_proxy():
    return api.choiceproxyapi.create_choice_proxy(request.json)

#DELETE: <number>  
#RETURNS: statuscode: True = 200, False = 500
@app.route('/api/choiceproxy/<senderid>', methods=['DELETE'])
def delete_choice_proxy(senderid):
    return api.choiceproxyapi.delete_choice_proxy(senderid)

#POST: { "receiverid":<number>, "senderid":<number> }  
#RETURNS: statuscode: True = 200, False = 500
@app.route('/api/choiceproxy/update', methods =['POST'])
def update_choice_proxy():
    return api.choiceproxyapi.update_choice_proxy(request.json)

#GET: electionroundid=<number>
#TODO Test Method!
#RETURNS: { "id":<number>, "name":<string> }
@app.route('/api/election/getAllPersonsWhoVoted/<electionroundid>', methods =['GET'])
def get_all_persons_who_voted(electionroundid):
    return api.voteapi.get_all_persons_who_voted(electionroundid)

#GET: electionroundid=<number>
#TODO Test Method!
#RETURNS: { "id":<number>, "name":<string> }
@app.route('/api/vote/getAllPersonsWhoHaveNotVoted/<electionroundid>', methods =['GET'])
def get_all_persons_who_have_not_voted(electionroundid):
    return api.voteapi.get_all_persons_who_have_not_voted(electionroundid)

#POST: { "elec_round_id":<number>, "person_id":<number> }
#RETURNS: { "Result?":<string>, "Error?":<string> }
@app.route('/api/vote/setVote', methods =['POST'])
def set_vote():       
    return api.voteapi.set_vote(request.json)


#POST: file
#RETURNS: { "message":<string> }
@app.route('/api/csv', methods =['POST'])
def upload_csv():       
    return api.csvapi.upload_csv(request.files['file'])

'''@app.route("/")
def hello():
    return api.helpers.ok({"message": "test"})
'''
if __name__ == "__main__":
    app.run()

