from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from .views import *

from djoser.views import (
    TokenCreateView, TokenDestroyView,
)

from rest_framework.routers import DefaultRouter


router = routers.SimpleRouter()
router.register(r'vegetableslist', ProductsViewSet)
router.register(r'auctions', AuctionsViewSet)
router.register(r'vendors', VendorsViewSet)
router.register(r'users', UsersViewSet)
router.register(r'bids', BidsViewSet)
router.register(r'users', UsersViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # http://127.0.0.1:8000/course/<pk>
    # re_path('api/my_view/', my_view),
    path(r'api/auth/', include('djoser.urls')),
    re_path(r'api/auth/', include('djoser.urls.authtoken')),

    # path('auth/token/create/', TokenCreateView.as_view(), name='token_create'),
    # path('auth/token/destroy/', TokenDestroyView.as_view(), name='token_destroy'),
    # path('auth/register/', RegistrationView.as_view(), name='register'),
    # path('auth/delete/', UserDeleteView.as_view(), name='user_delete'),
    # path('auth/password/reset/', PasswordResetView.as_view(), name='password_reset'),
    # path('auth/password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('auth/password/set/', SetPasswordView.as_view(), name='set_password'),

]

router = DefaultRouter()
router.register(r'users', UsersViewSet)

urlpatterns = [
]
