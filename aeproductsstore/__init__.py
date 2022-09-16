from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csc206databasesgroupae'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:qwertyui@localhost:3306/products_store'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products_store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from aeproductsstore import routes

db.create_all()
db.session.commit()