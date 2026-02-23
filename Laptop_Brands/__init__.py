from sys import path

from django.urls import include

from Project.Laptop_Brands import admin


[
    'Mainpage',          # ← listed here
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Mainpage.urls')),   # ← and referenced here
]