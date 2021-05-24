from django.urls import path

from accounts import views

app_name = "account"


urlpatterns = [
    path('login/',views.login,name='login')
]
