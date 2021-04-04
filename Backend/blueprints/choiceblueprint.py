from flask import Blueprint,request
from api import choicesapi

choice_Blueprint = Blueprint('choice_Blueprint', __name__)


#DELETE: { "id": <number> }
#RETURNS: { "id":<number>, "deleted":<boolean> }
@choice_Blueprint.route('/api/choice/<id>', methods=['DELETE'])
def delete_choice(id):
    return choicesapi.delete_choice(id)

#POST: { "description": <string>, "election_round_id":<number>, "picture?":<base64string> };
#RETURNS: { "id":<number>, "updated":<boolean>, "message?":<error message> }
@choice_Blueprint.route('/api/choice/create', methods=['POST'])
def create_choice():
    return choicesapi.create_choice(request.json)

#URL: <number>; POST: { "choiceid": <number>, "picture":<base64string> };
#RETURNS: { "id":<number>, "description?":<string>, "message?":<error message> }
@choice_Blueprint.route('/api/choice/updatePicture/<choiceid>', methods=['POST'])
def updatePicture(choiceid):
    return choicesapi.updatePicture(choiceid, request.json)

#URL: <number>; POST: { "votes": <number> }
#RETURNS: { "id":<number>, "success":<Boolean>, "message?":<error message> }
@choice_Blueprint.route('/api/choice/vote/<choiceid>', methods=['POST'])
def update_votes(choiceid):
    return choicesapi.update_votes(choiceid, request.json)
