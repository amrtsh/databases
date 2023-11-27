from flask import Flask
from app.models.BaseModel import db
from app import routes
from app import config


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1111@localhost/mydb'
# db.init_app(app)
#
# with app.app_context():
#     db.create_all()
