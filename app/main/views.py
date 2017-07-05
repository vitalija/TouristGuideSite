from flask import request, render_template, redirect, url_for
from config import Config
from .emails import send_email, send_email_copy
from .forms import ContactForm
from . import main


@main.route('/tours/<region>/<destination>') 
def tours(region, destination):
    location ='base/tours/' + region + "/" + destination + ".html"
    return render_template('tour_description.html', location = location)

@main.route('/', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
def index():
    form = ContactForm()    

    if request.method == 'POST':
        if form.validate() == False:
            #flash_errors(form)
            return render_template('index.html', form=form, redirect="contactme")
        else:            
            #Message Data
            contact_name = form.userName.data
            contact_email = form.userEmail.data
            msg_subject = form.msgSubject.data
            msg_text = form.msgText.data
            
            # send message to site owner
            send_email([Config.MAIL_RECEIVER], contact_name, contact_email, msg_subject, msg_text)      
            # send email to contacting person 
            send_email_copy(contact_name, contact_email, msg_subject, msg_text)  
                 
            # clean the form
            form.userName = ''
            form.userEmail = ''
            form.userPhone = ''
            form.msgSubject = ''
            form.msgText = ''
            return redirect(url_for('main.message_sent'))      
              
    elif request.method == 'GET':
        return render_template('index.html', form=form)