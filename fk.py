from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/hi", methods=['GET','POST'])
def hi():
    print("hi")
    if request.method=='GET':
        return jsonify({"ft":"hi"})
    else:
        return "other methods"

if __name__ == "__main__":
    app.run(port=1000)