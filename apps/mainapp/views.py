from django.shortcuts import render

def index(request):
    return render(request, 'mainapp/index.html')

def about(request):
    return render(request, 'mainapp/about.html')

def blog(request):
    return render(request, 'mainapp/blog.html')

def contact(request):
    return render(request, 'mainapp/contact.html')

def services(request):
    return render(request, 'mainapp/services.html')

