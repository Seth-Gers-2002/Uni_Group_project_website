from flask import Flask, render_template
from config import Config
from models import db
from routes.inventory import inventory_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(inventory_bp)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    # Initialize DB tables within an application context before starting the server
    with app.app_context():
        db.create_all()
    app.run(debug=True)
