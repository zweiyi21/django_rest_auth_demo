from django.urls import path
from .views import SignupView, SigninView, MeView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='sign-up'),
    path('signin/', SigninView.as_view(), name='sign-in'),
    path('me/', MeView.as_view(), name='me'),
]