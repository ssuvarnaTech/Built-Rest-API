# File: main_emulate.py
import flask
from main import getHackerInfo, createNewHacker, updateHacker
import os

app = flask.Flask('functions')
methods = ['GET', 'POST', 'PUT', 'DELETE']

@app.route('/getHackerInfo', methods=['GET'])
def directGet():
    return getHackerInfo(flask.request)

@app.route('/createNewHacker', methods=["POST"])
def directPost():
    print("WE HERE BRO")
    return createNewHacker(flask.request)

@app.route('/updateHacker', methods=["PUT"])
def directPut():
    return updateHacker(flask.request)

if __name__ == '__main__':
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/sreevanisuvarna//Users/sreevanisuvarna/cruzhacks-engineering-firebase-adminsdk-vi27b-430cb4a4d1.json"
    app.run()
