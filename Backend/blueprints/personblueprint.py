from flask import Blueprint,request
from api import personapi

person_Blueprint = Blueprint('person_Blueprint', __name__)



#POST { "name":<string> }
#RETURNS: statuscode: True = 200, False = 500
@person_Blueprint.route('/api/persons/create', methods =['POST'])
def create_person():
    return personapi.create_person(request.json)


 #GET
#RETURNS: { [{ "id":<number>, "name":<string>, "password":<string>, "is_present":<boolean>, "role":<number as string> }] }
@person_Blueprint.route('/api/persons/getAllPersons', methods =['GET'])
def get_all_persons():
    return personapi.get_all_persons()

#GET
#RETURNS: { [{ "id":<number>, "name":<string>, "password":<string>, "is_present":<boolean>, "role":<number as string> }] }
@person_Blueprint.route('/api/persons/getAllPersonsCheckedIn', methods =['GET'])
def get_all_persons_checked_in():
    return personapi.get_all_persons_checked_in()

#GET
#RETURNS: { [{ "id":<number>, "name":<string>, "password":<string>, "is_present":<boolean>, "role":<number as string> }] }
@person_Blueprint.route('/api/persons/getAllPersonsCheckedOut', methods =['GET'])
def get_all_persons_checked_out():
    return personapi.get_all_persons_checked_out()
     
   
#DELETE userid:<number>
#RETURNS: statuscode: True = 200, False = 500
@person_Blueprint.route('/api/persons/<userid>', methods =['DELETE'])
def delete_person(userid):
    return personapi.delete_person(userid)


# TODO(Test)
@person_Blueprint.route('/api/persons/approveMinimalVoters', methods =['GET'])
def approve_minimal_voters():
    return personapi.approve_minimal_voters()

#GET userid:<number>
#RETURNS: statuscode: True = 200, False = 500
@person_Blueprint.route('/api/persons/checkIn/<userid>', methods =['GET'])
def checkInForElectionRound(userid):
    return personapi.check_in(userid)

#GET userid:<number>
#RETURNS: statuscode: True = 200, False = 500
@person_Blueprint.route('/api/persons/checkOut/<userid>', methods =['GET'])
def check_out_from_election_round(userid):
    return personapi.check_out(userid)
