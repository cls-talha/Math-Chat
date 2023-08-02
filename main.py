from flask import Flask, render_template, request
from llm_api import *


chatLLAMA = LLM(get_apiKey()) #create an instance of the LLM class
app = Flask(__name__) #create the flask app


@app.route('/')
def homePage():
    return render_template('index.html') #render the html template


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatLLAMA.get_reply(userText)


if __name__ == '__main__':
    app.run(debug=True)

