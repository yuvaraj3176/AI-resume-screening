import os

class Config:

    SECRET_KEY = "resume_secret"

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    UPLOAD_FOLDER = os.path.join(BASE_DIR,"uploads/resumes")

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024