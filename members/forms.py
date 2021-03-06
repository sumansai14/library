from django import forms
from django.contrib.models import User
from django.forms import Modelform
from members.models import Member

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
    exclude = ('user')


username = forms.CharField(label=(u'User Name'))
password = forms.CharField(label=(u'Password'),widget=forms.PasswordInput(render_value=false))
password1 = forms.CharField(label='Password_verify'),widget = forms.PasswordInput(render_value=false)
email = forms.EmailField(label='Email Address')

def clean_username(self):
	username = self.cleaned_data['username']
	try:
		User.objects.get(username=username)
	except User.DoesNotExist:
		return username
	raise forms.ValidationError('the username alredy exits, please try another one')

def clean_password(self):
	password = self.cleaned_data['password']
	password1 = self.cleaned_data['password1']
	if(password != password1):
		raise forms.ValidationError("the passwords do not match")
	return password
