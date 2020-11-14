from flask import Flask, Response, request, render_template
import logging
import api.personapi
from models import Person, ElectionRound, Choice, session

app = Flask(__name__)

from api.choicesapi import createChoice, deleteChoice, readChoices, updateVotes

app = Flask(__name__)

# Init logging
logging.basicConfig(filename='example.log', level=logging.DEBUG)

# Some example log lines
logging.info("test")
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')


# this function should be defined in your /api/modelname
def yourfunction(data="test"):
    print(data)


# Blueprint for Flask Routes
# copy and adapt :)
@app.route('/api/modelname/function', methods=['GET', 'POST', 'DELETE', 'PUT'])
def functionname():
    if request.method == 'POST':
        data = request.json
        yourfunction(data)
        return Response(status=200)
    elif request.method == 'GET':
        return yourfunction()
    elif request.method == 'PUT':
        data = request.json
        yourfunction(data)
        return Response(status=200)
    elif request.method == 'DELETE':
        data = request.json
        yourfunction(data)
        return Response(status=200)

@app.route('/api/persons/getAllPersons', methods =['GET'])
def getallpersons():
    return api.personapi.getAllPersons()

@app.route('/api/persons/getAllPersonsCheckedIn', methods =['GET'])
def getAllPersonsCheckedIn():
    return api.personapi.getAllPersonsCheckedIn()

@app.route('/api/persons/getAllPersonsCheckedOut', methods =['GET'])
def getAllPersonsCheckedOut():
    return api.personapi.getAllPersonsCheckedOut()
     
@app.route('/api/persons/createPerson', methods =['POST'])
def createPerson():
    data = request.json
    if api.personapi.createPerson(data):
        return Response(status=200)
    return Response(status= 500)

@app.route('/api/persons/deletePerson', methods =['DELETE'])
def deletePerson():
    data = request.json
    if api.personapi.deletePerson(data):
        return Response(status=200)
    return Response(status= 500)


# TODO(Test)
@app.route('/api/persons/approveMinimalVoters', methods =['GET', 'POST'])
def approveMinimalVoters():
    if request.method == 'GET':
        if api.personapi.approveMinimalVoters():
            return True
        return False
    else:
        return Response(status=405)

@app.route('/api/persons/checkInForElectionRound', methods =['POST'])
def checkInForElectionRound():
    data = request.json
    if api.personapi.checkInForElectionRound(data):
        return Response(status=200)
    return Response(status= 500)

@app.route('/api/persons/checkOutFromElectionRound', methods =['POST'])
def checkOutFromElectionRound():
    data = request.json
    if api.personapi.checkOutFromElectionRound(data):
        return Response(status=200)
    return Response(status= 500)


@app.route('/')
def answer():
    return "HelloWOrd"

if __name__ == "__main__":
    app.run()


#DELETE: { "id": <number> }
#RETURNS: { "id":<number>, "deleted":<boolean> }
@app.route('/api/choice/<id>', methods=['DELETE'])
def delete_choice(id):
    return deleteChoice(id)

#POST: { "description": <string>, "electionId":<number> }; TODO: picture!
#RETURNS: { "id":<number>, "description?":<string>, "message?":<error message> }
@app.route('/api/choice/', methods=['POST'])
def create_choice():
    return createChoice(request.json)

#URL: <number>
#RETURNS: { [{ "id":<number>, "picture":<base64String>, "description":<string>, "counter":<number> }] }
@app.route('/api/election/<electionid>', methods=['GET'])
def read_choices(electionid):
    return readChoices(electionid)

#URL: <number>; POST: { "votes": <number> }
#RETURNS: { "id":<number>, "votes":<number>, "message?":<error message> }
@app.route('/api/choice/vote/<choiceid>', methods=['POST'])
def updateVotes_choices(choiceid):
    return updateVotes(choiceid, request.json)

#html template for test purpose
@app.route('/test')
def testpage():
   return render_template('testpage.html')
