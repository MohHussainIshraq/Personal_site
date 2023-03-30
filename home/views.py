import imp
from django.shortcuts import render
from blog.models import Article
from home.models import(Services, About, Portfolio,
Skill,Contact_us, Message,
Blog, Footer, Counters,
Testimonial, Sub_title)

def home(request):
    articles = Article.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Message.objects.create(name=name, email=email, subject=subject, message=message)

    services = Services.objects.all()
    about = About.objects.all().last()
    portfolio = Portfolio.objects.all()
    skill = Skill.objects.all()
    contact = Contact_us.objects.all().last()
    blog = Blog.objects.all()
    footer = Footer.objects.all().last()
    counter = Counters.objects.all().last()
    testimonial = Testimonial.objects.all().last()
    sub_title = Sub_title.objects.all().last()
    
    return render(request, "home/index.html", context={
        "services": services,
        "about": about,
        "portfolio": portfolio,
        "skill": skill,
        "contact": contact,
        "blog": blog,
        "footer": footer,
        "counter": counter,
        "testimo": testimonial,
        "sub_title": sub_title,
        "articles": articles
        })
