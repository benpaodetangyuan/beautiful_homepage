from flask_restful import Resource, fields, reqparse, marshal
from flask import Blueprint, redirect, url_for, jsonify
from apps.model import db
from apps.model.user import User
user_bp = Blueprint('user', __name__)

user_field = {'user': {
        'username': fields.String,
        'password': fields.String
    }
}


def init_user():
    username = 'xxx'
    password = '000000'
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
