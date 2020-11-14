from flask import Flask, Response,request
import logging
import api.personapi
from models import Person, ElectionRound, Choice, session
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
@app.route('/api/modelname/function', methods=['GET', 'POST','DELETE','PUT'])
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

@app.route('/api/persons/getAllPersons', methods =['Get'])
def getallpersons():
    if request.method == 'GET':
        return api.personapi.getAllPersons()

@app.route('/api/persons/getAllPersonsCheckedIn', methods =['Get'])
def getAllPersonsCheckedIn():
    if request.method == 'GET':
        return api.personapi.getAllPersonsCheckedIn()

@app.route('/api/persons/getAllPersonsCheckedOut', methods =['Get'])
def getAllPersonsCheckedOut():
    if request.method == 'GET':
        return api.personapi.getAllPersonsCheckedOut()
     
@app.route('/api/persons/createPerson', methods =['POST'])
def createPerson():
    if request.method == 'POST':
        data = request.json
        if api.personapi.createPerson(data):
            return Response(status=200)
        return Response(status= 500)

@app.route('/api/persons/deletePerson', methods =['DELETE'])
def deletePerson():
    if request.method == 'DELETE':
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
    if request.method == 'POST':
        data = request.json
        if api.personapi.checkInForElectionRound(data):
            return Response(status=200)
        return Response(status= 500)

@app.route('/api/persons/checkOutFromElectionRound', methods =['POST'])
def checkOutFromElectionRound():
    if request.method == 'POST':
        data = request.json
        if api.personapi.checkOutFromElectionRound(data):
            return Response(status=200)
        return Response(status= 500)


@app.route('/')
def answer():
    return "HelloWOrd"

if __name__ == "__main__":
    app.run()

 