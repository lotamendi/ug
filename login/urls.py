from django.urls import path
from login.views import LoginFormView, LogoutView

urlpatterns = [
    path('', LoginFormView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout")
]
