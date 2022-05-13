from django.urls import path

from users.views import SignUpView, confirm_user_auth

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name="users_signup"),
    path('confirm-auth/', confirm_user_auth, name="confirm_auth"),
]
