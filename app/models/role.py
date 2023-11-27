from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(54), nullable=True)
    role_description = db.Column(db.String(100), nullable=True)
