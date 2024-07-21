"""
To render html pages
"""

from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article



def home_view(request, *args, **kwargs):
    Article_obj = Article.objects.get(id=2)
    obj_queryset = Article.objects.all()
    context = {
        'Article_obj': Article_obj,
        'obj_queryset': obj_queryset,
        'title':  Article_obj.title,
        'content': Article_obj.content,
        'id': Article_obj.id
    }
    html_string = render_to_string('home.html', context=context)
    return HttpResponse(html_string)