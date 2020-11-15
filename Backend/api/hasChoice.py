# pylint: disable=maybe-no-member
import json
import logging
import sys
import os
from passlib.hash import argon2
from random import choice

# TODO(What is this and what does it do here?)
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from models import session,Choice, Person, has_choice_proxy_table

def create_choice_proxy(data: dict) -> bool:
    '''Create an proxy for an voter.'''
    receiver = session.query(Person).filter(
        Person.id == data['receiverid']).first()
    sender = session.query(Person).filter(
        Person.id == data['senderid']).first()
    receiver.received_proxy_vote.append(sender)

    try:
         session.commit()
    except:
        return False
    return True

def delete_choice_proxy(id: int) -> bool:
    '''Deletes an choice proxy.'''
    #choice = session.query(Person).join(
    #   has_choice_proxy_table).join(Person).filter(
    #   has_choice_proxy_table.sender_id == id).first()
    choice = session.query(has_choice_proxy_table).filter(
        has_choice_proxy_table.c.sender_id == id).first()
    receiver = session.query(Person).filter(
        Person.id == choice.receiver_id).first()
    sender = session.query(Person).filter(
        Person.id == choice.sender_id).first()
    receiver.received_proxy_vote.remove(sender)
    try:
         session.commit()
    except:
        return False
    return True

def update_choice_proxy(data: dict) -> bool:
    '''Updates an choice proxy'''
    receiver = session.query(Person).filter(
        Person.id == data['receiverid']).first()
    sender = session.query(Person).filter(
        Person.id == data['senderid']).first()
    #delete_choice_proxy(data['senderid'])
    receiver.received_proxy_vote.append(sender)

    try:
         session.commit()
    except:
        return False
    return True