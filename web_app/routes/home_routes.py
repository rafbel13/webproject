
from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    return render_template("home.html")

@home_routes.route("/hiking")
def hiking():
    return render_template("hiking.html")

@home_routes.route("/gear")
def gear():
    return render_template("gear.html")

@home_routes.route("/logistics")
def logistics():
    return render_template("logistics.html")
