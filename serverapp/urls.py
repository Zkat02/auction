from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from .views import *

from djoser.views import (
    TokenCreateView, TokenDestroyView,
)

from rest_framework.routers import DefaultRouter


router = routers.SimpleRouter()
router.register(r'vegetableslist', ProductViewSet)
router.register(r'auctions', AuctionViewSet)
router.register(r'vendors', VendorViewSet)
router.register(r'users', UserViewSet)
router.register(r'bids', BidViewSet)
# router.register(r'users', UsersViewSet)

# http://localhost:8000/api/auth/users/
# POST
# create user
# {
#     "username": "seconduser",
#     "password": "...",
#     "email": "sec@gmail.com",
# }
# returns:
# {
#     "username": "seconduser",
#     "email": "sec@gmail.com",
#     "id": 2
# }

# http://localhost:8000/api/auth/token/login/
# POST
# {
#     "username": "seconduser",
#     "password": "...",
# }
# return:
# {
#     "auth_token": "97f12b490ce118b45e2ecab02e472fee67a3bc0e"
# }

# for getting data from server need to give in headers auth token
# POST
# headers:
# +
# authorization Token 97f12b490ce118b45e2ecab02e472fee67a3bc0e

# for logout
# POST
# headers:
# +
# authorization Token 97f12b490ce118b45e2ecab02e472fee67a3bc0e


urlpatterns = [
    path('api/', include(router.urls)),
    path(r'api/auth/', include('djoser.urls')),
    re_path(r'api/auth/', include('djoser.urls.authtoken')),
]