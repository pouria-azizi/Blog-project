import datetime

from .models import Category


def shared_context(request):
    return {
        'year': datetime.datetime.today().year,
        'category_list': Category.objects.values_list('name'),

    }
