import django_filters 
from django import forms
from .models import Post
class PostFilter(django_filters.FilterSet):
    date_posted = django_filters.DateTimeFilter(widget= forms.DateInput(attrs={'type': 'date'}), lookup_expr='date__exact')
        
    class Meta:
        model = Post
        fields = ['date_posted']