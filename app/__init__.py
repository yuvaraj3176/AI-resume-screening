from flask import Flask
from app.routes.auth_routes import auth_bp
from app.routes.resume_routes import resume_bp
from app.routes.api_routes import api_bp

def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = "resume_secret"
    app.config['UPLOAD_FOLDER'] = "uploads/resumes"

    app.register_blueprint(auth_bp)
    app.register_blueprint(resume_bp)
    app.register_blueprint(api_bp)

    return app