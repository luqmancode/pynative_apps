"""Use case module logic for useres"""
from models.users import list_all_users, create_single_user, user_list, delete_user

def list_users():
    return list_all_users()


def list_user(id_: str):
    return user_list(id_)


def add_user(user):
    return create_single_user(user)


def remove_user(id_: str):
    return delete_user(id_)
