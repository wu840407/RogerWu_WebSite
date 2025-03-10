from django.contrib import admin
from django.urls import path, include
from .views import home, cv_view, google_login_redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),       # allauth 的完整帳號功能（包含 Google 登入）
    path('blog/', include('blog.urls')),
    path('knowledgebase/', include('knowledgebase.urls')),
    path('forum/', include('forum.urls')),
    path('cv/', cv_view, name='cv'),
    path('', home, name='home'),
    path('google-login/', google_login_redirect, name='google-login-direct'),
]
