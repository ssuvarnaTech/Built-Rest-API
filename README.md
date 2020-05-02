# CruzHacks-Challenge-Suvarna-Sreevani
This project creates a REST API through Python through CRUD

There are three functions : updateHacker, getHackerInfo, and createNewHacker

1. POST Endpoint: https://us-central1-cruzhacks-engineering.cloudfunctions.net/createNewHacker

Taking this URL and pasting it on PostMan or another platform would allow to create a new profile for a hacker inside the database. It must be passed with a JSON request body with the following fields like given below:
Example:
{
    "firstName": "sreevani",
    "lastName": "suvarna",
    "age" : 20,
    "gender": "Female",
    "year": 2,
    "isStudent": false,
    "isFirstHackathon": true,
    "participation": "I love coding",
    "hasTransport": true,
    "needsSpecialAccommodation": false
  }
  

2. PUT Endpoint : https://us-central1-cruzhacks-engineering.cloudfunctions.net/updateHacker
  Taking this URL and pasting it on PostMan or another platform would allow to update a hacker's information inside the   database. It must be passed with a JSON request body with the following fields like given below:
  Example:
{
    "firstName": "sreevani",
    "lastName": "suvarna",
    "age" : 20,
    "gender": "Female",
    "year": 2,
    "isStudent": false,
    "isFirstHackathon": true,
    "participation": "I love coding",
    "hasTransport": true,
    "needsSpecialAccommodation": false
  }
  
3. GET Endpoint: https://us-central1-cruzhacks-engineering.cloudfunctions.net/getHackerInfo
Taking this URL gets the hacker's information inside the database. 
For example, if we took the header parameter passed with the hacker's first name and last name like below:
{
  "firstName": "sreevani",
  "lastName": "suvarna",
 }
 This would return the JSON object that would look like the example given below:
 {
    "code": 200,
    "hackerInfo": {
        "age": 54,
        "firstName": "harish",
        "gender": "male",
        "hasTransport": true,
        "isFirstHackathon": true,
        "isStudent": false,
        "lastName": "suvarna",
        "needsSpecialAccommodation": false,
        "participation": "I love aloobath",
        "year": 2
    }
}
