from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
@app.route("/home", methods=['GET','POST'])
@app.route("/onsurvey", methods=['GET','POST'])
def home():
    return render_template('onsurvey.html')

@app.route("/endsurvey", methods=['GET','POST'])
def endsurvey():
    return render_template('endsurvey.html')

@app.route("/makesurvey", methods = ['GET','POST'])
def makesurvey():
    error = None
    return render_template('makesurvey.html')

def makesurvey

if __name__ == "__main__":
    app.run(debug = True, port = 8080)