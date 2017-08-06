from flask import Flask
from flask import render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from moltin.moltin import Moltin
from forms import EmailForm
import uuid 

app = Flask(__name__)
app.config["WTF_CSRF_ENABLED"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

m = Moltin("6lI3pFVOxwB0CNRS5YJboKY7GXPHSgkMxD8QXmb7j3", "PuVZIDGLP9ws0Nph07dRwVR99l2mJf5iqiX8A1fA0b")
access_token = m.authenticate()

db = SQLAlchemy(app)

# This needs to be moved somewhere else
class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    token = db.Column(db.String(20), unique=True)

    def __init__(self, email):
        self.email = email
        self.token = uuid.uuid4().hex[:8].upper()

    def __repr__(self):
        return '<Subscriber %r>' % self.email


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/email', methods=['POST'])
def adding_email_address():
	form = EmailForm()
	form.from_json(request.get_json())
	
	if not form.validate():
		return jsonify({ 'message' : form.errors }), 400

	newsletter_subs = Email(email=form.data['email'])
	db.session.add(newsletter_subs)
	db.session.commit()
	return jsonify({ 'message' : 'Working properly!' }), 200



if __name__ == "__main__":
    app.run(debug=True) 