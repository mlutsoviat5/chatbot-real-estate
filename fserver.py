from flask import Flask
from flask import request
from flask_cors import CORS
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import random


fserver = Flask(__name__)
CORS(fserver)

@fserver.route("/")
def check_for_greeting():
    textMessage = request.args.get('textMessage')
    chatbot = ChatBot("DK")
    conv = open('chats.txt','r').readlines()
    chatbot.set_trainer(ListTrainer)
    chatbot.train(conv)
    response = str(chatbot.get_response(textMessage))
    return response
	
    if __name__ == '__main__':
        fserver.run(debug = True)