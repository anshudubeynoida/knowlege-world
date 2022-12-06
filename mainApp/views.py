from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.db.models import Q


def home(Request):
    data = blogpost.objects.all().order_by('id').reverse()[:8] 
    return render(Request,"index.html",{'data':data})

def shop(Request,mc,sc,br):
    if(mc=='All' and sc=='All' and br=='All'):
        data = blogpost.objects.all().order_by('id').reverse()
    elif(mc!='All' and sc=='All' and br=='All'):
        data = blogpost.objects.filter(maincategory=Maincategory.objects.get(name=mc)).order_by('id').reverse()
    elif(mc=='All' and sc!='All' and br=='All'):
        data = blogpost.objects.filter(subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
    elif(mc!='All' and sc!='All' and br=='All'):
        data = blogpost.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
    elif(mc!='All' and sc=='All' and br!='All'):
        data = blogpost.objects.filter(maincategory=Maincategory.objects.get(name=mc),brand=Brand.objects.get(name=br)).order_by('id').reverse()
    elif(mc=='All' and sc!='All' and br!='All'):
        data = blogpost.objects.filter(brand=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
    else:
        data = blogpost.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
    maincategory = Maincategory.objects.all()
    subcategory = Subcategory.objects.all()
    return render(Request,"post.html",{'data':data,'maincategory':maincategory,'subcategory':subcategory,'mc':mc,'sc':sc,'br':br})

def Pblog(Request,posturl):
    data = blogpost.objects.get(posturl=posturl)
    return render(Request,"blog.html",{'data':data});

# def post(Request):
#     return render(Request,"post.html")    

def contactPage(Request):
    if(Request.method=="POST"):
        c = Contact()
        c.name = Request.POST.get("name")
        c.email = Request.POST.get("email")
        c.phone = Request.POST.get("phone")
        c.subject = Request.POST.get("subject")
        c.message = Request.POST.get("message")
        c.save()
        messages.success(Request,"Thanks to Share Your Query With US!! Our Team Will Contact You Soon!!!!")
    return render(Request,"contact.html")


def searchPage(Request):
    search = Request.POST.get('search')
    data = blogpost.objects.filter(Q(name__icontains=search)|Q(description__icontains=search))
    maincategory = Maincategory.objects.all()
    subcategory = Subcategory.objects.all()
    return render(Request, "post.html", {'data': data, 'maincategory': maincategory, 'subcategory': subcategory, 'mc': 'All', 'sc': 'All'})    


def contactPage(Request):
    if(Request.method=="POST"):
        c = Contact()
        c.name = Request.POST.get("name")
        c.email = Request.POST.get("email")
        c.phone = Request.POST.get("phone")
        c.subject = Request.POST.get("subject")
        c.message = Request.POST.get("message")
        c.captcha = Request.POST.get("captcha")
        c.save()
        messages.success(Request,"Thanks to Share Your Query With US!! Our Team Will Contact You Soon!!!!")
    return render(Request,"contact.html")


# def life(Request):
#     data = blogpost.objects.all().order_by('id').reverse()[:8] 
#     return render(Request,"life.html",{'data':data})
    
def life(Request,mc,sc,br):
    if(mc=='All' and sc=='All' and br=='All'):
        data = blogpost.objects.all().order_by('id').reverse()
    elif(mc!='All' and sc=='All' and br=='All'):
        data = blogpost.objects.filter(maincategory=Maincategory.objects.get(name=mc)).order_by('id').reverse()
    elif(mc=='All' and sc!='All' and br=='All'):
        data = blogpost.objects.filter(subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
    elif(mc!='All' and sc!='All' and br=='All'):
        data = blogpost.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
    elif(mc!='All' and sc=='All' and br!='All'):
        data = blogpost.objects.filter(maincategory=Maincategory.objects.get(name=mc),brand=Brand.objects.get(name=br)).order_by('id').reverse()
    elif(mc=='All' and sc!='All' and br!='All'):
        data = blogpost.objects.filter(brand=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
    else:
        data = blogpost.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
    maincategory = Maincategory.objects.all()
    subcategory = Subcategory.objects.all()
    return render(Request,"life.html",{'data':data,'maincategory':maincategory,'subcategory':subcategory,'mc':mc,'sc':sc,'br':br})


def tech(Request,mc,sc,br):
    if(mc=='All' and sc=='All' and br=='All'):
        data = blogpost.objects.all().order_by('id').reverse()
    elif(mc!='All' and sc=='All' and br=='All'):
        data = blogpost.objects.filter(maincategory=Maincategory.objects.get(name=mc)).order_by('id').reverse()
    elif(mc=='All' and sc!='All' and br=='All'):
        data = blogpost.objects.filter(subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
    elif(mc!='All' and sc!='All' and br=='All'):
        data = blogpost.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
    elif(mc!='All' and sc=='All' and br!='All'):
        data = blogpost.objects.filter(maincategory=Maincategory.objects.get(name=mc),brand=Brand.objects.get(name=br)).order_by('id').reverse()
    elif(mc=='All' and sc!='All' and br!='All'):
        data = blogpost.objects.filter(brand=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
    else:
        data = blogpost.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
    maincategory = Maincategory.objects.all()
    subcategory = Subcategory.objects.all()
    return render(Request,"tech.html",{'data':data,'maincategory':maincategory,'subcategory':subcategory,'mc':mc,'sc':sc,'br':br})

def nature(Request,mc,sc,br):
    if(mc=='All' and sc=='All' and br=='All'):
        data = blogpost.objects.all().order_by('id').reverse()
    elif(mc!='All' and sc=='All' and br=='All'):
        data = blogpost.objects.filter(maincategory=Maincategory.objects.get(name=mc)).order_by('id').reverse()
    elif(mc=='All' and sc!='All' and br=='All'):
        data = blogpost.objects.filter(subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
    elif(mc!='All' and sc!='All' and br=='All'):
        data = blogpost.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
    elif(mc!='All' and sc=='All' and br!='All'):
        data = blogpost.objects.filter(maincategory=Maincategory.objects.get(name=mc),brand=Brand.objects.get(name=br)).order_by('id').reverse()
    elif(mc=='All' and sc!='All' and br!='All'):
        data = blogpost.objects.filter(brand=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
    else:
        data = blogpost.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
    maincategory = Maincategory.objects.all()
    subcategory = Subcategory.objects.all()
    return render(Request,"nature.html",{'data':data,'maincategory':maincategory,'subcategory':subcategory,'mc':mc,'sc':sc,'br':br})

def mobile(Request,mc,sc,br):
    if(mc=='All' and sc=='All' and br=='All'):
        data = blogpost.objects.all().order_by('id').reverse()
    elif(mc!='All' and sc=='All' and br=='All'):
        data = blogpost.objects.filter(maincategory=Maincategory.objects.get(name=mc)).order_by('id').reverse()
    elif(mc=='All' and sc!='All' and br=='All'):
        data = blogpost.objects.filter(subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
    elif(mc!='All' and sc!='All' and br=='All'):
        data = blogpost.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
    elif(mc!='All' and sc=='All' and br!='All'):
        data = blogpost.objects.filter(maincategory=Maincategory.objects.get(name=mc),brand=Brand.objects.get(name=br)).order_by('id').reverse()
    elif(mc=='All' and sc!='All' and br!='All'):
        data = blogpost.objects.filter(brand=Brand.objects.get(name=br),subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
    else:
        data = blogpost.objects.filter(maincategory=Maincategory.objects.get(name=mc),subcategory=Subcategory.objects.get(name=sc)).order_by('id').reverse()
    maincategory = Maincategory.objects.all()
    subcategory = Subcategory.objects.all()
    return render(Request,"mobile.html",{'data':data,'maincategory':maincategory,'subcategory':subcategory,'mc':mc,'sc':sc,'br':br})


def facts(Request):
    data = blogpost.objects.all().order_by('id').reverse()[:8] 
    return render(Request,"facts.html",{'data':data})