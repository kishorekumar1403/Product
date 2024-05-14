import django_filters     #pip install django-filter
from .models import *

class productFilter(django_filters.FilterSet):
    productName = django_filters.CharFilter(lookup_expr='contains')
    productCreatedDate = django_filters.CharFilter(field_name='productCreatedDate', lookup_expr='day')
    product_id = django_filters.CharFilter(field_name='id', lookup_expr='in')


class Meta:
    model = product
    fields = ['productName', 'productCreatedDate', 'product_id']