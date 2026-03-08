from flask import Blueprint,request,jsonify
from app.services.nlp_engine import calculate_similarity

api_bp = Blueprint("api",__name__)

@api_bp.route("/api/login",methods=["POST"])
def api_login():

    data=request.json

    if data["username"]=="yuvaraj" and data["password"]=="12345":

        return jsonify({"status":"success"})

    return jsonify({"status":"failed"})


@api_bp.route("/api/upload_resume",methods=["POST"])
def upload_resume():

    file=request.files["resume"]

    file.save("uploads/resumes/"+file.filename)

    return jsonify({"message":"resume uploaded"})


@api_bp.route("/api/parse_resume")
def parse_resume():

    return jsonify({"message":"resume parsed"})


@api_bp.route("/api/score_resume",methods=["POST"])
def score_resume():

    data=request.json

    resume=data["resume"]

    job=data["job_description"]

    score=calculate_similarity(resume,job)

    return jsonify({"score":score})


@api_bp.route("/api/shortlist")
def shortlist():

    return jsonify({
        "candidates":[
            "Candidate A",
            "Candidate B",
            "Candidate C"
        ]
    })