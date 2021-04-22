# URL Management Imports
from django.shortcuts import render, redirect
# Email Imports
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
from django.utils.html import strip_tags
# Site Messages Import
from django.contrib import messages

def genErrors(request, Emessages):
	for message in Emessages:
		messages.error(request, message)

def index(request):
	return render( request, 'main/index.html')

def about(request):
	return render( request, 'main/about.html')

def gethelp(request):
	return render( request, 'main/gethelp.html')

def contact(request):
	return render( request, 'main/contact.html')

def sendemail(request, id):

	if (int(id) == '1'):
		subject = 'Do-Not-Reply Look & See Contact Form Entry'
		html_message = loader.render_to_string(
			'main/contact_form_message.html',
			{
				'name': request.POST.get('name'),
				'email': request.POST.get('email'),
				'subject': request.POST.get('subject'),
				'message': request.POST.get('message'),
			}
		)
		plain_message = strip_tags(html_message)
		email_from = 'contact@lookandsee.app'
		recipient_list = [request.POST.get('email'), 'contact@lookandsee.app']
		send_mail( subject, plain_message, email_from, recipient_list, html_message=html_message)

		messages.success(request, 'Your Contact Form Entry has Been Recieved')
		return redirect("/contact")

	elif (int(id) == 2):
		subject = 'Do-Not-Reply Look & See Newsletter Notice'
		html_message = loader.render_to_string('main/newsletter_message.html')
		plain_message = strip_tags(html_message)
		email_from = 'contact@lookandsee.app'
		recipient_list = [request.POST.get('email'), 'contact@lookandsee.app']
		send_mail( subject, plain_message, email_from, recipient_list, html_message=html_message)
		print("Email Sent")
		messages.success(request, 'Thank you for Subscribing to Our Newsletter')
		return redirect("/#footer")
	
	else:
		print("Email Failure")
		return redirect("/")