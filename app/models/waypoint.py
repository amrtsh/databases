from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Type(db.Model):
    __tablename__ = 'type'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(54), nullable=True)
    latitude = db.Column(db.DECIMAL, nullable=True)
    longitude = db.Column(db.DECIMAL, nullable=True)
