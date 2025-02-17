# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # 儲存新使用者
            messages.success(request, "註冊成功！您現在可以登入了。")
            return redirect("login")  # 註冊成功後導向登入頁面
    else:
        form = RegistrationForm()
    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # 從表單取出驗證過的使用者
            login(request, user)  # 執行登入
            messages.success(request, f"歡迎回來，{user.username}！")
            return redirect("post_list")  # 登入成功後導向部落格首頁（根據需求修改）
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "您已成功登出。")
    return redirect("login")
