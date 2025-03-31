from flask import Flask, render_template
from config import Config
from models import db
from routes import hazard_management_bp, inventory_bp, job_bp, auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = "your_secret_key"  # Required for flash messages and CSRF protection

    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Register blueprints
    app.register_blueprint(hazard_management_bp)
    app.register_blueprint(inventory_bp)
    app.register_blueprint(job_bp)
    app.register_blueprint(auth_bp)

    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/about_us')
    def about_us():
        return render_template("about_us.html")

    @app.route('/client-home')
    def client_home():
        return render_template("client_home.html")
    @app.route('/login')
    def login():
        return render_template("login.html")

    @app.route('/base')
    def base():
        return render_template("base.html")

    return app

if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(debug=True)
