from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", endpoint="index")
def index():
    res = render_template("index.html", title="Главная")
    return res


@app.route("/about/", endpoint="about")
def index():
    res = render_template("about.html", title="О нас")
    return res


if __name__ == "__main__":
    app.run(debug=True, port=8080)
