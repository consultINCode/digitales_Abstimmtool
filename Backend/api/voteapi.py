from models import session, ElectionRound
import base64
import json

def setVote(elec_round, person):
    '''Person hat erfolgreich für diese Wahl abgestimmt'''
    # TODO(Impl method)
    pass    

def getAllPersonsWhoVoted(elec_round_id: int) -> dict:
    '''Gibt alle Personen zurück die in der Wahlrunde schon gewählt haben'''
    
    # Elec_round_id should be int
    try:
        elec_round_id = int(elec_round_id)
    except ValueError:
        return '{ "Error" : "elec_round_id has to be an int (base 10)." }'

    # Get ElectionRound object from the DB.
    elec_round = session.query(ElectionRound).filter_by(
            id=elec_round_id
        ).first()
    session.commit()

    # Handle invalid election round
    if elec_round is None:
        return '{ "Error" : "No electionround for this id." }'

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

def getAllPersonsWhoHaveNotVoted(elec_round):
    '''Gibt alle Personen zurück die noch Nicht gewählt haben'''
    # TODO(Impl method)
    pass

