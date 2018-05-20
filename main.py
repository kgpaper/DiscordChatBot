from flask import Flask, render_template

application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@application.route("/createvote")
def create_vote():
    return render_template('vote.html')


if __name__ == "__main__":
    application.run(host='0.0.0.0')