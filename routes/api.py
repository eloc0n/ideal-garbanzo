import json
from flask import Blueprint, Response
from database.mock import cv

api = Blueprint("api", __name__)

@api.route("/contact")
def get_contact():
    return Response(
        cv.contact.model_dump_json(), mimetype="application/json"
    )


@api.route("/skills")
def get_skills():
    return Response(
        cv.skills.model_dump_json(), mimetype="application/json"
    )


@api.route("/languages")
def get_languages():
    return Response(
        cv.languages.model_dump_json(), mimetype="application/json"
    )


@api.route("/experience")
def get_experience():
    data = [exp.model_dump() for exp in cv.experience]
    return Response(json.dumps(data), mimetype="application/json")


@api.route("/education")
def get_education():
    return Response(
        [edu.model_dump_json() for edu in cv.education],
        mimetype="application/json"
    )


@api.route("/interests")
def get_interests():
    return Response(
        cv.interests.model_dump_json(), mimetype="application/json"
    )

@api.route("/cv")
def get_full_cv():
    return Response(cv.model_dump_json(), mimetype="application/json")