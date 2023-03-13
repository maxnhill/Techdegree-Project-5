from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db.init_app(app)

class Projects(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column('Title',db. String())
    date = db.Column('Date', db.String())
    description = db.Column('Description', db.String())
    skills = db.Column('Skills Practiced', db.String())
    github_url = db.Column('Github Link', db.String())



 
def __repr__(self):
    return f'''< Title: {self.title} Date:{self.date} Description: {self.description} 
                Skills: {self.skills} Github Link: {self.github_url}>'''