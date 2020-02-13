from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    out = "changes from features-2"
    return out


if __name__ == '__main__':
    app.run()
