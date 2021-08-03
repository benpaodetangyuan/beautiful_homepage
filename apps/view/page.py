from flask_restful import Resource, fields, marshal
from flask import Blueprint, jsonify
from apps.model.home import HomePage

page_bp = Blueprint('page',__name__)
homepage_field = {
    'page': {
        'video': fields.String,
        'image': fields.String,
        'title': fields.String,
        'text': fields.String
    }
}


class HomePageResourse(Resource):
    def get(self):
        page = HomePage.query.filter_by().all()
        page = marshal(page, homepage_field)
        return jsonify(page)
