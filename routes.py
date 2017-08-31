from packjoy.app import app, db, pp
from packjoy.models import Email
from packjoy.forms import EmailForm
from packjoy.moltin_helper import get_prods_by_slug
from flask import jsonify, request, render_template


@app.route('/api/email', methods=['POST'])
def adding_email_address():
    form = EmailForm()
    form.from_json(request.get_json())
    if form.validate():
        if Email.query.filter_by(email=form.email.data).first() is None:
            newsletter_subs = Email(email=form.data['email'])
            db.session.add(newsletter_subs)
            db.session.commit()
            return jsonify({ 'message' : '10% discount in your inbox. Use this email address at checkout!' }), 200
        return jsonify({ 'message': 'This email has already joined.' }), 400
    return jsonify({ 'message' : form.errors }), 400


@app.route('/api/products/')
@app.route('/api/products/<slug>')
def get_products(slug=None):
    data = get_prods_by_slug(slug)
    return jsonify(data)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/amp/')
def amp_index():
    products = get_prods_by_slug(slug=None)
    return render_template('index-amp.html', products=products)