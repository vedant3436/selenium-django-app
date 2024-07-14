from django.shortcuts import render, HttpResponse
from django.core.mail import EmailMultiAlternatives, get_connection

# Create your views here.

from django.core.mail import EmailMessage, get_connection
from django.conf import settings

def send_email(request):  
   if request.method == "POST": 
       with get_connection(  
           host=settings.EMAIL_HOST, 
     port=settings.EMAIL_PORT,  
     username=settings.EMAIL_HOST_USER, 
     password=settings.EMAIL_HOST_PASSWORD, 
     use_tls=settings.EMAIL_USE_TLS  
       ) as connection:  
           subject = 'Subject'
           email_from = settings.EMAIL_HOST_USER  
           recipient_list = ["receiver's mail"] 
           message = '''
Email Content
                    '''
           # screenshot_path = f"{settings.BASE_DIR}/screenshot.png"
           mail = EmailMultiAlternatives(subject, message, email_from, recipient_list, cc=['cc if any'],connection=connection)  #use EmailMessage instead of EmailMultiAlternatives if you dont want to use cc
           # mail.attach_file("screenshot.png", screenshot_path) option, only use if you want to add attachment
           mail.send()

   return render(request, 'home.html')