from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
# Create your views here.
class EmailValidationView(View):
  def get(self, request):
      data=json.loads(request.body)
      email = data['email']

      if not validate_email(email):
          return JsonResponse({'email_error':'Email is invalid'}, status=400)
      if User.objects.filter(email=email).exists():
          return JsonResponse({'email_error':'Sorry, email already in use. Choose another'}, status=409)
      return JsonResponse({'email_valid': True})

class UsernameValidationView(View):
  def get(self, request):
      data=json.loads(request.body)
      username = data['username']

      if not str(username).isalnum():
          return JsonResponse({'username_error':'username should only contain alphanunmeric characters'}, status=400)
      if User.objects.filter(username=username).exists():
          return JsonResponse({'username_error':'username already in use. Choose another'}, status=409)
      return JsonResponse({'username_valid': True})

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        
        # GET USER DATA
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        return render(request, 'authentication/register.html')
