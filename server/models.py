# server/models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Contains definitions of tables and associated schema constructs
metadata = MetaData()

# Create the Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

# Define the Pet model class by inheriting from db.Model
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    species = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Pet {self.id}, {self.name}, {self.species}>"
