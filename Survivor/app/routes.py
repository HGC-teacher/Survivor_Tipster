import csv
from app import app
from flask import Flask, render_template, request

def load_from_file(fname):
    # loads the contents from a given csv file
    contents = []
    with open(fname) as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            contents.append(row)
    return contents

@app.route('/')
@app.route('/index')
def index():
    comments = load_from_file('chat.csv')
    user = {'username': 'Kylie'}
    return render_template('index.html', title='Cosy Couch Survivor', user=user, comments=comments)

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

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/signup-received', methods = ["POST"])
def submit_sign_up():
    #print(request.form)
    #return ("Sign Up received")

    new_user = {}
    if request.method == "POST":
        new_user['name'] = request.form.get('name')
        new_user['pword'] = request.form.get('pword')
        new_user['domain'] = request.form.get('domain')

        return render_template('sign_up_received.html', new_user = new_user)