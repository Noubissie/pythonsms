from flask_sqlalchemy import SQLAlchemy
from flask import Flask
# import flask_whooshalchemy as wa

#  flaskwebgui is misbehaving due to debug on, hence always put it off

app = Flask(__name__)  # can't use two app in one project

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://NOUBISSIE:n678201252l@localhost/NOUBISSIE$school_database'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:678201252@localhost/NOUBISSIE$school_database'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:////home/landryplacid/Desktop/report_card_complete/test.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['DEBUG'] = True
app.config['WHOOSH_BASE'] = 'whoosh'

db = SQLAlchemy(app)
