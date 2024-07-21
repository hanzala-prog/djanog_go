from django.shortcuts import render, redirect
from .models import Article
from .form import ArticleForm
from django.contrib.auth.decorators import login_required

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

def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj, 
    }
    return render(request, "articles/detail.html", context=context)

@login_required
def article_create_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            article_obj = form.save()
            return redirect('article_detail', id=article_obj.id)  # Redirect to the article detail page
    else:
        form = ArticleForm()

    context = {
        "form": form
    }
    return render(request, "articles/create.html", context=context)
