from aeproductsstore import db

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)

    first_name= db.Column(db.String(15), unique=True)

    last_name= db.Column(db.String(15), unique=True)

    contact = db.Column(db.String(15), unique=True)

    email = db.Column(db.String(50), unique=True)

    address = db.Column(db.String(100), unique=True)

    password = db.Column(db.String(256), unique=True)

    def __repr__(self) -> str:
        return super().__repr__()

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)

    first_name= db.Column(db.String(15), unique=True)

    last_name= db.Column(db.String(15), unique=True)

    contact = db.Column(db.String(15), unique=True)

    email = db.Column(db.String(50), unique=True)

    address = db.Column(db.String(100), unique=True)

    password = db.Column(db.String(256), unique=True)

    role = db.Column(db.String(15), unique=True)


    def __repr__(self) -> str:
        return super().__repr__()