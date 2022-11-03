from django.urls import path
from products.views import ProductCreateAPIView, ProductListAPIView, ProductRemoveAPIView


urlpatterns = [
    # Products URLs...
    path('submin/', ProductCreateAPIView.as_view(),  name='submit'),
    path('list/', ProductListAPIView.as_view(),  name='list_productions'),
    path('delete/', ProductRemoveAPIView.as_view(),  name='delete_zero_sold_number')

]

