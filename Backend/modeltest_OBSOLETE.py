from models import session
from models import Choice,Person, ElectionRound


def dummydata():
    ## Person
    p1 = Person()
    p1.name = "Anna"
    p1.password = "hunter2"
    p1.is_present = True
    p1.role = 0

    p2 = Person()
    p2.name = "Bob"
    p2.password = "lol123"
    p2.is_present = False
    p2.role = 1

    ## Elec-Rounds
    elec_round = ElectionRound()
    elec_round.title = "Braucht Ihr Pause?"
    elec_round.running = "running"
    elec_round.max_choices_per_person = 1

    ## Choices
    ch1 = Choice()
    ch1.picture = "beer.png"
    ch1.description = "Ja!"
    ch1.counter = 4
    #ch2.elec_round = elec_round

    ch2 = Choice()
    ch2.picture = "working.jpg"
    ch2.description = "Ne, passt..."
    ch2.counter = 2
    ch2.election_round = elec_round

    # RELATIONSHIP (pls work)

    # The example Choice belongs to the first Election Round 
    ch1.election_round = elec_round
    # Anna and Bob both Voted in the first Election Round
    p1.voted_in_election_round.append(elec_round)
    p2.voted_in_election_round.append(elec_round)
    # Anna has Bobs Vote
    p1.received_proxy_vote.append(p2)

    session.add(p1)
    session.add(p2)
    session.add(elec_round)
    session.add(ch1)
    session.add(ch2)

    session.commit()