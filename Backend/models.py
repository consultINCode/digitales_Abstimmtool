from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import Table

engine = create_engine('sqlite:///test.db', echo=False)
Base = declarative_base()

#Linking Table for Votes per Electionround
has_voted_table = Table('has_voted_table', Base.metadata,
     Column('has_voted_in_election_round_id', Integer, ForeignKey('election_rounds.id')),
     Column('person_id', Integer, ForeignKey('persons.id'))
)

#Special Table recording the relationships of members who were elected to cast the vote for others
has_choice_proxy_table = Table('has_choice_proxy_table', Base.metadata,
     Column('receiver_id', Integer, ForeignKey('persons.id')),
     Column('sender_id', Integer, ForeignKey('persons.id'), unique = True)
)
class ElectionRound(Base):
    ''' An single election round for on position / decision '''
    __tablename__ = 'election_rounds'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    running = Column(String, nullable=False) # "not_started" , "running" , "finished"
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
    password = Column(String, nullable=False)
    is_present = Column(Boolean, nullable=False)
    role = Column(String, nullable=False) # 0 = Admin; 1 = User, 2 = Election Supervisor, 3 = Admin Election Supervisor
    
    voted_in_election_round = relationship("ElectionRound", secondary=has_voted_table, backref="persons_voted")

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





# Relationships Basic How To:

# class Customer(Base):
#    __tablename__ = 'customers'

#    id = Column(Integer, primary_key = True)
#    name = Column(String)
#    address = Column(String)
#    email = Column(String)

# class Invoice(Base):
#    __tablename__ = 'invoices'
   
#    id = Column(Integer, primary_key = True)
#    custid = Column(Integer, ForeignKey('customers.id'))
#    invno = Column(Integer)
#    amount = Column(Integer)
#    customer = relationship("Customer", back_populates = "invoices")

# c1 = Customer(name = "Gopal Krishna", address = "Bank Street Hydarebad", email = "gk@gmail.com")
# c1.invoices = [Invoice(invno = 10, amount = 15000), Invoice(invno = 14, amount = 3850)]
