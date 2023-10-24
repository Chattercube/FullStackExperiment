SECRET = "thisissecret"

from flask import Flask, jsonify, request
import sqlite3
import hashlib
app = Flask(__name__)

con = sqlite3.connect("myDatabase.db")
cur = con.cursor()

def login(username:str, password:str):
    res = cur.execute(f"SELECT PasswordHash FROM Users WHERE Username='{username.lower()}';")
    pwdhash = res.fetchone()[0]
    if pwdhash is None:
        print("Invalid")
        return False
    m = hashlib.sha256()
    m.update(bytes(password, 'utf-8')+bytes(SECRET, 'utf-8'))
    print(pwdhash)
    print(m.hexdigest())

    if pwdhash != m.hexdigest():
        print("Wrong Password")
        return False
    
    return True

def createSession(username:str, duration = 86400) -> str: 
    sessionKey:str = "Null"

    return sessionKey

def getUsernameBySessionKey(sessionKey:str):
    return str

def clearExpiredSessions():
    pass



def getProfile(username:str):
    pass

login("ChaTTerCube","yes")


# @app.after_request
# def after_request(response):
#     response.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:5500" # <- You can change "*" for a domain for example "http://localhost"
#     response.headers["Access-Control-Allow-Credentials"] = "true"
#     response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE, FUCK"
#     response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
#     return response

# @app.route("/", methods=["POST"])
# def hello():
#     # return f"""<h1> What are you looking at {request.get_json()["data"]}</h1>"""
#     return random_page

# if __name__ == '__main__': 
  
#     app.run(debug=True) 


