from app import app, db, mail
from flask import render_template
from flask import request, redirect, url_for, flash
from flask_mail_sendgrid import MailSendGrid
from flask_mail import Message
from .models import Projects, User
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    myprojects = Projects.query.filter_by(show="True").filter_by(top="True").all()
    moreprojects = Projects.query.filter_by(show="True").filter_by(top="False").all()
    allprojects = Projects.query.filter_by(show="True").all()
    return render_template(
        "index.html",
        myprojects=myprojects,
        moreprojects=moreprojects,
        allprojects=allprojects,
    )


@app.route("/contact", methods=["POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        msg = Message(
            "Portfolio Message Recieved - " + name,
            sender=email,
            recipients=["jl.conatus@gmail.com"],
        )
        fullmsg = (
            "Name:" + str(name) + "<br>" +
            "Email:" + str(email) + "<br>" +
            "Phone:" + str(phone) + "<br>" +
            "Message:" + str(message)
        )
        msg.html = fullmsg
        mail.send(msg)
    return redirect("index")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("projects"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user)
        next_page = request.args.get("projects")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("projects")
        return redirect(next_page)
    return render_template("login.html", form=form)


@app.route("/projects")
@login_required
def projects():
    projects = Projects.query.all()
    return render_template("projects.html", projects=projects)


@app.route("/project/add", methods=["POST"])
@login_required
def project_add():
    if request.method == "POST":
        newproject = Projects(
            name=request.form["name"],
            idname=request.form["idname"],
            card_text=request.form["card_text"],
            modal_body=request.form["modal_body"],
            modal_short=request.form["modal_short"],
            modal_tech=request.form["modal_tech"],
            preview=request.form["preview"],
            github=request.form["github"],
            show=request.form["show"],
            top=request.form["top"],
            images=request.form["images"],
        )
        db.session.add(newproject)
        db.session.commit()
    return redirect("projects")


@app.route("/projects/delete/<id>", methods=["GET"])
@login_required
def project_delete(id):
    if request.method == "GET":
        project = Projects.query.filter_by(id=id).first()
        db.session.delete(project)
        db.session.commit()
    return redirect("projects")


@app.route("/projects/edit/<id>", methods=["GET", "POST"])
@login_required
def edit_project(id):
    project = Projects.query.filter_by(id=id).first()
    if request.method == "GET":
        return render_template("edit_project.html", project=project)

    project.idname = request.form["idname"]
    project.card_text = request.form["card_text"]
    project.modal_body = request.form["modal_body"]
    project.modal_short = request.form["modal_short"]
    project.modal_tech = request.form["modal_tech"]
    project.preview = request.form["preview"]
    project.github = request.form["github"]
    project.show = request.form["show"]
    project.top = request.form["top"]
    project.images = request.form["images"]
    project.imagesmore = request.form["imagesmore"]

    db.session.commit()
    return redirect(url_for("projects"))


@app.route("/projects/list")
@login_required
def projects_list():
    projects = Projects.query.all()
    return render_template("project_list.html", projects=projects)
