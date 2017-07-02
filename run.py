"""
Kieran R Prasch
"""


from flask import Flask, request, send_from_directory
from flask import request, render_template, url_for


app = Flask(__name__)


# url_for('static', filename='style.css')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
