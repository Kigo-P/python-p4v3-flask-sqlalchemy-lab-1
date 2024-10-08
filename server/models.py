from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthquake(db.Model,SerializerMixin):
    # creating a table called earthquakes
    __tablename__ = "earthquakes"
    # creating columns with their data types
    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float, nullable=False)
    location = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)

    # a repr method to represent the string format 
    def __repr__(self) -> str:
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"
    pass