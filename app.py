from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from moltin.moltin import Moltin
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('packjoy.config.Development')


# Moove somewhere else
m = Moltin(app.config['MOLTIN_CLIENT_ID'], app.config['MOLTIN_CLIENT_SECRET'])
access_token = m.authenticate()


db = SQLAlchemy(app)
migrate = Migrate(app, db)

admin = Admin(app, name='packjoy', template_mode='bootstrap3')
import packjoy.admin

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/amp/')
def amp_index():
	return render_template('index-amp.html')

import packjoy.routes

if __name__ == "__main__":
    app.run(debug=True) 