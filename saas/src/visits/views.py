from django.shortcuts import render
from .models import pagevisit
# Create your views here.
def home_page_view(request):
    qs = pagevisit.objects.all()
    page_qs = pagevisit.objects.filter(path=request.path)
    path = request.path
    context = {
       "queryset":qs.count(),
       "path" : path,
       "qs" : page_qs.count()
    }
  

    pagevisit.objects.create(path=request.path)

    return render(request, 'home.html',context)