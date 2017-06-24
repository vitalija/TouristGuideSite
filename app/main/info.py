from flask import render_template
from . import main

@main.route('/message-sent')
def message_sent():
    return render_template('message_sent.html')