from flask import Flask, jsonify, request
import sqlite3
app = Flask(__name__)

random_page = open("test2.html", "r").read()
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "http://127.0.0.1:5500" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE, FUCK"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

@app.route("/", methods=["POST"])
def hello():
    # return f"""<h1> What are you looking at {request.get_json()["data"]}</h1>"""
    return random_page

if __name__ == '__main__': 
  
    app.run(debug=True) 
