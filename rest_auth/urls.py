from django.conf.urls import url
from rest_auth import views

from rest_framework.routers import DefaultRouter




from rest_auth.views import (
    LoginView, LogoutView, UserDetailsView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView, RegisterUserBasic
)

urlpatterns = [
    # URLs that do not require a session or valid token
    # url(r'^armprime/$', views.index),
    # url(r'^unit_properties/$', views.getUnitFbiUsingId),

    url(r'^password/reset/$', PasswordResetView.as_view(),
        name='rest_password_reset'),
    url(r'^password/reset/confirm/$', PasswordResetConfirmView.as_view(),
        name='rest_password_reset_confirm'),
    url(r'^login/$', LoginView.as_view(), name='rest_login'),

    url(r'^logout/$', LogoutView.as_view(), name='rest_logout'),
    url(r'^user/$', UserDetailsView.as_view(), name='rest_user_details'),
    url(r'^password/change/$', PasswordChangeView.as_view(),
        name='rest_password_change'),
    url(r'^user/$', UserDetailsView.as_view(), name='rest_user_details'),
    url(r'^register-basic/$', RegisterUserBasic.as_view(), name='rest_user_details'),
]