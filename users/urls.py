from django.urls import path 
from users.views import register_page, login_page, profile
urlpatterns = [
    path('register.html', register_page, name="register"),
    path('login.html', login_page, name="login"),
    path('profile.html', profile, name="profile"),
]
app_name = 'users'