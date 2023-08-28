from django.urls import path
from . import views

urlpatterns = [
	path('',views.login, name = 'login'),
	path('chatbot',views.chatbot, name = 'chatclone'),
	path('register',views.register, name = 'register'),
	path('logout',views.logout, name = 'logout'),
	path('upload',views.upload, name = 'upload'),
	path('delete', views.delete, name = 'delete')
]