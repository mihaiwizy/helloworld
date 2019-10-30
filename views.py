from django.shortcuts import render
from django.http import HttpResponse# returneaza html

# Create your views here.
def homePageView(request):#creata de mine - va fi home page, request este un obiect care contine informatii despre solicitarea paginii
  html = "Hello, World!"#variabila cu string
  return HttpResponse(html)#returneaza un html cu stringul din variabila html din functie
  #Dupa ce s-a scris in views.py ce era de scris, functii etc., este nevoie  sa se comunice lui Django ce trebuie sa faca cu ce e in views.py, astfel se va scrie in urls.py unde va fi afisat ce e in views.py
