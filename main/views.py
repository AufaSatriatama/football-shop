from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'appName': 'Football Shop',
        'npm' : '2406426321',
        'name': 'Aufa Daffa Satriatama',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)