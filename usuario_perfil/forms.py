from django import forms


class UserRegistrationForm(forms.Form):

    usuario = forms.CharField(
        required=False,
        label='usuario',
        max_length=100,
    )
    email = forms.CharField(
        required=True,
        label='email',
    )
    gender = forms.CharField(
        required=True,
        label='gender',
        max_length=9
    )
    password = forms.CharField(
        required=True,
        label='password',
        widget=forms.PasswordInput(),
    )
    confirmPassword = forms.CharField(
        required=True,
        label='confirmPassword',
        widget=forms.PasswordInput(),
    )