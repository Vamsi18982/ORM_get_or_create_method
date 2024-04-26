from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
def insert_topic(request):

    tn=input('enter topic name::')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse("topic created successfully")

def insert_webpage(request):


    TO=Topic.objects.get_or_create(topic_name='cricket')[0] 
    TO.save()
    n=input("enter name::")
    u=input('enter url::')
    WO=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]

    return HttpResponse('webpage created')



def insert_AcessRecord(request):
    TO=Topic.objects.get_or_create(topic_name='cricket')[0]
    TO.save()
    n=input("enter name")
    u=input("enter url")
    WO=WebPage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    d=input('enter date')
    a=input('enter author')
    AO=AcessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    AO.save()
    return HttpResponse('acess record created')