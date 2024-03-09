from django.urls import path
from .views import say_hello, RegistrationApiView, LoginApiView, ListUsersApiView

urlpatterns = [
    path('hello/', say_hello, name='say_hello'),
    path('regis/', RegistrationApiView.as_view()),
    path('login/', LoginApiView.as_view()),

    path('users/', ListUsersApiView.as_view())
]
