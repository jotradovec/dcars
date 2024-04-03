from django.http import HttpResponse
from django.template import loader
from .models import Car


def cars(request):
    car_list = Car.objects.all().values('id', 'name')
    template = loader.get_template('all_cars.html')
    context = {
        'mycars': car_list,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    car = Car.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'car': car,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
