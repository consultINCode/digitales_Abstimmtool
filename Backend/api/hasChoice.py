import json
import logging
import sys
import os
from passlib.hash import argon2
from random import choice

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from models import session,Choice, Person, has_choice_proxy_table


## Has_Choice


#Stimmübertragung von Sender zu Receiver erstellen
def createChoiceProxy(data):
    receiver = session.query(Person).filter(Person.id == data['receiverid']).first()
    sender = session.query(Person).filter(Person.id == data['senderid']).first()
    receiver.received_proxy_vote.append(sender)

    try:
         session.commit()
    except:
        return False
    return True


#Löscht eine Stimmübertragung
def deleteChoiceProxy(id):
    #choice = session.query(Person).join(has_choice_proxy_table).join(Person).filter(has_choice_proxy_table.sender_id == id).first()
    choice = session.query(has_choice_proxy_table).filter(has_choice_proxy_table.c.sender_id == id).first()
    receiver = session.query(Person).filter(Person.id == choice.receiver_id).first()
    sender = session.query(Person).filter(Person.id == choice.sender_id).first()
    receiver.received_proxy_vote.remove(sender)
    try:
         session.commit()
    except:
        return False
    return True


#Stimmübertragung für Sender bearbeiten und neuen Receiver eintragen

def updateChoiceProxy(data):
    receiver = session.query(Person).filter(Person.id == data['receiverid']).first()
    sender = session.query(Person).filter(Person.id == data['senderid']).first()
    #deleteChoiceProxy(data['senderid'])
    receiver.received_proxy_vote.append(sender)

    try:
         session.commit()
    except:
        return False
    return True