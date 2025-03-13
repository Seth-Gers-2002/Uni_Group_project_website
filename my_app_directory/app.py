from flask import Flask, render_template
from config import Config
from models import db
from routes import hazard_management_bp, inventory_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Register blueprints
    app.register_blueprint(hazard_management_bp)
    app.register_blueprint(inventory_bp)

    @app.route('/')
    def index():
        # Renders the home/landing page
        return render_template("index.html")

    return app

if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(debug=True)
