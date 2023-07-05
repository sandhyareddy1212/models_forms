from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
def first(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        print(username)
        print(password)
        return HttpResponse('Data is Submitted')
    return render(request,'first.html')


def insert_topic(request):
    if request.method=='POST':
        topic=request.POST['topic']

        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('Insertion of Topic is Done')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        n=request.POST['name']
        t=request.POST['tn']
        u=request.POST['url']
        print(t)
        TO=Topic.objects.get(topic_name=t)

        WO=webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
        WO.save()
        return HttpResponse('webpage is created')
    return render(request,'insert_webpage.html',d)

def retrieve_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        MSTS=request.POST.getlist('topic')
        print(MSTS)
        RWOS=webpage.objects.none()

        for i in  MSTS:
            RWOS=RWOS|webpage.objects.filter(topic_name=i)

        d1={'RWOS':RWOS}
        return render(request,'display_webpage.html',d1)


    return render(request,'retrieve_webpage.html',d)

def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        MSTS=request.POST.getlist('topic')
        print(MSTS)
        RWOS=webpage.objects.none()

        for i in  MSTS:
            RWOS=RWOS|webpage.objects.filter(topic_name=i)

        d1={'RWOS':RWOS}
        return render(request,'display_webpage.html',d1)


    return render(request,'checkbox.html',d)



def insert_AcessRecord(request):
    WTO = webpage.objects.all()
    d = {'WTO': WTO}
    if request.method=='POST':
        n=request.POST['name']#2
        d=request.POST['date']
        a=request.POST['author']
        WO = webpage.objects.get(id = n)#id=2#WDO
        AR=AcessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
        AR.save()
        return HttpResponse('AcessRecord is created')
    return render(request,'insert_AcessRecord.html', d)


def retrieve_AcessRecord(request):
    LWO=webpage.objects.all()
    d={'LWO':LWO}
    if request.method == 'POST':
        MSTS=request.POST.getlist('n')
        RWOS=AcessRecord.objects.none()
        for i in MSTS:
            RWOS=RWOS|AcessRecord.objects.filter(id = i)
        d1={'RWOS':RWOS}
        return render(request,'display_AcessRecord.html',d1)
    return render(request,'retrieve_AcessRecord.html',d)
    
