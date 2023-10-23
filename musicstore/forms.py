from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import http.client
import json

#User = get_user_model

class NewUserForm(UserCreationForm):
    print("In side new user form")
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField(
        label = "Password",
        widget=forms.PasswordInput(
            attrs=
            {
                "class": "forms-control",
                "id":"user-password"
            }
        )
    )
    password2 = forms.CharField(
        label = "Confirm password",
        widget=forms.PasswordInput(
            attrs=
            {
                "class": "forms-control",
                "id":"user-confirm-password"
            }
        )
    )
    def is_valid(self):
        return True
    def clean_username(self):
        username = self.cleaned_data['username']
        qs = User.objects.filter(username__iexact=username)
        if  qs.exists():
            raise forms.ValidationError("Invalid user name. Pick another")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(username__iexact=email)
        if  qs.exists():
            raise forms.ValidationError("Email already exists")
        return email

class ListViewForm(forms.Form):
    
    def is_valid(self):
        return True
    name = "Alan Walker"
    def connect_genius(self) :
        #print("In side connect_genius")
        conn=http.client.HTTPSConnection("genius-song-lyrics1.p.rapidapi.com")

        #genius key
        headers = {
            'X-RapidAPI-Key': 'a6ff79bbd5msh926c1900c3403bfp162aeajsnd9dd3338b4e5',
            'X-RapidAPI-Host': 'genius-song-lyrics1.p.rapidapi.com'
        }
        def name_to_url_string(name):
            new_name = ''
            for c in name:
                if c != " ":
                    new_name += c
                else:
                    new_name += '%20'
            return new_name
        print(self.name)
        conn.request("GET","/search?q="+name_to_url_string(self.name), headers=headers)
        res=conn.getresponse()

        if res.status <= 200 :
            data = res.read()
            res_dict = json.loads(data.decode('utf-8'))
        else:
            res_dict={}
            print(res.status)

        conn.close()
        return res_dict




