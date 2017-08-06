import uuid 

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    token = db.Column(db.String(20), unique=True)

    def __init__(self, email):
        self.email = email
        self.token = uuid.uuid4().hex[:6].upper()

    def __repr__(self):
        return '<Subscriber %r>' % self.Email