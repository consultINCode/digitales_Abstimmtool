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
    print(str(data))
    return ''


def deleteChoice(choiceid):
    choice = session.query(Choice).get(choiceid)
    if choice:
        session.delete(choice)
        session.commit()
        return 'Auswahl {} gelöscht'.format(choiceid)
    else:
        return 'Auswahl {} nicht gefunden'.format(choiceid)

def updateVotes(choiceId, votes):
    if not votes['votes'].isdigit():
        return json.dumps({'id':'error', 'votes': -1, 'message':'Not a number'})
    choice = session.query(Choice).get(choiceId)
    if choice:
        choice.counter += int(votes['votes'] or 0)
        session.commit()
        return json.dumps({'id':choiceId, 'votes': choice.counter})
    else:
        return json.dumps({'id':choiceId, 'votes': -1, 'message':'choice not found'})
