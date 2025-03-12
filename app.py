from flask import Flask, render_template

app = Flask(__name__)


def get_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

@app.route('/')
def index():  # put application's code here
    return render_template("index.html")
@app.route('/home/')
def home():
    return render_template("home.html")

@app.route('/forms/')
def forms():
    return render_template("forms.html")

@app.route('/jobs/')
def jobs():
    return render_template("jobs.html")


if __name__ == '__main__':
    app.run()
