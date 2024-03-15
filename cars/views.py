from django.http import HttpResponse
from django.template import loader
from .models import Car


def cars(request):
    mycars = Car.objects.all().values()
    template = loader.get_template('all_cars.html')
    context = {
        'mycars': mycars,
    }
    return HttpResponse(template.render(context, request))
