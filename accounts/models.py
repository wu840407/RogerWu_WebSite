from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        建立並儲存一個普通用戶，使用 email 作為唯一識別欄位。
        """
        if not email:
            raise ValueError('使用者必須提供電子郵件地址')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        建立並儲存一個超級用戶。
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('超級用戶必須有 is_staff=True。')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('超級用戶必須有 is_superuser=True。')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None  
    email = models.EmailField(unique=True, verbose_name="電子郵件地址")
    first_name = models.CharField(max_length=30, blank=True, verbose_name="名字")
    last_name = models.CharField(max_length=30, blank=True, verbose_name="姓氏")
    is_staff = models.BooleanField(default=False, verbose_name="是否是工作人員")
    is_active = models.BooleanField(default=True, verbose_name="是否啟用")
    date_joined = models.DateTimeField(default=timezone.now, verbose_name="加入日期")
    # 若有其他欄位，也可以在此添加

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # 若需要其他必填欄位，可在此加入欄位名稱

    def __str__(self):
        return self.email
