from django import forms
from django_filters import FilterSet, CharFilter, ChoiceFilter, ModelChoiceFilter, DateRangeFilter
from .models import Ads, Category

class AdsFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains', label='Поиск по названию')
    time_create = DateRangeFilter(field_name='time_create', label='Дата создания', lookup_expr='gte')
    category = ModelChoiceFilter(queryset=Category.objects.all(), label='Категории', to_field_name='name') 