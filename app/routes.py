from app import app
from flask import render_template
from flask import Flask, request, redirect, url_for
from flask_mail_sendgrid import MailSendGrid
from flask_mail import Message

app.config['MAIL_SENDGRID_API_KEY'] = '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'
mail = MailSendGrid(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

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
