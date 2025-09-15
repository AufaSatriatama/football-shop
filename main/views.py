from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product

from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def show_main(request):
    jersey_list = Product.objects.all()

    context = {
        'appName': 'Jual Jersey',
        'npm' : '2406426321',
        'name': 'Aufa Daffa Satriatama',
        'class': 'PBP B',
        'jersey_list': jersey_list
    }

    return render(request, "main.html", context)

def add_jersey(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_jersey.html", context)


def show_dashboard(request):


    return render(request, "dashboard.html")

def show_jersey(request, id):
    jersey = get_object_or_404(Product, pk=id)

    context = {
        "jersey": jersey
    }

    return render(request, "jersey_detail.html", context)

def show_xml(request):
     jersey_list = Product.objects.all()
     xml_data = serializers.serialize("xml", jersey_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    jersey_list = Product.objects.all()
    json_data = serializers.serialize("json", jersey_list)
    return HttpResponse(json_data, content_type="application/json")

def show_json_by_id(request, jersey_id):
   try:
       jersey_item = Product.objects.get(pk=jersey_id)
       json_data = serializers.serialize("json", [jersey_item])
       return HttpResponse(json_data, content_type="application/json")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_xml_by_id(request, jersey_id):
   try:
       news_item = Product.objects.filter(pk=jersey_id)
       xml_data = serializers.serialize("xml", news_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)
   
