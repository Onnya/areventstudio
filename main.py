from flask import Flask, render_template, make_response, jsonify


app = Flask(__name__)


@app.route("/")
def index():
    params = {}
    params["title"] = "AreventStudio"
    return render_template("index.html", **params)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def main():
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()