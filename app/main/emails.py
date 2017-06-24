from flask_mail import Message, Mail
from config import Config


def send_email(recipients_list, contact_name, contact_email, msg_subject, msg_text):
    sender = Config.MAIL_USERNAME
    subject = "ElleJourney.com: You have been contacted by a visitor"
    msg = Message(subject, sender=sender, recipients=recipients_list)
    msg.body = "Message Sender: {}\n".format(contact_name) + \
               "Sender's Email: {}\n".format(contact_email) + \
               "Message Subject: {}\n".format(msg_subject) +\
               "\n{}".format(msg_text)           
    Mail().send(msg)
    
    
def send_email_copy(contact_name, contact_email, msg_subject, msg_text):
    sender = Config.MAIL_USERNAME
    subject = "ElleJourney.com: You have contacted us"
    msg = Message(subject, sender=sender, recipients=[contact_email])
    msg.body = "Dear {},\n".format(contact_name) + \
               "Thank you for contacting us! We will get back to you shortly.\n\n" + \
               "Best Regards,\nElleJourney Team\n\n" + \
               "Message Sender: {}\n".format(contact_name) + \
               "Sender's Email: {}\n".format(contact_email) + \
               "Message Subject: {}\n".format(msg_subject) +\
               "\n{}".format(msg_text)           
    Mail().send(msg)