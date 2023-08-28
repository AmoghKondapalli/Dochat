from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat
from .models import upload_file, UploadFileForm
from django.utils import timezone
from .ingest import main_ingest
from .func import proc
import os
# from .constants import getsum

def chatbot(request):
	chats = Chat.objects.filter(user=request.user)
	if request.method=='POST':
		mymodel = upload_file.objects.filter(user=request.user).first()
		if mymodel:
			file_url = mymodel.file.path
			folder_path = os.path.dirname(file_url)
		main_ingest(folder_path+'/db',folder_path)
		message = request.POST.get('message')
		response = proc(message,folder_path+'/db',folder_path)
		# message = request.POST.get('message')
		# response = '# elo there matey'
		chat = Chat(user = request.user, message = message, response = response, created_at = timezone.now)
		chat.save()
		return JsonResponse({'message':message, 'response':response})
	return render(request, 'chatbot.html',{'chats':chats})


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(request, username=username,password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('upload')
		else:
			error_message = 'Invalid user'
			return render(request, 'login.html',{'error_message':error_message})
	else:
		return render(request, 'login.html')

def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password2 == password1:
			try:
				user = User.objects.create_user(username, email, password1)
				user.save()
				auth.login(request, user)
				return redirect('upload')
			except:
				error_message = 'Error creating account'
				return render(request, 'register.html',{'error_message':error_message})
		else:
			error_message = 'Password does not match'
			return render(request, 'register.html',{'error_message':error_message})
	return render(request, 'register.html')

def logout(request):
	auth.logout(request)
	return redirect('login')

def upload(request):
	if request.method == 'POST':
		# if 'file' not in request.FILES:
		# 	error_message = 'No file match'
		# 	return render(request, 'upload.html',{'error_message':error_message})
		form = UploadFileForm(request.POST, request.FILES)
		# if file['file'] == '':
		# 	error_message = 'No selected files'
		# 	return render(request, 'upload.html',{'error_message':error_message})
		if form.is_valid():
			mm = upload_file(user = request.user)
			mm.file = form.cleaned_data['file']
			mm.save()
			mymodels = upload_file.objects.filter(user=request.user)
			uploaded_files = []
			for mymodel in mymodels:
				if os.path.exists(mymodel.file.path):
					uploaded_files.append(mymodel.file.name)
			success = 'Successfulyl Uploaded'
			#return redirect('upload')
			return render(request, 'upload.html',{'success':success,'uploaded_files':uploaded_files})
	else:
		return render(request, 'upload.html')

def delete(request):
	mymodel = upload_file.objects.filter(user=request.user).first()
	if mymodel:
		file_url = mymodel.file.path
		folder_path = os.path.dirname(file_url)
	print(folder_path)
	os.system(f"rm -r {folder_path}/")
	return redirect('upload')