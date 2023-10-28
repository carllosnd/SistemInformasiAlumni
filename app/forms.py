from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from .models import UserProfile

class RegisterUserForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'password1', 'password2') 

	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'
  
class ReplyForm(forms.Form):
    reply = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']
