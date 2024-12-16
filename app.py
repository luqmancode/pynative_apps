from flask import Flask, jsonify
from models.sqlite_sql import Database, DATABASE


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello from Flask"


@app.route('/api/v1/info')
def get_version_v1():
    version_info = "v1"
    with Database(DATABASE) as db:
        cursor_rec = db.execute("SELECT build_date, version, links, methods "
                                  "FROM api_release WHERE version=:version",
                                  params={"version": version_info}
                       )
        version_info = cursor_rec.fetchall()
    return jsonify({"version_info": version_info}), 200



if __name__ == "__main__":
    # with Database(DATABASE) as db:
    #    db.execute("CREATE TABLE IF NOT EXISTS api_release(build_date "
    #               "datetime, version varchar(30) primary key, links "
    #               "varchar2(30), methods varchar2(30))")
    app.run(host="0.0.0.0", port=5000, debug=True)
