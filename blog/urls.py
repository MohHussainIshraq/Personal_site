from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('blog/', views.blog, name="blog_article"),
    path('blog/', views.blog, name="blog_article"),
    path('search/', views.search, name="search_articles")
]