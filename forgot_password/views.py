from django.shortcuts import render
import requests
import random
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from user_data.models import *
from login.models import *
from django.core.mail import send_mail
from django.contrib.auth.models import User
@csrf_exempt
def forgot_get_pass(request):
	response={}
	context={}
	print str(request.user)
	if request.method=="POST":
		try:
			response["success"]=True
			email=str(request.POST.get("email"))
			response["email"]=email
			try:
				user_row=user_data.objects.get(email=email)
				request.session['email']=email
				forgot_row=forgot_data.objects.get(user_id=user_row.user_id)
				setattr(forgot_row,'email',str(email))
				setattr(forgot_row,'flag',int(0))
				response["message"]="email id found"
				context["message"]="Enter the otp sent to your email id"
				otp=str(random.randint(1000,9999))
				print str(otp)
				setattr(forgot_row,'otp',int(otp))
				forgot_row.save()
				send_mail(
					"change password for code  nitrr",
					otp,
					'no-reply@codenitrr.com',
					[str(email)],
					fail_silently=False,
					)
				return render(request,"forget_ver_pass.html",context)
			except:
				response["message"]="email id not found"
				context["message"]="email id not found"
		except:
			response["success"]=False


		print str(response)
		return HttpResponse(str(response))
		

	else:
		return render(request,"forgot_change_pass.html")


@csrf_exempt
def forgot_ver_pass(request):
	context={}
	context["message"]="Enter the otp sent to your registerd email id"
	response={}
	if request.method=="POST":
		try:
			response["success"]=True
			otp=str(request.POST.get("otp"))
			email=str(request.session.get("email"))
			print str(email)
			forgot_row=forgot_data.objects.get(email=email)
			if otp==str(forgot_row.otp):
				setattr(forgot_row,'flag',int(1))
				forgot_row.save()
				return render(request,"change_password.html")
			else:
				context["message"]="Please enter correct otp"
				return render(request,"forget_ver_pass.html",context)
		except:
			response["success"]=False

		print str(response)
		return HttpResponse(str(response))

	else:
		return render(request,'forget_ver_pass.html',context)

@csrf_exempt
def change_password(request):
	response={}
	context={}
	if request.method=="POST":
		try:
			password=str(request.POST.get("pass"))
			print str(password)
			response["success"]=True
			email=str(request.session.get("email"))
			print str(email)
			user_row=user_data.objects.get(email=email)
			print str(user_row.user_id)
			forgot_row=forgot_data.objects.get(email=email)
			login_row=login_data.objects.get(user_id=str(user_row.user_id))
			u = User.objects.get(username=user_row.user_id)
			if forgot_row.flag==1:
				setattr(login_row,'password',str(password))
				u.set_password(str(password))
				u.save()
				response["message"]="password changed successfully"
				login_row.save()
				return render(request,'main.html',response)
			else:
				context["message"]="password not changed please re-enter detail"
				return render(request,'forgot_change_pass.html',context)
		except:
			response["success"]=False
		print str(response)
		return HttpResponse(str(response))

	else:
		return render(request,'change_password.html')









# Create your views here.
