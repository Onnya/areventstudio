from flask import Flask, render_template, make_response, jsonify
import os


app = Flask(__name__)


@app.route("/")
def index():
    params = {}
    params["title"] = "AreventStudio"
    return render_template("index.html", **params)

@app.route("/projects")
def projects():
    params = {}
    params["title"] = "Our projects"
    return render_template("projects.html", **params)

@app.route("/applications")
def applications():
    params = {}
    params["title"] = "Your application"
    return render_template("applications.html", **params)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)