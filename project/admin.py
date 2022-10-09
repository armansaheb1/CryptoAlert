from flask import Blueprint
from . import db
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Exchange, Coin
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
import ast
admin = Blueprint('admin', __name__)

@admin.route('/admin/add')
def addcoin():
    ex = Exchange.query.all()
    coins = Coin.query.all()
    return render_template('CoinAdd.html', exchanges = ex, coins = coins)


@admin.route('/exchange-add', methods=['POST'])
@login_required
def exchange_add_post():
    exchange = request.form.get('name')
    new_exchange = Exchange(name = exchange)

    # add the new user to the database
    db.session.add(new_exchange)
    db.session.commit()
    return redirect(url_for('admin.addcoin'))

@admin.route('/coin-add', methods=['POST'])
@login_required
def coin_add_post():
    coin = request.form.get('name')
    
    dict_str = request.data.decode("UTF-8")
    mydata = ast.literal_eval(dict_str)
    
    if db.session.query(Coin).filter_by(name= mydata['name']).count():
        del_coin = Coin.query.filter_by(name= mydata['name']).first()
        db.session.delete(del_coin)
    new_coin = Coin(name= mydata['name'])
    for item in mydata['exchanges']:
        if not Exchange.query.get(int(item)) in new_coin.exchanges:
            new_coin.exchanges.append(Exchange.query.get(int(item)))
    # add the new user to the database
    db.session.add(new_coin)
    db.session.commit()
    return redirect(url_for('admin.addcoin'))

@admin.route('/exchange-delete', methods=['POST'])
@login_required
def exchange_delete_post():  
    dict_str = request.data.decode("UTF-8")
    mydata = ast.literal_eval(dict_str)
    ex = Exchange.query.filter_by(id=int(mydata['id'])).first()
    db.session.delete(ex)
    db.session.commit()
    return url_for('add')

@admin.route('/coin-delete', methods=['POST'])
@login_required
def coin_delete_post():  
    dict_str = request.data.decode("UTF-8")
    mydata = ast.literal_eval(dict_str)
    coin = Coin.query.filter_by(id=int(mydata['id'])).first()
    db.session.delete(coin)
    db.session.commit()
    return url_for('add')
