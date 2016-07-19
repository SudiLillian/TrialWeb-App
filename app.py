from flask import Flask, render_template

from content_management import content_management

TOPIC_DICT = Content()

app = Flask(__name__)

# @ signifies a decorator - way to wrap a function and modifying its behavior
@app.route("/")
def homepage():
	return render_template("main.html")

@app.route("/dashboard/ ")	
def homepage():
	return render_template("dashboard.html", TOPIC_DICT - TOPIC_DICT)
	

if __name__ == "__main__":
    app.run(debug=True)	