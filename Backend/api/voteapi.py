# pylint: disable=maybe-no-member

import base64
import json

from models import session, ElectionRound, Person, Choice
import api.response_helper as Response

#Helper
def model_as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

def _get_electionround_by_id(elec_round_id: int) -> ElectionRound:
    '''get election round by id and handle errors'''
    # Elec_round_id should be int
    try:
        elec_round_id = int(elec_round_id)
    except ValueError:
        return Response.wrong_format({"message":"elec_round_id has to be an int (base 10)."})

    # Get ElectionRound object from the DB.
    try:
        elec_round = session.query(ElectionRound).filter_by(
                id=elec_round_id
            ).first()
        session.commit()
    except:
        return Response.database_error()
    # Handle invalid election round
    if elec_round is None:
        return Response.ressource_not_found({"message":"No electionround for this id."})
    return elec_round

def get_person_by_id(personid :int) -> Person:
    try:
        person = session.query(Person).filter_by(
                id=personid
            ).first()
        session.commit()
    except:
        return Response.database_error()
    if person is None:
        return Response.ressource_not_found({ "message" : "No persion for this id."})
    return person


def place_vote(data:dict):
    if not 'choice_id' in data:
        return Response.wrong_format({'message': 'choiceid is required for voting'})
    if not 'election_round_id' in data:
         return Response.wrong_format({'message': 'election_round_id required for voting'})
    if not 'person_id' in data: 
        return Response.wrong_format({'message': 'person_id required for voting'})
    try:
        election_round_id = int(data['election_round_id'])
        person_id = int(data['person_id'])
        choice_id = int(data['choice_id'])
    except:
        return Response.wrong_format({"message":"ids have to be an int base 10"})
    elec_round = _get_electionround_by_id(election_round_id)
    if not elec_round:
        return Response.ressource_not_found({"message":"No electionround for this id."})
    person = get_person_by_id(person_id)
    if  person in elec_round.persons_voted:
        return Response.server_error({"message":"Person already voted"})
    try:
        choice = session.query(Choice).filter_by(id = choice_id).first()
        session.commit()
        if choice is None:
            return Response.ressource_not_found({ "message" : "No Choice with this id."})
    except:
        print("no choice")
        return Response.database_error()
    
    if choice not in elec_round.choices:
        return Response.server_error({"message":"Electionround has no Choice with that ID"})
    try:
        choice.counter = choice.counter + 1
        session.commit()
    except:
        return Response.database_error()
    try:
        elec_round.persons_voted.append(person)
        session.commit()
    except:
        return Response.database_error()

    return Response.ok(model_as_dict(choice))
    

    

def set_vote(data: dict):
    '''Add a person to the as has voted to the election_round'''
    if not 'elec_round_id' in data:
        return Response.wrong_format({'message': 'elec_round_id required'})
    if not 'person_id' in data:
        return Response.wrong_format({'message': 'person_id required'})

    try:
        elec_round_id = int(data['elec_round_id'])
        person_id = int(data['person_id'])
    except ValueError:
        return Response.wrong_format({ "message" : "ids have to be an int (base 10)."})

    # Get election_round
    try:
        elec_round = _get_electionround_by_id(elec_round_id)
        if not elec_round:
            return Response.ressource_not_found({"message":"No electionround for this id."})
    except:
        return Response.database_error()

    # Get person
    try:
        person = session.query(Person).filter_by(
                id=person_id
            ).first()
        session.commit()
        if person is None:
            return Response.ressource_not_found({ "message" : "No persion for this id."})

        # Add person to election_round
        elec_round.persons_voted.append(person)
        session.commit()

    except:
        return Response.database_error()
    return Response.ok({"message" : "OK"})

def get_all_persons_who_voted(elec_round_id: int):
    '''Return all persons as dict who have already participated in
    an election round.'''
    
    try:
        elec_round = _get_electionround_by_id(elec_round_id)
        if not elec_round:
            return Response.ressource_not_found({ "message" : "No election round for this id."})
    except:
        return Response.database_error()

    # Build and return dict
    ret = []
    for person in elec_round.persons_voted:
        ret.append(
            {
                "id" : person.id,
                "name" : person.name
            }
        )
    return Response.ok(json.dumps(ret))

def get_all_persons_who_have_not_voted(elec_round_id: int) -> dict:
    '''Get all persons who have not voted
    
    Warning: This is only accurate at the time of the election round, since 
    people can leave (altering the is_present) after the election round.
    '''
    try:
        elec_round = _get_electionround_by_id(elec_round_id)
        if not elec_round:
            return Response.ressource_not_found({ "message" : "No election round for this id."})
    except:
        return Response.database_error()
    persons_voted = elec_round.persons_voted

    # Get present people
    try:
        persons_present = session.query(Person).filter(
            Person.is_present == True).all()
        session.commit()
    except:
        return Response.database_error()
    # Get all persons who didn't vote but are present
    persons_not_voted = []
    for person in persons_present:
        if person not in persons_voted:
            persons_not_voted.append(person)

    # Create response
    ret = []
    for person in persons_not_voted:
        ret.append(
            {
                "id" : person.id,
                "name" : person.name
            }
        )
    return Response.ok(json.dumps(ret))
