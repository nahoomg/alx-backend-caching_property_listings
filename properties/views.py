from django.http import JsonResponse
from .utils import get_all_properties
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def property_list(request):
    properties = get_all_properties()
    return JsonResponse({
        "data": properties
    })
