from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kylie'}
    players = [
        {
            'player': {'username': 'John'},
            'body': 'George drives me crazy!'
        },
        {
            'player': {'username': 'Susan'},
            'body': 'Hayley for prime minister'
        }
    ]
    return render_template('index.html', title='Cosy Couch Survivor', user=user, players=players)

# adding new navigation links
@app.route('/orders')
def orders():
    return render_template('orders.html', title='Cosy Couch Survivor')

@app.route('/menu')
def menu():
    items = [
        { 'item': 'Hot Chips',
          'price': 4.00,
          'delivery': 'Yes'},
        { 'item': 'Burger',
          'price': 8.00,
          'delivery': 'Yes'},
        { 'item': 'Fish of the day',
          'price': 12.00,
          'delivery': 'No'}
    ]
        
    return render_template('menu.html', items=items)

@app.route('/bet')
def bet():
    user = {'username': 'Kylie'}
    how_to='This is how to bet'
    return render_template('bet.html', user=user, how_to=how_to)