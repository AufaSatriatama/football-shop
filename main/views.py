from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'appName': 'Jual Jersey',
        'npm' : '2406426321',
        'name': 'Aufa Daffa Satriatama',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)

def show_dashboard(request):

    context = {
        'appName': 'Jual Jersey',
        'npm' : '2406426321',
        'name': 'Aufa Daffa Satriatama',
        'class': 'PBP B'
    }

    return render(request, "dashboard.html", context)