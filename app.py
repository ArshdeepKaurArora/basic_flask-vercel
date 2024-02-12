from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'
