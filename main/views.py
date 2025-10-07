from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product

from django.http import HttpResponse
from django.core import serializers

from django.utils.html import strip_tags
from django.http import HttpResponseRedirect, JsonResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Create your views here.

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        jersey_list = Product.objects.all()
    else:
        jersey_list = Product.objects.filter(user=request.user)

    context = {
        'appName': 'Jual Jersey',
        'npm' : '2406426321',
        'name': 'Aufa Daffa Satriatama',
        'class': 'PBP B',
        'jersey_list': jersey_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'username': request.user.username
    }

    return render(request, "main.html", context)

def add_jersey(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        jersey_entry = form.save(commit=False)
        jersey_entry.user = request.user
        jersey_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_jersey.html", context)

def show_dashboard(request):


    return render(request, "dashboard.html")

@login_required(login_url='/login')
def show_jersey(request, id):
    jersey = get_object_or_404(Product, pk=id)

    context = {
        "jersey": jersey
    }

    return render(request, "jersey_detail.html", context)

def show_json(request):
    jersey_list = Product.objects.all()
    data = []
    
    for jersey in jersey_list:
        # Handle created_at field that might not exist in model
        try:
            created_at = jersey.created_at.isoformat() if jersey.created_at else '2024-01-01T00:00:00'
        except AttributeError:
            created_at = '2024-01-01T00:00:00'
            
        data.append({
            'id': str(jersey.id),
            'name': jersey.name,
            'title': jersey.name,  # Keep title for backward compatibility
            'description': jersey.description,
            'price': float(jersey.price) if jersey.price else 0.0,
            'category': jersey.category,
            'thumbnail': jersey.thumbnail,
            'created_at': created_at,
            'is_featured': jersey.is_featured,
            'user_id': jersey.user_id,
            'user_username': jersey.user.username if jersey.user_id else None,
        })

    return JsonResponse(data, safe=False)

def show_xml(request):
     jersey_list = Product.objects.all()
     xml_data = serializers.serialize("xml", jersey_list)
     return HttpResponse(xml_data, content_type="application/xml")
   
def show_json_by_id(request, jersey_id):
    try:
        jersey = Product.objects.select_related('user').get(pk=jersey_id)
        data = {
            'id': str(jersey.id),
            'title': jersey.name,
            'description': jersey.description,
            'category': jersey.category,
            'thumbnail': jersey.thumbnail,
            'created_at': jersey.created_at.isoformat() if jersey.created_at else None,
            'is_featured': jersey.is_featured,
            'user_id': jersey.user_id,
            'user_username': jersey.user.username if jersey.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

def show_xml_by_id(request, jersey_id):
   try:
       jersey_item = Product.objects.filter(pk=jersey_id)
       xml_data = serializers.serialize("xml", jersey_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def register_ajax(request):

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            response_data = {
                "success": True,
                "redirect_url": reverse("main:show_main"),
                "message": "Your account has been successfully created!"
            }

            return JsonResponse(response_data)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            # Check if it's an AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                response_data = {
                    "success": True,
                    "redirect_url": reverse("main:show_main"),
                    "message": "Login successful!"
                }
                return JsonResponse(response_data)
            else:
                # Traditional form submission - redirect
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
        else:
            # Check if it's an AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({"success": False, "errors": form.errors}, status=400)
            else:
                # Traditional form submission - render with errors
                return render(request, 'login.html', {"form": form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {"form": form})


# def login_user(request):
#    if request.method == 'POST':
#       form = AuthenticationForm(data=request.POST)

#       if form.is_valid():
#         user = form.get_user()
#         login(request, user)
#         response = HttpResponseRedirect(reverse("main:show_main"))
#         response.set_cookie('last_login', str(datetime.datetime.now()))
#         return response

#    else:
#       form = AuthenticationForm(request)
#    context = {'form': form}
#    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def edit_jersey(request, id):
    jersey = get_object_or_404(Product, pk=id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=jersey)
        
        # Debug logging
        print(f"POST data: {request.POST}")
        print(f"Form errors: {form.errors}")
        print(f"Form is valid: {form.is_valid()}")
        
        if form.is_valid():
            form.save()
            
            # Check if it's an AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'Jersey updated successfully!'
                })
            else:
                return redirect('main:show_main')
        
        # For AJAX requests with form errors
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'errors': form.errors
            }, status=400)
    
    else:
        form = ProductForm(instance=jersey)

    context = {
        'form': form,
        'jersey': jersey
    }

    return render(request, "edit_jersey.html", context) 

def delete_jersey(request, id):
    jersey = get_object_or_404(Product, pk=id)
    jersey.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
def delete_jersey_ajax(request, id):
    if request.method == 'DELETE' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        jersey = get_object_or_404(Product, pk=id)
        jersey.delete()

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

@csrf_exempt
@require_POST
def add_jersey_entry_ajax(request):
    name = strip_tags(request.POST.get("name")) # strip HTML tags!
    description = strip_tags(request.POST.get("description")) # strip HTML tags!
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_jersey = Product(
        name=name, 
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_jersey.save()

    return HttpResponse(b"CREATED", status=201)

