from django.core.mail import send_mail
from celery import shared_task
import time

@shared_task
def celery_send_email_task(email,products_info, user_info):
    #CRITICAL_DATA#
    #Your Email Sender Address
    sender_email_address =''
    resiver_email_address = email
    # resiver_email_address.append(email)
    email_subject="products submitions"
    email_body_text = "Hi we have new production on webservice. \n"
    email_body = { 'message' :email_body_text, 'new_product': products_info, 'user_creator':user_info} 
    send_mail(email_subject, email_body, sender_email_address, resiver_email_address, fail_silently=False,)
    return 'celery task Done!'


