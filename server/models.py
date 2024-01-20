from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Enum

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)


class Zookeeper(db.Model):
    __tablename__ = "zookeepers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    Animal_id = db.Column(db.Integer, db.ForeignKey("animals.id"))


class Enclosure(db.Model):
    __tablename__ = "enclosures"

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(Enum("grass", "sand", "water"), nullable=False)
    open_to_visitors = db.Column(db.Boolean, nullable=False)


class Animal(db.Model):
    __tablename__ = "animals"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    species = db.Column(db.String(80), nullable=False)
    Zookeeper_id = db.Column(db.Integer, db.ForeignKey("zookeepers.id"))
    Enclosure_id = db.Column(db.Integer, db.ForeignKey("enclosures.id"))
