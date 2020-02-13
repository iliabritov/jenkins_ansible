from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    out = "This is out from feature 1"
    return out


if __name__ == '__main__':
    app.run()
