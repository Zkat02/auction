from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser

from .models import *
from .serializers import *
from rest_framework import generics, viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

# views.py
from rest_framework import status
from rest_framework.response import Response
from djoser.views import UserViewSet
from .models import Users


class UsersViewSet(UserViewSet):
    def perform_create(self, serializer):
        user = serializer.save()
        Users.objects.create(user=user, country='', city='', address='', phone_number='')


# @api_view(['GET', 'POST'])
# def user_view(request):
#     if request.method == 'GET':
#         # список объектов
#     elif request.method == 'POST':
#         # создание нового объекта
#     else:
#         pass
#         # некорректный метод



# def my_view(request):
#     try:
#         data = {'message': 'Hello, world!'}
#         response = JsonResponse(data)
#         print(response)
#         response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
#         return response
#     except Exception as e:
#         logger.exception("An error occurred: %s", e)


class ProductsViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer



    permission_classes = (IsAdminUser)


class UsersViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class ProductsViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class VendorsViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Vendors.objects.all()
    serializer_class = VendorsSerializer

class AuctionsViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Auctions.objects.all()
    serializer_class = AuctionsSerializer

class BidsViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Bids.objects.all()
    serializer_class = BidsSerializer
