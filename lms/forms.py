from django import forms
from django.contrib.auth.models import User
from lms.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password','first_name','last_name')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'fadeIn second'}),
            'email': forms.TextInput(attrs={'class': 'fadeIn third'}),
            'password': forms.PasswordInput(attrs={'class': 'fadeIn third'}),
            'first_name': forms.TextInput(attrs={'class': 'fadeIn second'}),
            'last_name': forms.TextInput(attrs={'class': 'fadeIn second'}),

        }


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('institute_name', 'phone_no')
        widgets = {
            'institute_name': forms.TextInput(attrs={'class': 'fadeIn third'}),
            'phone_no': forms.TextInput(attrs={'class': 'fadeIn third'}),
        }
from lms.models import Instructor

class UserForm1(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password','first_name','last_name')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'fadeIn second'}),
            'email': forms.TextInput(attrs={'class': 'fadeIn third'}),
            'password': forms.PasswordInput(attrs={'class': 'fadeIn third'}),
            'first_name': forms.TextInput(attrs={'class': 'fadeIn second'}),
            'last_name': forms.TextInput(attrs={'class': 'fadeIn second'}),

        }
class UserProfileInfoForm1(forms.ModelForm):
    class Meta():
        model = Instructor
        fields = ('institute_name', 'phone_no')
        widgets = {
            'institute_name': forms.TextInput(attrs={'class': 'fadeIn third'}),
            'phone_no': forms.TextInput(attrs={'class': 'fadeIn third'}),
        }


from lms.models import courseforms

class course(forms.ModelForm):
    class Meta():
        model = courseforms
        fields =('instructor','title', 'bio')


        widgets ={

            'title': forms.TextInput(attrs={'class':'fadeIn third'}),
            'bio': forms.TextInput(attrs={'class':'fadeIn third'}),

        }