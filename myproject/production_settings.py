# production_settings.py

from .settings import *  # 引入基礎設定

# 關閉 Debug 模式
DEBUG = True

# 設定允許存取的主機名稱，請填入你網站的網域或 IP
ALLOWED_HOSTS = ['rogerwu-website.onrender.com']

# 安全性設定
SECURE_SSL_REDIRECT = True          # 強制 HTTPS 連線
CSRF_COOKIE_SECURE = True            # CSRF cookie 僅透過 HTTPS 傳輸
SESSION_COOKIE_SECURE = True         # Session cookie 僅透過 HTTPS 傳輸
X_FRAME_OPTIONS = 'DENY'             # 防止網頁被嵌入到 frame 或 iframe 中
SECURE_HSTS_SECONDS = 31536000       # 強制 HTTP 嚴格傳輸安全（HSTS），設定 1 年
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# 靜態檔案管理：指定 collectstatic 指令收集的目錄
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
