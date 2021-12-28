from django.forms.fields import DateField
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import( PasswordChangeForm, UserCreationForm , 
UserChangeForm ,AuthenticationForm ,SetPasswordForm, UsernameField , PasswordResetForm)
from django.forms import TextInput, fields , EmailInput, widgets
from django.contrib.auth import password_validation
from django.utils.translation import gettext , gettext_lazy as _

from .models import (
    Profile,
    Bank,
    Card,
Adhar_card , 
Pan_card,
PaymentMethod,
Transaction
)

class RegistrationFormUser(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password' , 'class':'form-control','placeholder':'Enter the  Password '}),
        help_text=password_validation.password_validators_help_text_html(),
        )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password' , 'class':'form-control' , 'placeholder':'Confirm Password Again'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
        )
    class Meta:
        model=User
        fields=('username' , 'first_name' , 'last_name' , 'email')
        labels={'email':'Email'}
       
        widgets = {
        'username':TextInput(attrs={'class':'form-control','placeholder':'Enter the Username','required':'required'}),
        'first_name':TextInput(attrs={'class':'form-control','placeholder':'Enter the First Name','required':'required'}),
        'last_name':TextInput(attrs={'class':'form-control','placeholder':'Enter the Last Name','required':'required'}),
        'email':EmailInput(attrs={'class':'form-control', 'placeholder':'Enter the Email', 'required':'required'})
        
        }

class LoginuserForm(AuthenticationForm):
     username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True ,'class':'form-control','placeholder':'Enter the Username', 'required':'required'}))
     password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control' ,'placeholder':'Enter the password', 'required':'required' }),
    )





class  MypasswordchangeForm(PasswordChangeForm):
        old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True , 'class':'form-control' ,'placeholder':'Enter the Old password', 'required':'required' }),
        )
        new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control' ,'placeholder':'Enter the New password', 'required':'required'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
        )
        new_password2 = forms.CharField(
        label=_("New password (Again)"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control' ,'placeholder':'New password (Again)', 'required':'required'}),
        )

class Usersetpasswordform(SetPasswordForm): 
        new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control' ,'placeholder':'Enter the New password', 'required':'required'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
        )
        new_password2 = forms.CharField(
        label=_("New  Confirm password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control' ,'placeholder':'Confirm password ', 'required':'required'}),
        )
       
class ImageForm(forms.ModelForm):
  class Meta:
    model=Adhar_card
    fields=('forent_photo' , 'back_photo')


class PanImageForm(forms.ModelForm):
  class Meta:
    model=Pan_card
    fields=['forent_pan_image']






class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('first_name' , 'last_name' , 'birthday' , 'city','address','state')
 
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the first name', 'required':'required'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the  last name', 'required':'required'}),
            'birthday':forms.SelectDateWidget(years=range(1980 , 2050) ,attrs={'class':'form-control', 'placeholder':'Enter the birthday', 'required':'required'}),
            'city':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the city', 'required':'required'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the address', 'required':'required'}),
            'state':forms.Select(attrs={'class':'form-control', 'placeholder':'Enter the state', 'required':'required'}),
            
        }

class Email_Check(PasswordResetForm):
     email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email' ,'class':'form-control', 'placeholder':'Enter the Email', 'required':'required'})
    )

class TransactionForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields=('transaction_type' , 'category' , 'amount')
 
        widgets={
            'transaction_type':forms.Select(attrs={'class':'form-control', 'placeholder':'Enter the Transaction Type', 'required':'required'}),
            'category':forms.Select(attrs={'class':'form-control', 'placeholder':'Enter the category', 'required':'required'}),
            'amount':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter the amount', 'required':'required'}),
           
        }