from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
# Create your views here.

class UsernameValidationView(View):
  def get(self, request):
      data=json.loads(request.body)
      username = data['username']

      if not str(username).isalnum():
          return JsonResponse('username_error':'username should only contain alphanunmeric characters')

class RegistrationView(View):
  def get(self, request):
    return render(request, 'authentication/register.html')
