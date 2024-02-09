from flask import Blueprint,render_template


sed = Blueprint("sed",__name__,static_folder="static",template_folder="templates")

@sed.route("/home")
@sed.route("/")# this overrides the shiet in app.py file
def home():
    return render_template("index.html")

@sed.route("/test")
def test():
    return "blueprint works"