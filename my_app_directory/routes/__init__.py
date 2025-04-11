from flask import Flask, render_template, session, redirect, url_for
from config import Config
from models import db, User
from routes.hazard_management import hazard_management_bp
from routes.inventory import inventory_bp
from routes.job_intake import job_intake_bp
from routes.auth import auth_bp
from routes.account import account_bp
from my_app_directory.routes.customer import customer_bp
from my_app_directory.routes.individual_cleaner import individual_bp
import access_control


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
    app.register_blueprint(job_intake_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(account_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(individual_bp)

    @app.route('/index')
    def index():
        return render_template("index.html")  # Dashboard for non-customers

    @app.route('/about_us')
    def about_us():
        return render_template("about_us.html")

    @app.route('/')
    def client_home():
        return render_template("client_home.html")

    @app.route('/login')
    def login():
        return render_template("login.html")

    @app.route('/base')
    def base():
        return render_template("base.html")

    # NEW: Landing route for role-based redirection
    @app.route('/landing', endpoint='landing')
    def landing():
        if 'user_id' not in session:
            return redirect(url_for('login'))
        user = User.query.get(session['user_id'])
        role_names = [ur.role.role_name.lower() for ur in user.roles] if user.roles else []
        if 'customer' in role_names:
            return redirect(url_for('client_home'))
        else:
            return redirect(url_for('index'))

    with app.test_request_context():
        print(app.url_map)

    return app


if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(debug=True)
