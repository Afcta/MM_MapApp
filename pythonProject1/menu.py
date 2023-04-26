from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("map"))

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/culture")
def culture():
    return render_template("culture.html")

if __name__ == "__main__":
    app.run(debug=True)