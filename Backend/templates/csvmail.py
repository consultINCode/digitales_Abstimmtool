#mail template to send password to user
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


import configparser
config = configparser.ConfigParser()
config.read('config.ini')

URL = config['Server']['domain']

def get_message(name: str, password: str, mail: str) -> str:
    
    msg = MIMEMultipart('alternative')
    msg.set_charset("utf-8")
    msg['Subject'] = 'Dein Passwort für das Abstimmtool'
    msg['From'] = config['Mail_Server']['mail']
    msg['To'] = mail

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    #TODO: Move to seperate File
    html = '''
    <html>
    <head></head>
    <body><h4>Hallo {}</h4>
    <p>Willkommen beim digitalen Abstimmtool.</p>
    <p>Bei der nächsten Wahl kannst du dich mit deiner Mailadresse und dem Passwort 
    <b>{}</b>
    auf {} anmelden.</p>
    <p>Wir freuen uns auf dich!</p>
    <p>Dein Abstimmtool-Bot</p>
    <b>consult.IN</b><br/> 
    Studentische Unternehmensberatung<br/> 
    Technische Hochschule Ingolstadt<br/>
    Esplanade 10 | 85049 Ingolstadt <br/>
    www.consultin.net<br/>
    <br/>
    Sitz und Registergericht: Ingolstadt VR 200430 <br/>
    HINWEIS: Diese Nachricht ist vertraulich und nur für den Adressaten bestimmt.
    Sollten Sie irrtümlich diese Nachricht erhalten haben, bitte ich um Ihre Mitteilung per E-Mail an bereichsleitung.it@consultin.net.<br/>
    Automatisch versendete Nachricht<br/>
    ATTENTION: This message contains confidential information intended only for the person(s) named above. If you have received this message in error, please notify bereichsleitung.it@consultin.net immediately.<br/>
    This message was sent automaticly<br/>
    </body>
    </html>
    '''
    msg.attach(MIMEText(html.format(name, password, URL), 'html'))
    
    return  msg.as_string()