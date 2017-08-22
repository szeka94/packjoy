from packjoy.app import app, db
from packjoy.models import Email
from packjoy.forms import EmailForm
from packjoy.moltin_helper import get_prods_by_slug
from flask import jsonify, request


@app.route('/api/email', methods=['POST'])
def adding_email_address():
	form = EmailForm()
	form.from_json(request.get_json())
	if form.validate():
		if Email.query.filter_by(email=form.email.data).first() is None:
			newsletter_subs = Email(email=form.data['email'])
			db.session.add(newsletter_subs)
			db.session.commit()
			return jsonify({ 'message' : 'Working properly!' }), 200
		return jsonify({ 'message': 'This email has already joined.' })
	return jsonify({ 'message' : form.errors }), 400


@app.route('/api/products/')
@app.route('/api/products/<slug>')
def get_products(slug=None):
	data = get_prods_by_slug(slug)
	print(data)
	return jsonify(data)