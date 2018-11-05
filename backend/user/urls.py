from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    url(r'^account/login/?$', csrf_exempt(obtain_auth_token))
]
