from django.shortcuts import render


def home(request):
    return render(request, 'Mainpage.html')

# individual brand pages

def acer(request):
    return render(request, 'acer.html')


def asus(request):
    return render(request, 'asus.html')


def dell(request):
    return render(request, 'dell.html')


def hp(request):
    return render(request, 'hp.html')


def lenovo(request):
    return render(request, 'lenovo.html')


def sony(request):
    return render(request, 'sony.html')
