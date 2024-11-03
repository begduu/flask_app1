from flask import Flask, render_template

app = Flask(__name__)

@app.route("/example")
def index():
    return render_template("index.html")






if __name__ == "__main__":
    app.run(debug = True, host = 1.1.1.1, port = 5001)