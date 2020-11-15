import base64
import json

from models import session, ElectionRound, Person


def _get_electionround_by_id(elec_round_id: int) -> ElectionRound:
    # Elec_round_id should be int
    try:
        elec_round_id = int(elec_round_id)
    except ValueError:
        raise Exception("elec_round_id has to be an int (base 10).")

    # Get ElectionRound object from the DB.
    elec_round = session.query(ElectionRound).filter_by(
            id=elec_round_id
        ).first()
    session.commit()

    # Handle invalid election round
    if elec_round is None:
        raise Exception("No electionround for this id.")
    
    return elec_round


def setVote(elec_round_id: int, person_id: int) -> dict:
    '''Person hat erfolgreich für diese Wahl abgestimmt'''
    # Get election_round
    try:
        elec_round = _get_electionround_by_id(elec_round_id)
    except Exception as e:
        return '{{ "Error" : "{}" }}'.format(str(e))

    # Get person
    try:
        elec_round_id = int(elec_round_id)
    except ValueError:
        return '{ "Error" : "person_id has to be an int (base 10)."}'

    person = session.query(Person).filter_by(
            id=person_id
        ).first()
    session.commit()

    if person is None:
        return '{ "Error" : "No persion for this id."}'

    # Add person to election_round
    elec_round.persons_voted.append(person)
    session.commit()

    return '{ "Result" : "OK" }'

def getAllPersonsWhoVoted(elec_round_id: int) -> dict:
    '''Gibt alle Personen zurück die in der Wahlrunde schon gewählt haben'''
    
    try:
        elec_round = _get_electionround_by_id(elec_round_id)
    except Exception as e:
        return '{{ "Error" : "{}" }}'.format(str(e))

    # Build and return dict
    ret = []
    for person in elec_round.persons_voted:
        ret.append(
            {
                "id" : person.id,
                "name" : person.name
            }
        )
    return json.dumps(ret)

def getAllPersonsWhoHaveNotVoted(elec_round_id: int) -> dict:
    '''Get all persons who have not voted
    
    Warning: This is only accurate at the time of the election round, since 
    people can leave (altering the is_present) after the election round.
    '''
    try:
        elec_round = _get_electionround_by_id(elec_round_id)
    except Exception as e:
        return '{{ "Error" : "{}" }}'.format(str(e))
    persons_voted = elec_round.persons_voted

    # Get present people
    persons_present = session.query(Person).filter(
        Person.is_present == True).all()
    session.commit()

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

    return json.dumps(ret)

