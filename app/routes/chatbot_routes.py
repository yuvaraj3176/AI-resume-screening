from flask import Blueprint, request, jsonify
from app.services.resume_parser import parse_resume

chatbot_bp = Blueprint("chatbot", __name__)

@chatbot_bp.route("/api/chat", methods=["POST"])
def chat():

    data = request.json

    question = data["question"]

    response = "Candidate has skills related to Python and Machine Learning."

    return jsonify({"answer": response})