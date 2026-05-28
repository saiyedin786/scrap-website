from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ferrous")
def ferrous_scrap():
    return render_template("ferrous.html")

@app.route("/nonferrous")
def nonferrous_scrap():
    return render_template("nonferrous.html")

@app.route("/achievements")
def achievements():
    return render_template("achievements.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)