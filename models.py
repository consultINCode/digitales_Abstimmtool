from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import Table

engine = create_engine('sqlite:///test.db', echo=False)
Base = declarative_base()

class Choice(Base):
    '''A Single Choice for an Election round'''
    __tablename__ = 'choices'
    id = Column(Integer, primary_key=True)
    picture = Column(Text) # Picture as Base64-Encoded String
    description = Column(String, nullable=False)
    counter = Column(Integer, nullable=False)

    # Make the link to election round
    election_round_id = Column(Integer, ForeignKey('election_rounds.id'))
    election_round = relationship("ElectionRound", back_populates="choices")


# Associationtable between election_round and person
has_voted_table = Table('has_voted_table', Base.metadata,
    Column('electionRound_id', Integer, ForeignKey('election_rounds.id')),
    Column('person_id', Integer, ForeignKey('persons.id'))
)

class ElectionRound(Base):
    ''' An single election round for on position / decision '''
    __tablename__ = 'election_rounds'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    running = Column(String, nullable=False) # "not_started" , "running" , "finished"
    max_choices_per_person = Column(Integer, nullable=False)
    
    # Link to choice
    choices = relationship("Choice", back_populates="election_round")

    # Link to persons_voted
    persons_voted = relationship("Person", secondary=has_voted_table, back_populates="voted_in_electionround")
    

# Special Table recording the relationships of members who were elected to cast the vote for others
has_choice_proxy_table = Table('has_choice_proxy_table', Base.metadata,
    Column('receiver_id', Integer, ForeignKey('persons.id')),
    Column('sender_id', Integer, ForeignKey('persons.id'))
)

class Person(Base):
    ''' A member of consult.IN who is generally eligible to vote'''
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_present = Column(Boolean, nullable=False)
    role = Column(String, nullable=False) # 0 = Admin; 1 = User, 2 = Election Supervisor, 3 = Admin Election Supervisor
    
    voted_in_electionround = relationship("ElectionRound", secondary=has_voted_table, back_populates="persons_voted")

    # Handling for Many-To-Many in one Table
    received_proxy_vote = relationship(
        'Person',
        secondary=has_choice_proxy_table,
        primaryjoin=id == has_choice_proxy_table.c.receiver_id,
        secondaryjoin=id == has_choice_proxy_table.c.sender_id,
        backref=backref('has_proxied_vote_to')
    )


# Create tables
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Tests
## Person
p1 = Person()
p1.name = "Anna"
p1.password = "Test"
p1.is_present = True
p1.role = 0

p2 = Person()
p2.name = "Bob"
p2.password = "Test2"
p2.is_present = False
p2.role = 1
# TODO(Voing and proxy)

## Elec-Rounds
elec_round = ElectionRound()
elec_round.title = "ElecRound 1"
elec_round.running = "running"
elec_round.max_choices_per_person = 1

## Choices
ch1 = Choice()
ch1.picture = "ABC"
ch1.description = "Description ch1"
ch1.counter = 4
ch1.elec_round = elec_round
#ch1.election_round_id = 1

ch2 = Choice()
ch2.picture = "DEF"
ch2.description = "Description ch2"
ch2.counter = 2
ch2.elec_round = elec_round
#ch2.election_round_id = 1

session.add(p1)
session.add(p2)
session.add(elec_round)
session.add(ch1)
session.add(ch2)

session.commit()

# Create objects
# father = Father()
# child = Child("Kind", father)

# Create objects
# session.add(father)
# session.commit()
# session.add(child)
# session.commit()

# Show all fathers with all children
# for entry in session.query(Father).all():
#     print(entry.name)
#     for child in entry.childs:
#         print(child.name)

