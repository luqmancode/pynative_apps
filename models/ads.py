from datetime import datetime

from models.sqlite_sql import Database, DATABASE


def create_ad(ad):
    with Database(DATABASE) as db:
        query = ("INSERT INTO advertisements(username, header, "
                 "industry, content, date_created) VALUES(:username, "
                 ":header, :industry, :content, :date_created)")
        params = (ad.get('username'),
                  ad.get('header'),
                  ad.get('industry'),
                  ad.get('content'),
                  datetime.now().isoformat())
        db.execute(query, params)


def get_ads():
    with Database(DATABASE) as db:
        query = "SELECT * FROM advertisements;"
        cur_ads = db.execute(query)
        return cur_ads.fetchall()


def get_ad(id_):
    with Database(DATABASE) as db:
        query = "SELECT * FROM advertisements WHERE id=:id;"
        params = (id_,)
        cur_ad = db.execute(query, params)
        return cur_ad.fetchone()

