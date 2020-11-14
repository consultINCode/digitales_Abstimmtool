from flask import Flask, Response,request, render_template
import urllib.request, json 

import logging

app = Flask(__name__)
if __name__ == "__main__":
    app.run(port=80)

# Init logging
logging.basicConfig(filename='example.log', level=logging.DEBUG)

# Some example log lines
logging.info("test")
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

@app.route('/')
def index():
   return render_template('welcome.html')

@app.route('/showAllPersons')
def showAllPersons():
    with urllib.request.urlopen("http://127.0.0.1:5000/api/persons/getAllPersons") as url:
        data = json.loads(url.read().decode())
        return render_template('/showAllPersons.html', persons=data)
