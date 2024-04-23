from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(100), nullable=False) 
    price = db.Column(db.Float, nullable=False) 
    # image = db.Column(db.String(255)) 
    # description = db.Column(db.Text)
    def __repr__(self):
        return '<Item %r>' % self.title

# Главная страница
@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

# Страница каталога товаров
@app.route('/catalog')
def catalog():
    # Здесь можно добавить логику для загрузки данных о товарах из базы данных или другого источника
    # Затем передать эти данные в шаблон для отображения
    return render_template('catalog.html')

# Страница контактов
@app.route('/contact')
def contacts():
    # Здесь можно добавить логику для отображения контактной информации, формы обратной связи и т. д.
    return render_template('contact.html')

# Страница "О нас"
@app.route('/about')
def about():
    # Здесь можно добавить логику для отображения информации о компании, истории, команде и т. д.
    return render_template('about.html')

# Добавление товаровц
@app.route('/create', methods=['POST','GET'])
def create():
    if request.method == "POST":
        title = request.form['title']
        price = request.form['price']
        
        item = Item(title=title, price=price)
        
        try:
            db.session.add(item)
            db.session.commit(item)
            return redirect('/')
        except:
            return "Получилась Ошибка"
            
    else:
        return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)
