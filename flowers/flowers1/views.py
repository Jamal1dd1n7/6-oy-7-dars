from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.handlers.wsgi import WSGIRequest
from .models import Flower, Type1

def home(request: WSGIRequest):
    type1 = Type1.objects.all()
    flowers = Flower.objects.all()
    context = {
        'flowers': flowers,
        'types': type1,
        'title': 'Gullar'
    }
    return render(request, 'intex.html', context)

def flower_by_type(request: WSGIRequest, type1_id):
    flowers = get_list_or_404(Flower, type1_id=type1_id)
    type1 = get_object_or_404(Type1, pk=type1_id)
    context = {
        'flowers': flowers,
        "title": f"{type1.name}: barcha maqolalar!"
    }
    return render(request, 'index.html', context)

def flower_detail(request: WSGIRequest, flower_id):
    flower = get_object_or_404(Flower, id= flower_id)
    context = {
        'flower': flower,
        'title': flower.name
    }
    return render(request, 'index2.html', context)