from django import forms
from django.contrib.auth.models import User
from account.models import Profile
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm

# USER LOGIN
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True, 'class':'form-control',}))
    password = forms.CharField(
        label= ("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class':'form-control',}),
    )

class PassResetForm(PasswordResetForm):
    email = forms.EmailField(
        label='Email',
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", 'class':'form-control'}),
    )

# USER REGISTRATION
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs = {
                'class' : 'form-control',
        }
    ))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(
        attrs = {
                'class' : 'form-control',
        }
    ))

    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
        attrs = {
            'class' : 'form-control',
        }
    ))

    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs = {
            'class' : 'form-control',
        }
    ))

    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs = {
            'class' : 'form-control',
        }
    ))

    email = forms.CharField(label='Email Address', widget=forms.TextInput(
        attrs = {
            'class' : 'form-control',
            'type':'email',
            'placeholder' : 'name@example.com',
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    # Check for matching passwords
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don\'t match")
        return cd['password2']
    
    # django will check for username being unique but we have to do email ourself
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("Email already exist!")
        return data
    


# USER EDIT
class UserEditForm(forms.ModelForm):

    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
        attrs = {
            'class' : 'form-control',
        }
    ))

    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs = {
            'class' : 'form-control',
        }
    ))

    email = forms.CharField(label='Email Address', widget=forms.TextInput(
        attrs = {
            'class' : 'form-control',
            'type':'email',
            'placeholder' : 'name@example.com',
        }
    ))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.exclude(id=self.instance.id).filter(email=data).exists():
            raise forms.ValidationError("Email already exist!")
        return data


# PROFILE EDIT
class ProfileEditForm(forms.ModelForm):

    photo = forms.FileField(
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'type':'file',
            }
        )
    )

    date_of_birth = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control',
            }
        )
    )
    
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']