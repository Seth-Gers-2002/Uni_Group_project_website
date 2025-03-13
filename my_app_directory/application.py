from flask import Flask, render_template
from config import Config
from models import db
from routes import inventory_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    flask db init
    flask db migrate - m "Initial migration."
    flask db upgrade

app.register_blueprint(inventory_bp)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
