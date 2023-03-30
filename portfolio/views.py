from django.shortcuts import render
from portfolio.models import Portfolio_Info, Images

def portfolio(request):
    portfolio_info = Portfolio_Info.objects.all().last()
    image = Images.objects.all().last()

    return render(request, "portfolio/portfolio_details.html", context={"portfolio_info": portfolio_info, "image": image })
    
