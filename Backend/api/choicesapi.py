from models import Choice, session
import base64
import json


def readChoices(electionid):
    choices = session.query(Choice).filter_by(election_round_id=electionid)
    liste = []
    for choice in choices:
        liste.append({'id': choice.id, 'picture': choice.picture, 'description': choice.description, 'counter': choice.counter})
    return json.dumps(liste)


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

def updateVotes(choiceId, votes):
    choice = session.query(Choice).get(choiceId)
    if choice:
        choice.counter += votes
        session.commit()
        return json.dumps({'id':choiceId, 'votes': choice.counter})
    else:
        return json.dumps({'id':choiceId, 'votes': -1})
