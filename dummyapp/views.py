from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.core import serializers
import json
from django.contrib.admin.views.decorators import staff_member_required
from dummyapp.models import Category, SubCategory


def getSubCategories(request):
    id = request.GET.get('id', '')
    cat = Category.objects.get(id=id)
    result = SubCategory.objects.filter(category=cat)
    data = serializers.serialize('json', result)
    print(data)
    return HttpResponse(data, content_type="application/json")

    # id = request.GET.get('id', '')
    # result = list(SubCategory.objects.filter(category_id=int(id)).values('id', 'name'))
    # return HttpResponse(json.dumps(result), content_type="application/json")


getSubCategories = staff_member_required(getSubCategories)
