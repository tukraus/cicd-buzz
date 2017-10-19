import os
import signal
from flask import Flask
from buzz import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    page = '<html><title>CICD-BUZZ: ' + os.getenv('TITLE') + '</title><body><h1>'
    page += generator.show_buzzes().replace('\n', '<br />\n')
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))

