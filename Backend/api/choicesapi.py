# pylint: disable=maybe-no-member

import base64
import json

from models import Choice, session


def read_choices(electionid: int) -> str:
    choices = session.query(Choice).filter_by(election_round_id=electionid)
    liste = []
    for choice in choices:
        liste.append(
            {
                'id': choice.id, 
                'picture': choice.picture, 
                'description': choice.description, 
                'counter': choice.counter
            }
        )
    return json.dumps(liste)

def create_choice(data: dict) -> str:
    choice = Choice(
        description=data['description'], 
        counter=0, 
        picture=data["image"], 
        election_round_id=data['electionId']
    )
    session.add(choice)
    session.commit()
    if choice.id:
        return json.dumps({'id':choice.id, 'description': choice.description})
    return json.dumps({'id':-1, 'message': 'Failed to insert choice '})

def delete_choice(choiceid: int) -> str:
    choice = session.query(Choice).get(choiceid)
    if choice:
        session.delete(choice)
        session.commit()
        return json.dumps({'id':choiceid, 'deleted': True})
    return json.dumps({'id':choiceid, 'deleted': False})

def update_votes(choiceId: int, votes: int) -> str:
    if not votes['votes'].isdigit():
        return json.dumps(
            {
                'id' : 'error', 
                'votes' : -1, 
                'message' : 'Not a number'
            }
        )
    choice = session.query(Choice).get(choiceId)
    if choice:
        choice.counter += int(votes['votes'] or 0)
        session.commit()
        return json.dumps({'id':choiceId, 'votes': choice.counter})
    else:
        return json.dumps(
            {
                'id' : choiceId, 
                'votes' : -1, 
                'message' : 'choice not found'
            }
        )
