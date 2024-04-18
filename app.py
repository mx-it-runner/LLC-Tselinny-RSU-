from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
