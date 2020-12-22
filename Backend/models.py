# pylint: disable=maybe-no-member
import configparser
from sqlalchemy import (
    Boolean,
    create_engine,
    Column,
    ForeignKey,
    Integer,
    String,
    Text,
    Table
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
#for AdminAccount

from passlib.hash import argon2
from random import choice



# Init configparser
config = configparser.ConfigParser()
config.read('config.ini')

engine = create_engine(
    config['DB']['db_con_string'], 
    echo=(config['DB']['echo'] == "True")) # Hacky conversion
Base = declarative_base()

# Linking Table for Votes per Electionround
has_voted_table = Table('has_voted_table', Base.metadata,
     Column(
         'has_voted_in_election_round_id', 
         Integer, 
         ForeignKey('election_rounds.id')
    ),
     Column('person_id', Integer, ForeignKey('persons.id'))
)

# Special Table recording the relationships of members who were elected to 
# cast the vote for others
has_choice_proxy_table = Table('has_choice_proxy_table', Base.metadata,
     Column('receiver_id', Integer, ForeignKey('persons.id')),
     Column('sender_id', Integer, ForeignKey('persons.id'), unique = True)
)


class ElectionRound(Base):
    ''' An single election round for on position / decision '''
    __tablename__ = 'election_rounds'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    # Values of running: "not_started" , "running" , "finished"
    running = Column(String, nullable=False) 
    max_choices_per_person = Column(Integer, nullable=False)


class Choice(Base):
    '''A Single Choice for an Election round'''
    __tablename__ = 'choices'
    id = Column(Integer, primary_key=True)
    picture = Column(Text) # Picture as Base64-Encoded String
    description = Column(String, nullable=False)
    counter = Column(Integer, nullable=False)

    # Make the link to election round
    election_round_id = Column(Integer, ForeignKey('election_rounds.id'))
    election_round = relationship("ElectionRound", backref="choices")


class Person(Base):
    ''' A member of consult.IN who is generally eligible to vote'''
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    mail = Column(String, nullable=False, unique = True)
    password = Column(String, nullable=False)
    is_present = Column(Boolean, nullable=False)
    # Values of role:
    #   0 = User 
    #   1 = Election Supervisor
    #   2 = Admin
    #   3 = Admin Election Supervisor
    role = Column(String, nullable=False) 
    
    voted_in_election_round = relationship(
        "ElectionRound", secondary=has_voted_table, backref="persons_voted")

    # Handling for Many-To-Many in one Table
    # Relationship records members who gave their vote to someone else
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

if config['DB']['add_test_data'] == "True":     
    ## ADD SOME TEST DATA INTO DB
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
    
    session.commit()
