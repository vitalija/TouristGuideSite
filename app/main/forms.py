from flask import flash
from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, validators

# flashing errors: function is useful for debugging purposes
def flash_errors(form):
    errors = ""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))
            

 
class ContactForm(FlaskForm):
    userName = TextField("Name:",  [validators.Required("This field is obligatory. Enter your name")])
    userEmail = TextField("E-mail:",  [validators.Required("This field is obligatory. Enter your e-mail."), 
                                     validators.Email("Enter a valid e-mail address")])
    msgSubject = TextField("Subject:",  [validators.Required("This field is obligatory. Enter message subject")])
    msgText = TextAreaField("Message:",  [validators.Required("This field id obligatory. Enter message text")])