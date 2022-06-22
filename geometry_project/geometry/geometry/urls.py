"""geometry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def rootRouteHandler(request):
    response = HttpResponse("<h1>Welcome to the internet</h1>")
    print('=-=-=-=-=-=-=-=')
    print(dir(request))
    print('--------------')
    print(dir(response))
    print('=-=-=-=-=-=-=-=')
    return response

def rectangle_area(request):
    try:
        height = int(request.GET.get("height"))
        width = int(request.GET.get("width"))
        area = height * width
        response = HttpResponse(f"<h1>answer: {area}</h2>")
    except:
        return HttpResponse(status=418)        
    return response

def rectangle_perimeter(request):
    try:
        height = int(request.GET.get("height"))
        width = int(request.GET.get("width"))
        perimeter = 2 * (height + width)
        response = HttpResponse(f"<h1>answer: {perimeter}</h2>")
    except:
        return HttpResponse(status=418)        
    return response

def circle_area(request):
    try:
        radius = int(request.GET.get("radius"))
        area = 3.1415 * radius ** 2
        response = HttpResponse(f"<h1>answer: {area}</h2>")
    except:
        response.status_code = 418
    return response

def circle_circumference(request):
    try:
        radius = int(request.GET.get("radius"))
        circumference = 2 * 3.1415 * radius
        response = HttpResponse(f"<h1>answer: {circumference}</h2>")
    except:
        return HttpResponse(status=418)        
    return response

def rectangle_area_url(response, height, width):
    try:
        perimeter = height * width
        response = HttpResponse(f"<h1>answer: {perimeter}</h2>")
    except:
        return HttpResponse(status=418)
    return response


def rectangle_perimeter_url(request, height, width):
    try:
        perimeter = 2 * (height + width)
        response = HttpResponse(f"<h1>answer: {perimeter}</h2>")
    except:
        return HttpResponse(status=418)
    return response


def circle_area_url(request, radius):
    try:
        area = 3.1415 * radius ** 2
        response = HttpResponse(f"<h1>answer: {area}</h2>")
    except:
        response.status_code = 418
    return response


def circle_circumference_url(request, radius):
    try:
        circumference = 2 * 3.1415 * radius
        response = HttpResponse(f"<h1>answer: {circumference}</h2>")
    except:
        return HttpResponse(status=418)
    return response

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", rootRouteHandler),

    # Query parameters
    path('rectangle/area/', rectangle_area),
    path('rectangle/perimeter/', rectangle_perimeter),
    path('circle/area/', circle_area),
    path('circle/circumference/', circle_circumference),

    # URL parameters
    path('rectangle/area/<int:height>/<int:width>/', rectangle_area_url),
    path('rectangle/perimeter/<int:height>/<int:width>/', rectangle_perimeter_url),
    path('circle/area/<int:radius>/', circle_area_url),
    path('circle/circumference/<int:radius>/', circle_circumference_url),
]
