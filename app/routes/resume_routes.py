from flask import Blueprint, render_template, request, session
import os

from app.services.resume_parser import parse_resume
from app.services.nlp_engine import calculate_similarity

resume_bp = Blueprint("resume", __name__)

UPLOAD_FOLDER = "uploads/resumes"
HR_RESUME = "uploads/hr_resume/hr.pdf"

@resume_bp.route("/upload", methods=["GET","POST"])
def upload_resume():

    role = session.get("role")

    if request.method == "POST":

        file = request.files["resume"]

        if role == "hr":

            file.save(HR_RESUME)

            return "HR Resume uploaded successfully"

        elif role == "student":

            student_path = os.path.join(UPLOAD_FOLDER, file.filename)

            file.save(student_path)

            hr_text = parse_resume(HR_RESUME)

            candidates = []

            for filename in os.listdir(UPLOAD_FOLDER):

                if not filename.endswith(".pdf"):
                    continue

                path = os.path.join(UPLOAD_FOLDER, filename)

                student_text = parse_resume(path)

                score = calculate_similarity(student_text, hr_text)

                candidates.append({
                    "name": filename,
                    "score": round(score,2)
                })

            ranked = sorted(candidates, key=lambda x: x["score"], reverse=True)

            top_candidate = ranked[0] if ranked else None

            return render_template(
                "results.html",
                filename=file.filename,
                ranked=ranked,
                top_candidate=top_candidate,
                score=top_candidate["score"] if top_candidate else 0
            )

    return render_template("upload.html")