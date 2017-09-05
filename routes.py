from packjoy.app import app, db, pp
from packjoy.models import Email
from packjoy.forms import EmailForm
from packjoy.moltin_helper import get_prods_by_slug
from flask import jsonify, request, render_template, redirect, url_for
from flask import abort


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

@app.route('/amp/<brand>')
def amp_brand_page(brand):
    products = brand
    return render_template('brand-page-amp.html', products=products)

@app.route('/amp/<brand>/<product>')
def amp_product_page(brand, product):
    prod = get_prods_by_slug(product)
    if prod is None:
        # There is no such a prduct
        # raise a 404 Error
        abort(404) 
    brand_slug = prod.brand['slug']
    if brand_slug != brand:
        return redirect(url_for('amp_product_page', brand=prod.brand['slug'], product=prod.slug))
    return render_template('product-page-amp.html', product=prod)