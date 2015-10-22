
from __future__ import absolute_import
from proj.celery import app

@app.task(send_error_emails = True)
def just_print():
    print "Print from celery task"

@app.task(send_error_emails = True)
def add(x, y):
    return x + y

@app.task(send_error_emails = True)
def minus(x, y):
    return x - y

