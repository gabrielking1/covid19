"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .models import Worlds, Country
from app.filters import CountryFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    """Renders the home page."""
    nice = Worlds.objects.all()

    condata = Country.objects.all()

    myfilter = CountryFilter(request.GET, queryset=condata)
        
        
    page = request.GET.get('page', 1)

    paginator = Paginator(myfilter.qs, 10)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'world':nice,
            'country':condata,
            'myfilter':myfilter,
            'page_obj':page_obj,
        }
    )

# def contact(request):
#     """Renders the contact page."""

#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         'app/mapa.html',
#         {
#             'title':'Contact',
#             'message':'Your contact page.',
#             'year':datetime.now().year,
#         }
#     )

# def about(request):
#     """Renders the about page."""
#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         'app/about.html',
#         {
#             'title':'About',
#             'message':'Your application description page.',
#             'year':datetime.now().year,
#         }
#     )
