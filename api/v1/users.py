from use_cases.users import list_users, add_user, list_user, remove_user
from flask import Blueprint, jsonify, abort, request


user_app = Blueprint('users', __name__, url_prefix='/api/v1')

@user_app.route("/users", methods=['GET'])
def get_users():
    """Listing users"""
    return jsonify(list_users()), 200


@user_app.route("/users/<id_>", methods=['GET'])
def get_user(id_: str):
    """Get single user details"""
    user_info = list_user(id_)
    if user_info:
        return jsonify(user_info), 200
    return abort(404)


@user_app.route("/users", methods=['POST'])
def create_user():
    """Create a new user"""
    if (not request.json or not 'username' in request.json or not 'email' in
        request.json or not 'password' in request.json):
        abort(400)
    add_user(request.json)
    return jsonify({"message": "Successfully added"}), 201


@user_app.route('/users/<id_>', methods=['DELETE'])
def delete_user(id_: str):
    remove_user(id_)
    return jsonify({"message": "Successfully deleted"}), 200
