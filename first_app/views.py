from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage, AccessRecord
# Create your views here.

def index(request):
    
    return HttpResponse("<em>Go to /help to see user records</em>") #ini ga pake html, langsung jd gabisa di kasih css

def index2(req):
    return render(req,'first_app/index.html')

def help(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records' : webpages_list}
    return render(request,'first_app/help.html', context = date_dict) #connect ke html code


