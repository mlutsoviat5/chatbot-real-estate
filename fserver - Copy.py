from flask import Flask
from flask import request
from flask_cors import CORS
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import random


app = Flask(__name__)
CORS(app)

@app.route("/")
def chat_bot_reply():
    textMessage = request.args.get('textMessage')
    chatbot = ChatBot("DK")
    conv = open('chats.txt','r').readlines()
    chatbot.set_trainer(ListTrainer)
    chatbot.train(conv)
    response = str(chatbot.get_response(textMessage))
    return response
	
    if __name__ == '__main__':
        app.run(debug = True)