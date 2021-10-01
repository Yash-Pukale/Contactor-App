import flask

app = flask.Flask(__name__)

@app.route("/test", methods=["GET"])
def test():
    return flask.jsonify(ok=True)



if __name__ == '__main__':
    app.run(debug=True, port=10000)
