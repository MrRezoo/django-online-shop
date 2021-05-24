from django import forms
from accounts.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    confirmed_password = forms.CharField(label='confirmed password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'full_name', 'phone_number')

    def clean_confirmed_password(self):
        data = self.cleaned_data
        if data['password'] and data['confirmed_password'] and data['password'] != data['confirmed_password']:
            raise forms.ValidationError('password must match')
        return data['confirmed_password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'full_name', 'phone_number')

    def clean_password(self):
        return self.initial['password']
