from django.http import HttpResponse
from django.template import loader
from .models import Car


def cars(request):
    car_list = Car.objects.filter(operational=True).order_by('name').values('id', 'slug', 'name')
    cars_by_speed = Car.objects.filter(maximum_speed__gt=0).order_by('-maximum_speed').values('id', 'slug', 'name',
                                                                                              'maximum_speed')
    template = loader.get_template('all_cars.html')
    context = {
        'all_cars': car_list,
        'speed_cars': cars_by_speed,
    }
    return HttpResponse(template.render(context, request))


def details(request, slug):
    car = Car.objects.get(slug=slug)
    template = loader.get_template('details.html')
    context = {
        'car': car,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
