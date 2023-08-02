from django.urls import path 
from users.views import register_page, login_page, profile, log_out
urlpatterns = [
    path('register/', register_page, name="register"),
    path('login/', login_page, name="login"),
    path('profile/', profile, name="profile"),
    path('log_out/', log_out, name="log_out"),
]
app_name = 'users'