# pylint: disable=maybe-no-member

import json

from models import Choice, session
import api.response_helper as Response


def read_choices(electionid: int) -> str:
    try:
        choices = session.query(Choice).filter_by(election_round_id=electionid)
    except:
        Response.database_error()
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
    return Response.ok(json.dumps(liste))

def create_choice(data: dict) -> str:
    if not 'description' in data:
        return Response.wrong_format(json.dumps({'message':'description missing'}))
    if not 'election_round_id' in data:

        return Response.wrong_format(json.dumps({'message':'election_round_id missing'}))

    if 'picture' in data:
        if data['picture'].endswith('=='):
            picture = data['picture']

        elif not data['picture']:
            picture = ''
        else:
            return Response.wrong_format({"message" : "picture is not Base64"})
    else :
        picture = ''

    choice = Choice(
        description=data['description'], 
        counter=0, 
        picture=picture,
        election_round_id=data['election_round_id']
    )
    session.add(choice)
    try:
        session.commit()
    except:
        return Response.database_error()
    return Response.ok(json.dumps({'id':choice.id, 'description': choice.description}))




def delete_choice(choiceid: int) -> str:
    try:
        choice = session.query(Choice).get(choiceid)
    except:
        return Response.database_error()
    if not choice:
        return Response.ressource_not_found({'id':choiceid, 'message':'choiceid not found!'})
    session.delete(choice)
    try:
        session.commit()
    except:
        return Response.database_error()
    return Response.ok(json.dumps({'id':choiceid, 'deleted': True}))

def updatePicture(choiceid: int, data: dict) -> str:
    if not 'picture' in data:
        return Response.wrong_format({'updated': False, 'message':'picture missing'})
    if not data['picture'].endswith('=='):
        return Response.wrong_format({'updated': False, 'message':'not a base64 string'})
    try:
        choice = session.query(Choice).get(choiceid)
    except:
        return Response.database_error()
    if not choice:
        return Response.ressource_not_found({'id':choiceid, 'message':'choiceid not found!'})
    choice.picture=data['picture']
    try:
        session.commit()
    except:
        return Response.database_error()
    return Response.ok({'id':choiceid, 'updated': True})

def update_votes(choiceId: int, data: dict) -> str:
    if not 'votes' in data:
        return Response.wrong_format({'updated': False, 'message':'votes missing'})

    if not type(data['votes']) == int:
        return Response.wrong_format({'id' : 'error', 'message' : 'Not a number'})
    try:
        choice = session.query(Choice).get(choiceId)
    except:
        return Response.database_error()
    if choice:
        choice.counter += int(data['votes'] or 0)
        try:
            session.commit()
        except:
            return Response.database_error()
        return Response.ok({'id':choiceId, 'success': True})
    else:
        return Response.ressource_not_found(
            {
                'id' : choiceId,
                'message' : 'choice not found'
            }
        )
