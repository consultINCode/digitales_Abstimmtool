from flask import Blueprint,request
from api import voteapi

vote_Blueprint = Blueprint('vote_Blueprint', __name__)


#GET: electionroundid=<number>
#TODO Test Method!
#RETURNS: { "id":<number>, "name":<string> }
@vote_Blueprint.route('/api/election/getAllPersonsWhoVoted/<electionroundid>', methods =['GET'])
def get_all_persons_who_voted(electionroundid):
    return voteapi.get_all_persons_who_voted(electionroundid)

#GET: electionroundid=<number>
#TODO Test Method!
#RETURNS: { "id":<number>, "name":<string> }
@vote_Blueprint.route('/api/vote/getAllPersonsWhoHaveNotVoted/<electionroundid>', methods =['GET'])
def get_all_persons_who_have_not_voted(electionroundid):
    return voteapi.get_all_persons_who_have_not_voted(electionroundid)

#POST: { "elec_round_id":<number>, "person_id":<number> }
#RETURNS: { "Result?":<string>, "Error?":<string> }
@vote_Blueprint.route('/api/vote/setVote', methods =['POST'])
def set_vote():       
    return voteapi.set_vote(request.json)

#POST: { "election_round_id":<number>, "person_id":<number> , "choice_id": <number>}
#RETURNS: { "Result?":<string>, "Error?":<string> }
@vote_Blueprint.route('/api/vote/place_vote', methods =['POST'])
def place_vote():       
    return voteapi.place_vote(request.json)
