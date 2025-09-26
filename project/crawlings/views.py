from django.shortcuts import render, redirect
from .models import Crawlings
from .scraper import fetch_visible_comments

# Create your views here.
def index(request):
    crawlings = []
    if request.method == 'POST':
        company_name = request.POST.get('company_name')

        if company_name:
            comments = fetch_visible_comments(company_name)
            
            for comment in comments:
                Crawlings.objects.create(company_name=company_name, stock_code=0, comments=comment)
            crawlings = Crawlings.objects.filter(company_name=company_name)
    context = {
        'crawlings': crawlings,
    }
    return render(request, 'crawlings/index.html', context)

def delete(request, crawling_pk):
    crawling = Crawlings.objects.get(pk=crawling_pk)
    company_name = crawling.company_name
    crawling.delete()

    return redirect('crawlings:index')

def crawl_and_save(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        if company_name:
            comments = fetch_visible_comments(company_name)
            for comment in comments:
                Crawlings.objects.create(
                    company_name=company_name,
                    stock_code=0,
                    comments=comment
                )
    return redirect('crawlings:index')