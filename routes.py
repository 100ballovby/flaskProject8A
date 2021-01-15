''' маршрутизация сайта '''
from app import app  # импортирую переменную сайта
from flask import render_template  # рисует страницу


@app.route('/')
def main_page():
    return render_template('index.html', title='Главная страница!')


@app.route('/contacts')
def contact_page():
    return render_template('contacts.html')


@app.route('/gallery')
def gallery_page():
    return render_template('gallery.html')