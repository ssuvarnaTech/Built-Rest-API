import firebase_admin
import logging
from firebase_admin import firestore
import flask


project_id = "corded-racer-275903"
default_app = firebase_admin.initialize_app()

db = firestore.client()
hacker_ref = db.collection('Hackers')

# expects request to contain name of hacker
def getHackerInfo(request):
    try:
        identifier = request.args.get('user')
        hackerDoc = hacker_ref.document(identifier)
        hacker = hackerDoc.get()
        if hacker.exists:
            responseDict = dict()
            responseDict["hackerInfo"] = hacker.to_dict()
            responseDict["code"] = 200
            response = flask.jsonify(responseDict)
            return response
    except:
        return flask.jsonify({"code": 400, "error": "Could not get user."}), 400



def createNewHacker(request):
    try:
        keyValuePairs = request.json
        identifier = keyValuePairs['firstName'] + keyValuePairs['lastName']
        logging.info("identifier: " + identifier)
        hacker_ref.document(identifier).set(keyValuePairs)
        return flask.jsonify({"code": 200, "message": "Successful post to database!"}), 200
    except:
        return flask.jsonify({"code": 400, "error": "Could not post successfully to database."}), 400

def updateHacker(request):
    try:
        keyValuePairs = request.json
        firstName = keyValuePairs['firstName']
        lastName = keyValuePairs['lastName']
        identifier = firstName + lastName
        hackerDoc = hacker_ref.document(identifier)
        hackerDoc.update(keyValuePairs)
        return flask.jsonify({"code": 200, "message": "Successfully updated!"}), 200
    except:
        return flask.jsonify({"code": 400, "error": "Could not update successfully."}), 400

