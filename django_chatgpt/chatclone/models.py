from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Chat(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	message = models.TextField()
	response = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.user.username}:{self.message}'


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class upload_file(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)



class UploadFileForm(forms.Form):
    file = forms.FileField()