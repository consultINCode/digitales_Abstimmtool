from Backend.models import Choice, session
import base64
import json


def readChoices(electionid):
    choices = session.query(Choice).all()
    jsonO = json.dumps(choices)
    return jsonO


def createChoice(data):
    return 'test'



def deleteChoice(choiceid):
    choice = session.query(Choice).get(choiceid)
    if choice:
        session.delete(choice)
        session.commit()
        return 'Auswahl {} gelöscht'.format(choiceid)
    else:
        return 'Auswahl {} nicht gefunden'.format(choiceid)
