from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
conferences = [
    {'id':1,'title':"IT Essentials conference programs",
     'email':"tech@gmail.com",'description':"developing IT essentials skills"},
     {'id':2,'title':"Softwate development conference programs",
     'email':"tech@gmail.com",'description':"implementing software  essentials skills in ICT community"},
     {'id':3,'title':"Biomedical conference programs",
     'email':"biotech@gmail.com",'description':"developing IT essentials skills"},
     {'id':4,'title':"Mathematics conference programs",
     'email':"matechnology@gmail.com",'description':"developing IT  and managiment of mathematics essentials skills"},
     {'id':5,'title':"IT Essentials conference programs",
     'email':"tech@gmail.com",'description':"developing IT essentials skills"},
]

def conference(request):
    context = {'conferences':conferences}
    return render(request,'home.html',context)

def individualconference(request,pk):
 conference=None
 for i in conferences:
    if i['id']== int(pk):
       conference=i
       
 return render(request,'individualconference.html',{'conference':conference})


def createconference(request):
    return render(request,'create-conference.html')

def updateconference(request,pk):
 conference=None
 for i in conferences:
    if i['id']==int(pk):
       conference=i
 return render(request,'update-conference.html',{'conference':conference})

def deleteconference(request,pk):
 conference=None
 for i in conferences:
    if i['id']==int(pk):
       conference=i
 return render(request,'delete-conference.html',{'conference':conference})

