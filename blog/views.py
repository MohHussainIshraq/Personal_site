from django.shortcuts import render
from . models import Article
# Create your views here.

def blog(request):
    blog_details = Article.objects.all()
    recent_article = Article.objects.all()[:2]
    archive_article = Article.objects.all().order_by('-create_date',)
    tag = Article.objects.all()
    return render(request, "blog/blog_single.html", {"blog_details": blog_details,
    "recent_article": recent_article,
    "archive_article": archive_article,
    "tag": tag})



def search(request):
    invoke = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=invoke)

    return render(request, "blog/blog_single.html",  {"blog_details": articles })