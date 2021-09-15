from django.shortcuts import redirect
from django.http import HttpResponse

from time import sleep


class ContactUSRedirectMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response


	def __call__(self, request):
		response = self.get_response(request)
		if request.path.startswith('/contact_us') and request.method == 'POST':
			# response = self.get_response(request)
			HttpResponse('Your message has been sent! Thanks for you request!')
			sleep(3)
			return redirect('index')
		else:
			return response