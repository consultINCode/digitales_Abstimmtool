# pylint: disable=maybe-no-member

import api.response_helper as Response
from pandas import read_csv
from models import Person,session
from passlib.hash import argon2
from random import choice
from api.personapi import generate_password
from sqlalchemy.exc import IntegrityError

import configparser
config = configparser.ConfigParser()
config.read('config.ini')


def upload_csv(file):
    first_name = 'fn'
    surname = 'sn'
    mail = 'mail'
    if not file:
        return Response.wrong_format({'message':'no file'})

    try:
        csv_file_pandas = read_csv(file, usecols=[first_name, surname, mail])
    except ValueError:
        return Response.wrong_format({'message':'.csv columns missing. Must contain {}, {}'.format(first_name, surname, mail)})
    except:
        return Response.server_error({'message':'error processing .csv-file'})

    pw_list = []

    for index, row in csv_file_pandas.iterrows():
        person = Person()
        person.name = '{} {}'.format(row[first_name], row[surname])
        password = ''.join(
            [choice('abcdefghijklmnopqrstuvwxyz0123456789-') for i in range(15)])
        person.password = argon2.hash(password)
        person.mail = row[mail]
        person.is_present = False
        person.role = '0'
        pw_list.append({'mail':person.mail, 'password':password, 'name': person.name})
        session.add(person)
    
    duplicates = []
    try:
         session.commit()
    except IntegrityError as e:
        print(e)
        duplicates.append(e)
    except:
        return Response.database_error()

    send_email(pw_list)
    
    return Response.ok({'message':'ok', "duplicates" : str(duplicates)})

def send_email(mail_list):
    import smtplib, ssl
    from templates.csvmail import get_message

    smtp_server = config['Mail_Server']['smtp_server']
    port = config.getint('Mail_Server','port')
    sender_email = config['Mail_Server']['mail']
    password = config['Mail_Server']['password']
    context = ssl.create_default_context()  


    try:
        server = smtplib.SMTP(smtp_server,port)
        server.starttls(context=context) # Secure the connection
        server.login(sender_email, password)
        for recipient in mail_list:
            message = get_message(recipient['name'], recipient['password'], recipient['mail'])
            server.sendmail(sender_email, recipient['mail'], message)
            print('mail sent to {}'.format(recipient['mail']))
    except Exception as e:
        print(e)
        return Response.server_error({'message':'error while sending mails'})
    finally:
         server.quit()

def createadmin():
    pw_list = []
    person = Person()
    person.name = '{} {}'.format("Admin", "Er hat die Macht")
    password = ''.join(
        [choice('abcdefghijklmnopqrstuvwxyz0123456789-') for i in range(15)])
    person.password = argon2.hash(password)
    person.mail = config['Mail_Server']['mail']
    person.is_present = False
    person.role = '2'
    pw_list.append({'mail':person.mail, 'password':password, 'name': person.name})
    print(str(pw_list))
    session.add(person)
    try:
        session.commit()
    except IntegrityError as e:
        print(e)
    except:
        print("test")
    send_email(pw_list)
