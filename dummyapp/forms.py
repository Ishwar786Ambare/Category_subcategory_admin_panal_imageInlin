from django import forms
from .models import *
from django.conf import settings


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super(ProductForm, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        cleaned_data = super(ProductForm, self).clean()
        return cleaned_data

    class Media:
        # js = ('/static/customadmin/custom-admin-user.js',)
        js = (settings.STATIC_URL + 'custom-admin-user.js',)
