from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
        'password_tooshort': "Please enter at least 8 digits for password"
    }

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if len(password1) < 8:
            raise forms.ValidationError(
                self.error_messages['password_tooshort'],
                code='password_tooshort',
            )
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )

        return password2
