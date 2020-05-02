import re

def validateFirstName(s):
    regexPattern = re.compile("[A-Za-z0-9_.,!\"'/$]*")
    if regexPattern.match(s) and len(s) <= 100:
        return True
    return False

def validateLastName(s):
    regexPattern = re.compile("[A-Za-z0-9_.,!\"'/$]*")
    if regexPattern.match(s) and len(s) >= 1 and len(s) <=100:
        return True
    return False

def validateFirstHackathon(s):
    if s == 'yes' or s == 'no':
        return True
    return False

def validateAge(s):
    regexPattern = re.compile("[0-9]")
    if len(str(s)) <= 3 and regexPattern.match(s):
        return True
    return False

def validateParticipate(s):
    regexPattern = re.compile("[A-Za-z0-9_.,!\"'/$]*")
    if regexPattern.match(s) and len(s) <= 500:
        return True
    return False

def validateAccommodation(s):
    regexPattern = re.compile("[A-Za-z0-9_.,!\"'/$]*")
    if regexPattern.match(s) and len(s) <= 150:
        return True
    return False

def validateStudent(s):
    if s == 'yes' or s == 'no':
        return True
    return False




