from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/static/<path:path>')
def css_file():
    return render_template("hw1.css")

@app.route('/img/<path:path>')
def image(path):
    return app.send_static_file(path)

@app.route('/')
def html_file():
    return render_template("hw1.html")

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)