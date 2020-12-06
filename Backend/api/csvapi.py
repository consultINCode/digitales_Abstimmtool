# pylint: disable=maybe-no-member

import api.response_helper as Response
from pandas import read_csv
from models import Person,session
from api.personapi import generate_password

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

    for index, row in csv_file_pandas.iterrows():
        person = Person()
        person.name = '{} {}'.format(row[first_name], row[surname])
        # TODO: Encpyt Passwords
        person.password = generate_password().new_password
        person.mail = row[mail]
        person.is_present = False
        person.role = "0"
        session.add(person)
    
    try:
         session.commit()
    except:
        return Response.database_error()    
    return Response.ok({'message':'ok'})
