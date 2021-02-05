from django.urls import path, reverse_lazy
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
urlpatterns = [
    path('login/', LoginView.as_view(template_name='user/login.html', authentication_form= AuthenticationForm), name='login_url'),
    path('logout/', LogoutView.as_view(template_name='user/login.html',next_page=reverse_lazy('index_url') ), name='logout_url', ),
    #path('logout/', LogoutView.as_view(), name='logout_url'),
    path('CreateUser/', CreateUserView.as_view(),name='create_user_url'),
]