from flask import Flask, render_template
from config import Config
from models import db
from routes import hazard_management_bp, inventory_bp, job_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = "your_secret_key"  # Needed for flash messages and CSRF protection

    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Register blueprints
    app.register_blueprint(hazard_management_bp)
    app.register_blueprint(inventory_bp)
    app.register_blueprint(job_bp)


    @app.route('/')
    def index():
        # Render the home page; pass an empty 'form' to avoid undefined errors in templates
        return render_template("home.html", form={})

    return app

if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(debug=True)
