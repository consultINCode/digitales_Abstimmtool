
from flask import Blueprint,request
from api import choiceproxyapi

choiceproxy_Blueprint = Blueprint('choiceproxy_Blueprint', __name__)

#POST: { "receiverid":<number>, "senderid":<number> }  
#RETURNS: statuscode: True = 200, False = 500
@choiceproxy_Blueprint.route('/api/choiceproxy/create', methods =['POST'])
def create_choice_proxy():
    return choiceproxyapi.create_choice_proxy(request.json)

#DELETE: <number>  
#RETURNS: statuscode: True = 200, False = 500
@choiceproxy_Blueprint.route('/api/choiceproxy/<senderid>', methods=['DELETE'])
def delete_choice_proxy(senderid):
    return choiceproxyapi.delete_choice_proxy(senderid)

#POST: { "receiverid":<number>, "senderid":<number> }  
#RETURNS: statuscode: True = 200, False = 500
@choiceproxy_Blueprint.route('/api/choiceproxy/update', methods =['POST'])
def update_choice_proxy():
    return choiceproxyapi.update_choice_proxy(request.json)
