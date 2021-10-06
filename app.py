import flask
from models import *
from utils import JSONEncoder, dictify_document

app = flask.Flask(__name__)
app.json_encoder = JSONEncoder

app.config.from_pyfile('config.py')
db.init_app(app)


@app.route("/test", methods=["GET"])
def test():
    users = [dictify_document(k) for k in User.objects()]
    return flask.jsonify(ok=True, users=users)


if __name__ == '__main__':
    app.run(debug=True, port=10000)
