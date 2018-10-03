from app import app
from flask import render_template
from flask import request, redirect, url_for
from flask_mail_sendgrid import MailSendGrid
from flask_mail import Message
from pf import Projects, db


app.config['MAIL_SENDGRID_API_KEY'] = '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'
mail = MailSendGrid(app)


@app.route('/')
@app.route('/index')
def index():
    myprojects = Projects.query.filter_by(show=True).all()
    return render_template('index.html', myprojects=myprojects)


@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        msg = Message("Portfolio Message Recieved - " + name, sender=email, recipients=['jl.conatus@gmail.com'])
        fullmsg = "Name:" + str(name) + "<br>" + "Email:" + str(email) + "<br>" + "Phone:" + str(phone) + "<br>" + "Message:" + str(message)
        msg.html = fullmsg
        mail.send(msg)
    return redirect('index')


@app.route('/projects')
def projects():
    myprojects = Projects.query.filter_by(show=True).all()
    return render_template('projects.html', myprojects=myprojects)


@app.route('/project/add', methods=['POST'])
def project_add():
    if request.method == 'POST':
        newproject = Projects(
        name=request.form['name'],
        card_text=request.form['card_text'],
        modal_body=request.form['modal_body'],
        modal_short=request.form['modal_short'],
        modal_tech=request.form['modal_tech'],
        show=True
        )
        db.session.add(newproject)
        db.session.commit()
    return redirect('projects')


@app.route('/projects/delete/<id>', methods=['GET'])
def project_delete(id):
    if request.method == 'GET':
        project = Projects.query.filter_by(id=id).first()
        db.session.delete(project)
        db.session.commit()
    return redirect('projects')
