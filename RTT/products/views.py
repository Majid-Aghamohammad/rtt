import logging
#django import
from django.conf import settings
from django_filters import rest_framework as filters

#DRF import 
from rest_framework.generics import (CreateAPIView, ListAPIView, DestroyAPIView)
from rest_framework import  status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny

#Internal import
from user.models import User
from products.models import Product            
from products.tasks import celery_send_email_task
from products.serializers import ProductSerializer, InputProductSerializer, ProductListSerializer

# Create your views here.


# Pagination Config
DEFAULT_PAGE = 5


# Loger settings
logger = logging.getLogger(__name__)

class CustomPageNumberPagination(LimitOffsetPagination):
    """Custom pagination class for admin and other users"""
    def get_page_size(self, request):
        if (request.user.is_admin == True):
            return 1000
        else:
            return 100
    



class ProductCreateAPIView(CreateAPIView):
    permission_classes = [IsAdminUser]
    """submit New Products"""
    serializer_class = InputProductSerializer
    def post(self, request, *args, **kwargs):
        # print (request.user.id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        #If you want send email must Feth CRITICAL_DATA in setting or comment tow line blow 
        superuser_emails = User.objects.filter(is_superuser=True).values_list('email', flat=True)
        celery_send_email_task(superuser_emails, serializer.data, request.user)

        return Response(data =serializer.data, status=status.HTTP_200_OK) 

class ProductListAPIView(ListAPIView):
    """ """
    permission_classes = [AllowAny]
    pagination_class = CustomPageNumberPagination
    serializer_class = ProductListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    #TODO: You can change your Filed base on you have need
    filterset_fields = ('category', 'title', )
    def get_queryset(self):
        return Product.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



class ProductRemoveAPIView(DestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
    def delete(self, request,):
            Product.objects.filter(sold_number=0).delete()
            return Response (status= status.HTTP_204_NO_CONTENT)


#TODO:Develop Category class for showing category title and id
class CategoryListAPIView(ListAPIView):
    # permission_classes = [AllowAny]
    # serializer_class = CategorySerializer

    # def get_queryset(self):
    #     return Category.objects.all()

    # def get(self, request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)
    pass 







































