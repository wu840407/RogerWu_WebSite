# accounts/forms.py
from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 如果表單中有 username 欄位，就移除它
        if 'username' in self.fields:
            del self.fields['username']

    def save(self, request):
        user = super().save(request)
        # 這裡可加其他保存後的處理
        return user
    
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("email", "password1", "password2")