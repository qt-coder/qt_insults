from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
api = Api(app)


insults=[
        {"insult": "The hospital called. Your test results came back positive. You're a stage 5 dumbass."}, 
        {"insult": "In a battle of wits, you would be weaponless."},
        {"insult": "Your family tree is a cactus, because everybody on it is a prick"},
        {"insult": "If you really want to know about mistakes, you should ask your parents."},
        {"insult": "I could eat a bowl of alphabet soup and crap out a better comeback than what you just said."}
        ]



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def apipage():
    return render_template('api.html')



class Insult(Resource):
    def get(self):
        return insults[random.randint(0, len(insults)-1)]

api.add_resource(Insult, "/randominsult")

if __name__ == "__main__":
	app.run(debug=True)
