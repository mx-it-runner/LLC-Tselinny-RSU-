from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import ImageUploadField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'asda9sf79as7f9asf6sad7f6s8dfasd1231ad'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(100), nullable=False) 
    price = db.Column(db.Float, nullable=False)  
    description = db.Column(db.Text)
    image_path = db.Column(db.String(255))

with app.app_context():
    db.create_all()

admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')

class ProductView(ModelView):
    form_extra_fields = {
        'image_path': ImageUploadField('Image', base_path='static/images/products/', url_relative_path='static/')
    }

admin.add_view(ProductView(Product, db.session, name='product_admin'))

# Главная страница
@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

# Страница каталога товаров
@app.route('/catalog')
def catalog():
    products = Product.query.all()
    return render_template('catalog.html', products=products)


@app.route('/contact')
def contacts():
    return render_template('contact.html')

# Страница "О нас"
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/download_price')
def download_price():
    filename = 'price_list.xlsx'
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
