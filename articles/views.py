from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required


from django.shortcuts import render
from .models import Article
from .form import ArticleForm


def article_search_view(request):
    query_dict = request.GET

    try:
        query = int(query_dict.get("q"))
    except (TypeError, ValueError):
        query = None

    article_obj = None
    if query is not None:
        try:
            article_obj = Article.objects.get(id=query)
        except Article.DoesNotExist:
            article_obj = None

    context = {
        "object": article_obj,
    }
    return render(request, "articles/search.html", context=context)



# Create your views here.
def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object":  article_obj, 
    }
    return render(request, "articles/detail.html", context=context)

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)

    context = {
        "form": form
    }
    if form.is_valid():
        articles_obj = form.save()
        context['form'] = ArticleForm()
        # title = form.cleaned_data.get("title")
        # content = form.cleaned_data.get("content")
        # articles_obj = Article.objects.create(title=title, content=content)
        context["object"] = articles_obj
        context["created"] = True
    return render(request, "articles/create.html", context=context)