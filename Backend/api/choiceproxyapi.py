# pylint: disable=maybe-no-member
import json
import logging
import sys
import os
from passlib.hash import argon2
from random import choice
import api.response_helper as Response

# TODO(What is this and what does it do here?)
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from models import session,Choice, Person, has_choice_proxy_table

def create_choice_proxy(data: dict) -> bool:
    '''Create an proxy for an voter.'''
    if not 'senderid' in data: 
        return Response.wrong_format({'message':'senderid missing'})
    if not type(data['senderid']) == int:
        return Response.wrong_format({'message' : 'senderid: not a number'})
    
    if not 'receiverid' in data: 
        return Response.wrong_format({'message':'receiverid missing'})
    if not type(data['receiverid']) == int:
        return Response.wrong_format({'message' : 'receiverid: not a number'})
    
    if data['receiverid'] == data['senderid']: 
        return Response.wrong_format({'message':'receiverid equals senderid'})
    
    try:
        choice = session.query(has_choice_proxy_table).filter(
            has_choice_proxy_table.c.sender_id == data["senderid"]).first()
        if choice:
            return Response.wrong_format({'message':'senderid {} already gave their vote'.format(data['senderid'])})
        receiver = session.query(Person).filter(
            Person.id == data['receiverid']).first()
        if not receiver:
            return Response.ressource_not_found({'message' : 'receiverid: not found'})
        sender = session.query(Person).filter(
            Person.id == data['senderid']).first()
        if not sender:
            return Response.ressource_not_found({'message' : 'senderid: not found'})
        print('line 40')
        receiver.received_proxy_vote.append(sender)
        session.commit()
    except Exception as e:
        print(e)
        return Response.database_error()
    return Response.ok({"success": True, 'message':'senderid {} gave vote to receiverid {}'.format(sender.id, receiver.id)})
    

def delete_choice_proxy(id: int) -> bool:
    '''Deletes an choice proxy.'''
    #choice = session.query(Person).join(
    #   has_choice_proxy_table).join(Person).filter(
    #   has_choice_proxy_table.sender_id == id).first()
    try:
        choice = session.query(has_choice_proxy_table).filter(
            has_choice_proxy_table.c.sender_id == id).first()
        if not choice:
            return Response.ressource_not_found({'message':'senderid not found'})
        receiver = session.query(Person).filter(
            Person.id == choice.receiver_id).first()
        sender = session.query(Person).filter(
            Person.id == choice.sender_id).first()
        receiver.received_proxy_vote.remove(sender)
        session.commit()
    except Exception as e:
        print(e)
        return Response.database_error()
    return Response.ok({"success": True, 'message':'senderid {} deleted vote from receiverid {}'.format(sender.id,receiver.id)})

def update_choice_proxy(data: dict) -> bool:
    '''Updates an choice proxy'''
    if not 'senderid' in data: 
        return Response.wrong_format({'message':'senderid missing'})
    if not type(data['senderid']) == int:
        return Response.wrong_format({'message' : 'senderid: not a number'})
    
    if not 'receiverid' in data: 
        return Response.wrong_format({'message':'receiverid missing'})
    if not type(data['receiverid']) == int:
        return Response.wrong_format({'message' : 'receiverid: not a number'})
    
    if data['receiverid'] == data['senderid']: 
        return Response.wrong_format({'message':'receiverid equals senderid'})
    
    try:
        receiver = session.query(Person).filter(
            Person.id == data['receiverid']).first()
        sender = session.query(Person).filter(
            Person.id == data['senderid']).first()
        delete_choice_proxy(data['senderid'])
        receiver.received_proxy_vote.append(sender)
        session.commit()
    except:
        return Response.database_error()
    return Response.ok({"success": True, 'message':'senderid {} gave vote to receiverid {}'.format(sender.id, receiver.id)})
