from flask import abort

from models.ads import create_ad, get_ad, get_ads
from models.users import user_list


def add_ad(ad):
    user = user_list(ad.get('username'))
    if not user:
        abort(404)
    return create_ad(ad)


def list_ad(id_):
    return get_ad(id_)


def list_ads():
    return get_ads()
