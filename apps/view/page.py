from flask_restful import Resource, fields, marshal
from flask import Blueprint, jsonify
from apps.model.home import Home

page_bp = Blueprint('page',__name__)
home_field = {
    'page': {
        'video': fields.String,
        'image': fields.String,
        'title': fields.String,
        'text': fields.String
    }
}


class HomeResourse(Resource):
    def get(self):
        page = Home.query.filter_by().all()
        page = marshal(page, home_field)
        return jsonify(page)
