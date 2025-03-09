# accounts/forms.py
from django import forms
from allauth.account.forms import SignupForm
from .models import CustomUser


class CustomSignupForm(SignupForm):
    email = forms.EmailField(required=True)

    def save(self, request):
        user = super().save(request)
        # 如果需要，可在這裡做額外處理，例如設定使用者屬性
        class Meta:
            model = CustomUser
            fields = ("email", "password1", "password2")
        return user