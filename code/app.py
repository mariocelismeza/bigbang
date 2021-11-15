from datetime import timedelta

from flask import Flask
from flask_restful import Api

from resources.bigbang import BigBang

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #In order to know when the object change
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


#List of resources
api.add_resource(BigBang, '/bigbang')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)