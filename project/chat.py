from flask import Blueprint
from . import db
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Chat
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from flask import Flask, render_template
from project import socketio
from json import dumps
import jsonify
import ast

chat = Blueprint('chat', __name__)


@chat.route('/chat')
def sessions():
    chat = Chat.query.filter_by(user = current_user.id)
    serialize = []
    for item in chat:
        serialize.append({ 'id': item.id,'name': item.name,'text'  : item.text})
    return serialize

@chat.route('/admin/chats/<ids>')
def admin_sessions(ids):
    chat = Chat.query.filter_by(user = ids)
    serialize = []
    for item in chat:
        serialize.append({ 'id': item.id,'name': item.name,'text'  : item.text})
        item.aread = 1
        db.session.commit()

    return render_template('adminchat.html', chats = serialize , ids= ids)

@chat.route('/admin/chatsupdate/<ids>')
def chatsupdate(ids):
    chat = Chat.query.filter_by(user = ids)
    serialize = []
    for item in chat:
        serialize.append({ 'id': item.id,'name': item.name,'text'  : item.text})
    return serialize

@chat.route('/admin/chats')
def chats():
    chat = Chat.query.all()
    serialize = {}
    for item in chat:
        user = User.query.get(item.user)
        if not (item.user in serialize):
            if item.aread == 0:
                serialize[item.user] = {'id': item.id, 'name': user.name , 'unread': 1}
            else:
                serialize[item.user] = {'id': item.id, 'name': user.name, 'unread': 0}
        else:
            if item.aread == 0:
                serialize[item.user]['unread'] = serialize[item.user]['unread'] + 1
        print(serialize)
    return render_template('chats.html', chats = serialize)

@chat.route('/chat/send', methods=['POST'])
@login_required
def chat_add_post():
    dict_str = request.data.decode("UTF-8")
    mydata = ast.literal_eval(dict_str)

    text = mydata['text']
    name = mydata['name']
    new_chat = Chat(name = name, text=text , user= current_user.id, read= 1 , aread = 0)

    # add the new user to the database
    db.session.add(new_chat)
    db.session.commit()
    chat = Chat.query.filter_by(user = current_user.id)
    serialize = []
    for item in chat:
        serialize.append({ 'id': item.id,'name': item.name,'text'  : item.text})
    return serialize


@chat.route('/admin/chat/send', methods=['POST'])
@login_required
def chat_admin_add_post():
    dict_str = request.data.decode("UTF-8")
    mydata = ast.literal_eval(dict_str)

    text = mydata['text']
    ids = int(mydata['ids'])
    new_chat = Chat(name = 'ادمین', text=text , user= ids, read= 0 , aread = 1)

    # add the new user to the database
    db.session.add(new_chat)
    db.session.commit()
    chat = Chat.query.filter_by(user = current_user.id)
    serialize = []
    for item in chat:
        serialize.append({ 'id': item.id,'name': item.name,'text'  : item.text})
    return serialize
    