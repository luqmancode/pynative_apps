from flask import Flask, jsonify, make_response
from flasgger import Swagger

from models.sqlite_sql import Database, DATABASE
from api.v1.users import user_app
from api.v1.ads import ad_app



app = Flask(__name__)

swagger = Swagger(app, template={
    "info": {
        "title": "Pynative Flask API",
        "description": "An example API using Flask and Swagger",
        "version": "1.0.0"
    }
})



app.register_blueprint(user_app)
app.register_blueprint(ad_app)


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


@app.errorhandler(404)
def resource_not_found(error):
    return make_response(jsonify({"error": "Resource not found!"}), 404)


if __name__ == "__main__":
    # with Database(DATABASE) as db:
    #    db.execute("CREATE TABLE IF NOT EXISTS api_release(build_date "
    #               "datetime, version varchar(30) primary key, links "
    #               "varchar2(30), methods varchar2(30))")
    app.run(host="0.0.0.0", port=5000, debug=True)
