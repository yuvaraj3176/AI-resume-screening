from flask import Flask
import sqlite3

from app.routes.auth_routes import auth_bp
from app.routes.resume_routes import resume_bp
from app.routes.api_routes import api_bp
from app.routes.chatbot_routes import chatbot_bp

def create_app():

    app = Flask(
        __name__,
        template_folder="app/templates",
        static_folder="app/static"
    )

    app.config['SECRET_KEY'] = "resume_secret"
    app.config['UPLOAD_FOLDER'] = "uploads/resumes"

    app.register_blueprint(auth_bp)
    app.register_blueprint(resume_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(chatbot_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)