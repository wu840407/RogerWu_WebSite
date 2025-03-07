"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myproject.views import home, cv_view

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URL
    path('admin/', admin.site.urls),
    
    # 使用 django-allauth 提供完整的登入/註冊功能（包含 Google 登入）
    path('accounts/', include('allauth.urls')),
    
    # 如果你還有自訂的帳戶相關 URL，請考慮用不同的前綴，避免衝突
    # path('custom_accounts/', include('accounts.urls')),
    
    path('blog/', include('blog.urls')),               # 部落格
    path('knowledgebase/', include('knowledgebase.urls')),  # 知識庫（例如 BTC、ADA介紹）
    path('forum/', include('forum.urls')),             # 討論區
    path('cv/', cv_view, name='cv'),                   # CV 頁面
    path('', home, name='home'),                       # 根目錄首頁
]
