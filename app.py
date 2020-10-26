from chatbot import chatbot
from flask import Flask, render_template, request
from flask import jsonify
import json
from waitress import serve

a = {"resposne": ""}

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_bot_response", methods=[ 'GET'])
def get_bot_response():
    if request.method == 'GET':
        userText = request.args.get('msg')
        response = str(chatbot.get_response(userText))
        print(response)
        return response

if __name__ == "__main__":
    app.run() 
