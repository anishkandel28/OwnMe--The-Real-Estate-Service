# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mmglfamx3n927*93$ks#r)h%*a(@))vb7*=2q$&z(=6@q&*ghj'

DEBUG = False

ALLOWED_HOSTS = ['http://127.0.0.1:8000/']

# Email Config example gmail
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'aayaansharma100@gmail.com'
EMAIL_HOST_PASSWORD = 'Aayaan100#'
EMAIL_USE_TLS = True

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True