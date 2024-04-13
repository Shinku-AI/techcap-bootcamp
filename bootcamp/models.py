from bootcamp import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    program = db.Column(db.String(30), nullable=True)
    area_of_interest = db.Column(db.String(30), nullable=True)

    def fullname(self):
        return self.last_name + ' ' + self.first_name

    def __repr__(self):
        return f"User('{self.fullname()}', '{self.email}')"

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
