from flask import Blueprint, jsonify, abort, request
from use_cases.ads import add_ad, list_ad, list_ads


ad_app = Blueprint('ads', __name__, url_prefix='/api/v1')


@ad_app.route('/ads', methods=['POST'])
def create_ad():
    if (not request.json or not 'username' in request.json or
        not 'header' in request.json or not 'industry' in request.json):
        abort(400)
    add_ad(request.json)
    return jsonify({"status": "Successfully added"}), 201


@ad_app.route('/ads/<id_>', methods=['GET'])
def get_ad(id_):
    ad_info = list_ad(id_)
    if ad_info:
        return jsonify({"ad_info": ad_info}), 200
    return abort(404)


@ad_app.route('/ads', methods=['GET'])
def get_ads():
    return jsonify({"ads": list_ads()}), 200
