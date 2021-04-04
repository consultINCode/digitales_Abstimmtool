import logging

import api.choicesapi
import api.personapi
import api.voteapi
import api.electionroundsapi
import api.csvapi
# TODO(Why is this called choiceproxyapi and no <name>api.py?)
import api.choiceproxyapi
import login.auth
from flask import Flask, request
# testing endpoint decorators endpoint sessions
from flask import session as fsession
from  blueprints.personblueprint import person_Blueprint
from  blueprints.choiceblueprint import choice_Blueprint
from  blueprints.electionblueprint import election_Blueprint
from blueprints.choiceproxyblueprint import choiceproxy_Blueprint
from blueprints.voteblueprint import vote_Blueprint

#Decorators import
from login.auth import logged_in,has_role,is_present
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


from flask import abort
import datetime
''' 
TODO List:
- return json richtig parsen fuer checkin und checkout
'''

app = Flask(__name__)
# Secret for encrypting the sessions
app.secret_key = config[Session][APP_SECRET]
# Init logging
logging.basicConfig(filename='example.log', level=logging.DEBUG)


app.register_blueprint(person_Blueprint)
app.register_blueprint(choice_Blueprint)
app.register_blueprint(election_Blueprint)
app.register_blueprint(choiceproxy_Blueprint)
app.register_blueprint(vote_Blueprint)


@app.route('/sessions', methods=['GET'])
@logged_in
@has_role("0")
@is_present
def sessions():
    print(str(fsession))
    return "fsession"

# Logout method
@app.route('/logout', methods=['GET'])
def logout_user():
    return login.auth.logout(request)

@app.route('/login', methods=['POST'])
def login_user():
    return login.auth.login(request)
#POST: file
#RETURNS: { "message":<string> }
@app.route('/api/csv', methods =['POST'])
def upload_csv():       
    return api.csvapi.upload_csv(request.files['file'])

#Create Adminaccount on Startup
# api.csvapi.createadmin()